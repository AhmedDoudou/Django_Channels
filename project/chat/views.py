from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q

# Create your views here.

def Index(request):    
    messages =MSG.objects.all()
    context = { "messages":messages,}
    return render(request,'chat/index.html',context)