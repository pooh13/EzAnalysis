"""EmotionDiary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

app_name = 'AI_analyze'
urlpatterns = [
    path('callback/', views.callback),
    # path('userinform/<str:pk>', views.user_inform_from, name='userinfo'),  # kelly
    path('test/', views.test, name='test'),
    path('add/', views.add, name='add'),
    path('userdata/', views.userdata, name='userdata'),
    path('userdata2/', views.userdata2, name='userdata2'),

    path('index/', views.index, name='index'),
    path('usertest/', views.usertest, name='usertest'),
    path('userinform/', views.user_inform_from, name='userinfo'),
    # path('editdiary/', views.edit_diary, name='edit_diary'),
    path('menudiary/', views.menu_diary, name='menu_diary'),
]
