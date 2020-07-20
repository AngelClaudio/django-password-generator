# Render lets you pass a template that turns into an http response
from django.shortcuts import render

# Step 1 Need to return HttpResponse so import this module
from django.http import HttpResponse

# Create your views here.

def home(request):
    # Step 2 Use render, 1st arg is request, 2nd arg is the html path,
    # 3rd argument is content being passed to view.
    return render(request, 'generator/home.html')

def password(request):

    return render(request, 'generator/password.html')
