'''
à faire : ajouter une page d'authentification pour l'application
'''

from django.shortcuts import render, redirect
from .models import Person
#from django.contrib.auth import authenticate, login, logout
from django.contrib import auth, messages
# Create your views here.


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django import forms


class SignupForm(UserCreationForm):
   class Meta(UserCreationForm.Meta):
       model = Person
       fields = ['username', 'phone_number', 'ville']

class SignUpView(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# def index(request):
#     params = {
#         'users' : Person.objects.all()
#     }
#     return render(request, 'app/login.html', params)


'''
If the number of users is big then I can have lots of request consuming memory
    => Only necessary fields should be stored in the requests
    => Requests should be temporary
'''

def user_login(request): # each request is related to it's own user
    if request.method=='POST':
        try:        
            username=request.POST['username']
            password = request.POST['password']
            if Person.objects.filter(username=username).exists():
                user = Person.objects.get(username=username)
                if user.check_password(password):
                    user = auth.authenticate(username=username, password=password)
                    if user is not None:
                        auth.login(request, user)
                        return redirect('/')
            else:
                return redirect('login')
        except Exception as problem:
            return redirect('login')
    return render(request, 'app/login.html')
