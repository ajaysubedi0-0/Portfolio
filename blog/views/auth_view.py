from django.shortcuts import render


def login(request):
  return(request,'auth/login.html')