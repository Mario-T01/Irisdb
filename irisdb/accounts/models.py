from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,

    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=True)
    admin = models.BooleanField(default=True)

    # Password field absent bc its built if __name__ == '__main__':

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #email and PW required by defaultself.

    def get_full_name(self):
        #the user is identified by their email address
        return self.email

    def __str__(self):
        return self.email
