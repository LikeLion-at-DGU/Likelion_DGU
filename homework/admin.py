from django.contrib import admin
from .models import Homework, Assignment

# Register your models here.
admin.site.register([Homework, Assignment])