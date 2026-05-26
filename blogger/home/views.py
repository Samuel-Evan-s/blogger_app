from django.shortcuts import render, redirect
from datetime import datetime
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import SignupForm

# Create your views here.
class LogoutView(LogoutView):
    template_name = 'home/logout.html'

class LoginView(LoginView):
    template_name = 'home/login.html'

class SignupView(FormView):
    form_class = SignupForm
    template_name = 'home/signup.html'
    success_url = reverse_lazy('home.login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'
    extra_context = {'todays_date': datetime.today()}
    login_url = '/home/login/'
    




