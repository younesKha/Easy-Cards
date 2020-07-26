from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
# Create your views here.



def test(request):
    return HttpResponse("<h1>Good 0110 Morning</h1>")



def home(request):
    return render(request,'promo/base.html')





