from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def showlist(request):
  return render(request, 'hw_list.html')

def writehw(request):
  homework = Homework.objects.last()
  all_hw = Homework.objects.all()
  context = {
    'all_hw': all_hw,
    'homework': homework
  }
  return render(request, 'hw_write.html', context)

def showdetail(request):
  return render(request, 'hw_detail.html')