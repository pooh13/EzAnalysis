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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'EmotionDiary'
urlpatterns = [
    path('callback/', views.callback),
    path('index/', views.index, name='index'),
    path('menuDiary/', views.menu_diary, name='menuDiary'),
    path('addDiary1/<pk>', views.add_diary1, name='addDiary1'),
    path('addDiary2/', views.add_diary2, name='addDiary2'),
    path('addDiary3/', views.add_diary3, name='addDiary3'),
    path('editDiary/<pk>', views.edit_diary, name='editDiary'),
    path('profile/', views.profile, name='profile'),
    path('editUser/<pk>', views.edit_user, name='editUser'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
