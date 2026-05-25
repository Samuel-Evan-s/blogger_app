from django.shortcuts import render
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'home/home.html'
    extra_context = {'todays_date': datetime.today()}
    login_url = '/admin/login/'




