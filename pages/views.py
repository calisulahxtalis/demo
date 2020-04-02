from django.shortcuts import render

# Create your views here.
def indexPage(request,*args, **kwargs):
  return render(request, 'index.html',{})
