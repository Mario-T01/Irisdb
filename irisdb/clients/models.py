from django.db import models
import datetime
# Create your models here.

from django.db import models
from django.utils import timezone


class Client(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    client_created_date = models.DateTimeField('date created')
    def __str__(self):
        return self.client_firstname
    def was_created_recently(self):
        return self.created_date >= timezone.now()
        datetime.timedelta(days=1)
    #def fullname(self):
    #    client_fullname = CONCAT(client_firstname, ' ',client_lastname)
        #created_date = models.DateTimeField('date created')
    #    return self.client_fullname


class Referred_by(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    referred_by_opts = models.CharField(max_length=10)
    def __str__(self):
        return self.referred_by_opts
