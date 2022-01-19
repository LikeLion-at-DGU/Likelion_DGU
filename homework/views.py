from django.shortcuts import render

# Create your views here.
def showlist(request):
  return render(request, 'hw_list.html')

def writehw(request):
  return render(request, 'hw_write.html')