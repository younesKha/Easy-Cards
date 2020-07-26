from django.shortcuts import render ,redirect 
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers

from .forms import  CreateUserForm
from .forms import GroupForm,CardForm
from .models import c_groups,c_cards
from .serializers import group_ser

def logout_site(request):
    logout(request)
    return redirect('cards:login')
def login_site(request):
    if request.user.is_authenticated:
        return redirect('cards:cards')

    if request.method== 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('cards:cards')
        else:
            messages.info(request, 'Username OR password is incorrect')


        return render(request,'cards/login.html',{"title":"ADD New USer","msg":'Good' +username})
    else:
        return render(request,'cards/login.html',{"title":"ADD New USer","msg":''})

    return render(request,'cards/login.html',{"title":"ADD New USer","msg":'Good' +username})



def cards(request):
    if request.user.is_authenticated:
        cards = c_cards.objects.filter(cuser=request.user.id).order_by('-id')
        #messages.success(request, 'Account was created for ' + request.user.username)
        is_empty = cards.count() <= 0
        return render(request,'cards/cards.html',{"title":"All cards","username":request.user.username ,'cards':cards , 'is_empty':is_empty })
    else:
        return redirect('cards:login')

def search(request,txt):
    if request.user.is_authenticated:
        cards = c_cards.objects.filter(title__contains=txt)
        #messages.success(request, 'Account was created for ' + request.user.username)
        return render(request,'cards/cards.html',{"title":"search ","username":request.user.username ,'cards':cards })
    else:
        return redirect('cards:login')
        

def load_groups(request):
    if request.user.is_authenticated:
        groups = c_groups.objects.filter(cuser=request.user.id)
        serializer = group_ser(groups,many=True)
        return JsonResponse(serializer.data,safe=False)
    else:
        return redirect('cards:login')
#aa@gmail.com
def register(request):
    if request.user.is_authenticated:
        
        
        return redirect('cards:cards')

    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user=form.save()
                c_groups.objects.create(name='My Group', cuser=user,remember=0)
                login(request , user)
                messages.success(request, 'Account was created for ' + form.cleaned_data.get('username'))
                return redirect('cards:cards')
            else:
                return render(request, 'cards/register.html', {'form':form})                           
			

        context = {'form':form}
        return render(request, 'cards/register.html', context)



    #return render(request,'cards/register.html',{"title":"ADD New USer","msg":'Good'})

def save_group(request):
    if request.user.is_authenticated:
        if request.method== 'POST':
        
            form=GroupForm(request.POST)
            if form.is_valid():
                c_groups.objects.create(name=request.POST['name'], cuser=request.user,remember=request.POST['remember'])
                name =  request.POST['name'];
                messages.success(request, f"a group was created: {name}")
                
                return JsonResponse({"res":'1','msg': f"group was created: {name}"})
            else:
                return JsonResponse({'res': '0','msg': str(form.errors)})
    else:
        return redirect('cards:login')

def save_card(request):
    if request.user.is_authenticated:
        if request.method== 'POST':
        
            form=CardForm(request.POST)
            
            if form.is_valid():
                c_cards.objects.create(title=request.POST['title'],group_id= c_groups.objects.get(id=request.POST['group_id']),body=request.POST['body'],remember=request.POST['remember'], cuser=request.user,importancy= request.POST['importancy'])
                title =  request.POST['title'];
                messages.success(request, f"Card was created: {title}")
                
                return JsonResponse({"res":'1','msg': f"card was created: {title}"})
            else:
                return JsonResponse({'res': '0','msg': str(form.errors)})
    else:
        return redirect('cards:login')

def delete_card(request,id):
    if request.user.is_authenticated:
        cards = c_cards.objects.get(id=id)
        cards.delete()
        return JsonResponse({'res': '1','msg': 'card was deleted:'+str(cards.title)})
        messages.success(request, f"Card was deleted: {cards.title}")
    else:
        return JsonResponse({'res': '0','msg':'Error'})

#def update_group(request):
#    form=GroupForm()
#    return render(request,'cards/update_group.html',{"form":form})

def groups(request):

    if request.user.is_authenticated:
        groups = c_groups.objects.filter(cuser=request.user.id)
        return render(request,'cards/groups.html',{"title":"My Groups","groups":groups})
    else:
        return redirect('cards:login')
from itertools import chain
def home(request):
    if request.user.is_authenticated:
        groups = c_groups.objects.filter(cuser=request.user.id).order_by('-id')
        ccards= list()
        
        for gr in groups:
            cards = c_cards.objects.filter(cuser=request.user.id,group_id=gr.id).order_by('group_id').order_by('-id')[0:3]
            ccards =ccards + list(chain(cards))

        print(ccards)

        return render(request,'cards/home.html',{"title":"My Cards","msg":'Good','cards':ccards,'groups':groups , "username":request.user.username })
    else:
        return redirect('cards:login')

def levels(request,sel_lev):
    if request.user.is_authenticated:
        cards = c_cards.objects.filter(cuser=request.user.id,importancy=sel_lev).order_by('id')
        return render(request,'cards/levels.html',{"title":"level:"+ str(sel_lev),"cards":cards})
    else:
        return redirect('cards:login')

def remember(request):
    if request.user.is_authenticated:
        cards = c_cards.objects.filter(remember=1).order_by('-id')
        #messages.success(request, 'Account was created for ' + request.user.username)
        return render(request,'cards/cards.html',{"title":"remember cards","username":request.user.username ,'cards':cards })
    else:
        return redirect('cards:login')


def display_group(request,id):
    if request.user.is_authenticated:
        cards = c_cards.objects.filter(group_id=id).order_by('-id')
        group = c_groups.objects.get(id=id)
        #messages.success(request, 'Account was created for ' + request.user.username)
        return render(request,'cards/display_group.html',{"title":"group name : " + group.name,"username":request.user.username ,'cards':cards })
    else:
        return redirect('cards:login')


def forgot_password(request):
    return render(request,'cards/forgot-password.html',{"title":"groups","msg":'Good'})



    


