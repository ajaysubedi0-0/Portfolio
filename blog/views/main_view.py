from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request,'main/home.html') 

def create(request):
  return render(request,'main/create.html')

def edit(request):
  return render(request,'main/edit.html')

def delete(request):
  return render(request,'main/delete.html')

def single_blog(request):
  return render(request,'main/single_blog.html')
