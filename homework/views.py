from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *

# 과제 show
def showlist(request):
  return render(request, 'hw_list.html')

# 과제 작성 페이지
def writehw(request):
  homework = Homework.objects.last()
  all_hw = Homework.objects.all()
  context = {
    'all_hw': all_hw,
    'homework': homework
  }
  return render(request, 'hw_write.html', context)

# 과제 작성 action
def createassign(request):
  if request.method == "POST":
    new_as = Assignment()
    new_as.title = request.POST.get('title')
    new_as.writer = request.user
    new_as.url = request.POST.get('url')
    new_as.pub_date = timezone.now()
    new_as.contents = request.POST.get('contents')
    homeworkId = request.POST.get('hw_id')
    new_as.hw_id = get_object_or_404(Homework, id=homeworkId)
    new_as.save()
  return redirect('homework:showdetail', new_as.id)

# 과제 상세 페이지
def showdetail(request, assignment_id):
  assign = get_object_or_404(Assignment, id=assignment_id)
  return render(request, 'hw_detail.html', { 'assign': assign })