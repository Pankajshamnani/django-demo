from django.shortcuts import render
from .models import Shoe


shoes=Shoe.objects.all()

def index(request):
    return render(request,'index.html',{'shoes':shoes})
def category(request):
    return render(request,'login.html')