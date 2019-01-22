from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Client

from django.views import generic


class IndexView(generic.ListView):
    tempalte_name = 'clients/index.html'
    content_object_name = 'latest_client_list'

    def get_queryset(self):
        """Return the last five created clients."""

        return Client.objects.order_by('-created_date')[:5]
