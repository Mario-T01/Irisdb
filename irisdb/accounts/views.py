from django.shortcuts import get_object_or_404, render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import User
from django import forms
from django.views import generic

# Create your views here.

def register(request):
        #model = User
        form = UserCreationForm()
        return render(request,'accounts/register.html',{'form':form})

#class IndexView(request):
#     template_name = 'accounts/index.html'
#     return render(request,'accounts/index.html')
