from django.shortcuts import render, redirect, HttpResponse

def home(request):
  return redirect('login')
  
def login(request):
  return render(request,'authentication/login.html')
