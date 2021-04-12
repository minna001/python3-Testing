from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'app1/home.html',{'password':"gjgjgjgjgjgjg"})

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get("Special Characters"):
        characters.extend(list("!@#$%&?"))
    
    length = int(request.GET.get('length',12))
    thepassword = ""
    for x in range( length):
        thepassword += random.choice(characters)

    return render(request, "app1/password.html",{'password':thepassword})

def about(request):
    return render(request,"app1/about.html")

