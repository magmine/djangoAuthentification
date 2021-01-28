'''
à faire : ajouter une page d'authentification pour l'application
'''

from django.shortcuts import render
from .models import Person
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    params = {
        'users' : Person.objects.all()
    }
    return render(request, 'app/index.html', params)

def user_login(request):
    if request.method == "POST":
        user_name = request.POST['username']
        passwd = request.POST['passwd']
        if authenticate(user_name, passwd) == True:
            print("--------> Good")
        else:
            print("-----------> Bad")