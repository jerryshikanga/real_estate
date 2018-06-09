from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import os
from django.urls import reverse_lazy
from django.conf import settings


# Create your models here.
class Agent(models.Model) :
    telephone = models.IntegerField(verbose_name='Phone Number')
    address = models.CharField(verbose_name='Physical Address', max_length=200, null=True)
    description = models.TextField(verbose_name='Description')
    picture = models.ImageField(verbose_name='Picture', upload_to="agent")
    date_added = models.DateField(default=timezone.now)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.user.get_full_name() is not "" :
            return self.user.get_full_name()
        else:
            return self.user.username

    def get_absolute_url(self):
        return reverse_lazy('agent:detail', kwargs={'pk':self.pk})