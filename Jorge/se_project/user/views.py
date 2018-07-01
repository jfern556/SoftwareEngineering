from django.shortcuts import render
from . import forms
from django.contrib.auth import authenticate
from django.contrib.auth import login as log_user_in
from django.http import HttpResponseRedirect



def index(request):
    return render(request, 'user/index.html', {})

def login(request):
    form = forms.LoginForm()

    return render(request, 'user/login.html', {'form':form})

def processlogin(request):
    
    form = forms.LoginForm()

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            print("FORM VALIDATION SUCCESS!")
            print("User name is: " + form.cleaned_data['username'])
            
            print("Now we validate user...")

            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if  user is not None:
                print("This is a valid user!")

                print("logging user in...")

                log_user_in(request, user) #this is login function renamed to log_user_in

                print("Done logging user in")

                return HttpResponseRedirect('http://localhost:8000/') # Static reference!!!

            else:
                print("INVALID USER!")
        else:
            print("FORM DATA INVALID!")

    return render(request, 'user/login.html', {'form': form}) 



    

    