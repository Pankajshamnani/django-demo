from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')
def add(request):
    n1=int(request.POST['num1'])
    n2=int(request.POST['num2'])
    n3=n1+n2
    return render(request,'results.html',{'res':n3})
