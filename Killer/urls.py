from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('login.html', views.loginView, name='register'),
    path('logout.html', views.logoutView, name='logout'),
    path('kill.html', views.killView, name='kill'),
]
