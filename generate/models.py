from django.db import models
from accounts.models import UserProfileInfo
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Predictions(models.Model):
    profile = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, related_name='predict')
    filename = models.CharField(max_length = 200,default="CFG.py")



    def get_absolute_url(self):
        return reverse('predict:predict', kwargs={'pk': self.profile.pk})
