from .views import PrilagodjeniLoginView
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('registracija/', views.registracija, name='registracija'),
    path('dodaj_proizvod/', views.dodaj_proizvod, name='dodaj_proizvod'),
    path('dodaj_komentar/<int:proizvod_id>/', views.dodaj_komentar, name='dodaj_komentar'),
    path('dodaj_ocenu/<int:proizvod_id>/', views.dodaj_ocenu, name='dodaj_ocenu'),
    path('posalji_poruku/', views.posalji_poruku, name='posalji_poruku'),
    path('primljene_poruke/', views.primljene_poruke, name='primljene_poruke'),
    path('profile_settings/', views.profile_settings, name='profile_settings'),
    path('login/', PrilagodjeniLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='prodaja/logout.html'), name='logout'),
]
