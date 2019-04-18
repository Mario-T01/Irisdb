from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Client

from django.views import generic

class IndexView(generic.ListView):
	  template_name = 'clients/index.html'
    # client_list grabs all the clients in database 
	  context_object_name = 'client_list'
    # gets top 3 names from and is in acending  order
	  def get_queryset(self):
	  	 return Client.objects.order_by('created_date')[:3]
