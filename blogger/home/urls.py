from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name='home.login'),
    path('logout/', views.LogoutView.as_view(), name='home.logout'),
    path('signup/', views.SignupView.as_view(), name='home.signup'),
]