from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    tpassword = ''
    forma = list('qwertyuiopasdfghjklzxcvbnm')
    lenght = int(request.GET.get('lenght'))
    
    if request.GET.get('numbers'):
        forma.extend(list('1234567890'))
    if request.GET.get('uppercase'):
        forma.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    
    for i in range(lenght):
        tpassword += random.choice(forma)

    return render(request, 'generator/password.html', {'password':tpassword})


def aboutthis(request):
    return render(request, 'generator/about.html')