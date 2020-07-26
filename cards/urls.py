"""main_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
app_name = "cards"


urlpatterns = [
    path('login', views.login_site, name='login'),
    path('logout', views.logout_site, name='logout'),
    path('forgot_password', views.forgot_password, name='forgot_password'),




    path('cards', views.cards, name='cards'),
    path('cards/', views.cards, name='cards'),

    path('register', views.register, name='register'),

    path('home', views.home, name='groups'),
    path('groups', views.groups, name='groups'),
    path('levels', views.levels, name='groups'),
    path('remember', views.remember, name='groups'),

     path('save_group',views.save_group, name='update_group'),
     path('save_card',views.save_card, name='update_group'),
    path('load_groups',views.load_groups, name='load_groups'),



    path('levels/<int:sel_lev>',views.levels, name='levels'),
    path('delete_card/<int:id>',views.delete_card, name='levels'),

    path('display_group/<int:id>',views.display_group, name='display_group'),
    path('search/<str:txt>', views.search, name='search'),

]
