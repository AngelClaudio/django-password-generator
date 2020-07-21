# Render lets you pass a template that turns into an http response
from django.shortcuts import render

# Step 1 Need to return HttpResponse so import this module
from django.http import HttpResponse

import random

# Create your views here.
def about(request):
    return render(request, 'generator/about.html')

def home(request):
    # Step 2 Use render, 1st arg is request, 2nd arg is the html path,
    # 3rd argument is content being passed to view.
    return render(request, 'generator/home.html')

def password(request):
    thepassword = ''
    alphabet = 'abcdefghijklmnopqurstuvwxyz'
    characters = list(alphabet)

    # Use request object then use get attribute
    # 2nd argument is for default parameter
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend(list(alphabet.upper()))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password' : thepassword})
