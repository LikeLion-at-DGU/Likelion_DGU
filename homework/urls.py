from unicodedata import name
from django.urls import path
from .views import *

app_name='homework'
urlpatterns = [
  path('list/', showlist, name="showlist"),
  path('write/', writehw, name="writehw"),
  path('create/', createassign, name="createassign"),
  path('<int:assignment_id>/', showdetail, name="showdetail"),
  path('<int:assignment_id>/delete', delete_assign, name="delete_assign"),
  path('<int:assignment_id>/edit', edit_assign, name="edit_assign"),
]
