from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# 과제 show
def showlist(request):
  # 유저별 과제
  assign = Assignment.objects.filter(writer=request.user).order_by('-pub_date')
  # 멘토가 보는 모든 과제
  all_assign = Assignment.objects.all().order_by('-pub_date')
  paginatorAssign = Paginator(assign, 10)
  paginator_allAssign = Paginator(all_assign, 10)
  page = request.GET.get('page')
  # 페이지 네이션 할당
  assignments = paginatorAssign.get_page(page)
  all_assignments = paginator_allAssign.get_page(page)
  context = {
    'assignments' : assignments,
    'all_assignments' : all_assignments 
  }
  return render(request, 'hw_list.html', context)

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
    new_as.image = request.FILES.get('image')
    homeworkId = request.POST.get('hw_id')
    new_as.hw_id = get_object_or_404(Homework, id=homeworkId)
    new_as.save()
  return redirect('homework:showdetail', new_as.id)

# 과제 상세 페이지
def showdetail(request, assignment_id):
  assign = get_object_or_404(Assignment, id=assignment_id)
  return render(request, 'hw_detail.html', { 'assign': assign })

#과제 삭제하기
@login_required
def delete_assign(request, assignment_id):
  assign = get_object_or_404(Assignment, pk=assignment_id)
  assign.delete()
  return redirect('homework:showlist')

#과제 수정하기
@login_required
def edit_assign(request, assignment_id):
  assign = get_object_or_404(Assignment, pk=assignment_id)
  if assign.writer == request.user:
    if request.method == "POST":
      assign.title = request.POST['title']
      assign.url = request.POST['url']
      assign.contents = request.POST['contents']
      assign.image = request.FILES['image']
      assign.save()
      return redirect('homework:showdetail', assign.id )
  return render(request, 'hw_edit.html', { 'assign':assign })

# 멘토 - 과제 작성 페이지
def admin_writehw(request):
  return render(request, 'admin_hw_create.html')

# 멘토 - 과제 create
def admin_createhw(request):
  if request.method == "POST":
    new_hw = Homework()
    new_hw.title = request.POST.get('title')
    new_hw.writer = request.user
    new_hw.endDate = request.POST.get('endDate')
    new_hw.contents = request.POST.get('contents')
    new_hw.save()
  return redirect('homework:admin_showlist')

# 멘토 - 과제 show
def admin_showlist(request):
  # 멘토가 보는 모든 과제
  all_hw = Homework.objects.all().order_by('-pub_date')
  paginator_allHw = Paginator(all_hw, 10)
  page = request.GET.get('page')
  # 페이지 네이션 할당
  all_homeworks = paginator_allHw.get_page(page)
  context = {
    'all_homeworks' : all_homeworks
  }
  return render(request, 'admin_hw_list.html', context)

# 멘토 - 과제 detail
def admin_showdetail(request, homework_id):
  homework = get_object_or_404(Homework, id=homework_id)
  return render(request, 'admin_hw_detail.html', { 'homework': homework })

# 멘토 - 과제 수정하기
@login_required
def admin_edit(request, homework_id):
  homework = get_object_or_404(Homework, pk=homework_id)
  if homework.writer == request.user:
    if request.method == "POST":
      homework.title = request.POST['title']
      homework.contents = request.POST['contents']
      homework.endDate = request.POST['endDate']
      homework.save()
      return redirect('homework:admin_showdetail', homework.id )
  return render(request, 'admin_hw_edit.html', { 'homework':homework })


# 멘토 - 과제 삭제하기
@login_required
def admin_delete(request, homework_id):
  homework = get_object_or_404(Homework, pk=homework_id)
  homework.delete()
  return redirect('homework:admin_showlist')