from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from accounts.forms import SignUpForm
from accounts.models import User


class SignUp(generic.CreateView):
    form_class = SignUpForm
    model = User
    success_url = reverse_lazy('login')
    template_name = 'signup.html'