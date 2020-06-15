from django.contrib import admin
from generate.models import Predictions
from django import forms

class Prediction(admin.ModelAdmin):
    list_display=('profile','filename')
admin.site.register(Predictions,Prediction)
# Register your models here.
