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
  path('admin_writehw/', admin_writehw, name='admin_writehw'),
  path('admin_createhw/', admin_createhw, name="admin_createhw"),
  path('homeworklist/', admin_showlist, name="admin_showlist"),
  path('hwDetail/<int:homework_id>', admin_showdetail, name="admin_showdetail"),
  path('hwDelete/<int:homework_id>', admin_delete, name="admin_delete"),
  path('hwEdit/<int:homework_id>', admin_edit, name="admin_edit"),
]
