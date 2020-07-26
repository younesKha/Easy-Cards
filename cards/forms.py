from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import c_cards,c_groups

class GroupForm(ModelForm):
	class Meta:
		model = c_groups
		fields = ['name', 'remember']
        #widget={
        #    'username': form.
        #}

class CardForm(ModelForm):
	class Meta:
		model = c_cards
		fields = ['title', 'body' , 'group_id','importancy','remember']
        #widget={
        #    'username': form.
        #}



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
        #widget={
        #    'username': form.
        #}