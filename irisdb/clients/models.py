from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Client(models.Model):
    client_firstname = models.CharField(max_length=10)
    client_lastname = models.CharField(max_length=10
    client_fullname = CONCAT(client_firstname, ' ',client_lastname)
    created_date = models.DateTimeField('date created')
    def __str__(self):
        return self.client_fullname

class Referred_by(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    referred_by_opts = models.CharField(mad_length=10)
    def __str__(self):
        return self.referred_by_opts
