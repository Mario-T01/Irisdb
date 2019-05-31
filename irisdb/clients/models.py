from django.db import models
import datetime
# Create your models here.

from django.db import models
from django.utils import timezone


class Client(models.Model):
    first_name = models.CharField(max_length=15, blank=False, default='')
    last_name = models.CharField(max_length=15, blank=False, default='')
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name
    def was_created_recently(self):
        return self.created_date >= timezone.now()
        datetime.timedelta(days=1)

    class Meta:
        ordering = ('first_name',)


class Referred_by(models.Model):
    Client_info = models.ForeignKey(Client, on_delete=models.CASCADE)
    referred_by_opts = models.CharField(max_length=10)
    def __str__(self):
        return self.referred_by_opts
