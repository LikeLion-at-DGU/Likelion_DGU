from django.urls import path
from .views import *

app_name='homework'
urlpatterns = [
  path('list/', showlist, name="showlist")
]
