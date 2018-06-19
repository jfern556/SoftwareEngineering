from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'user/index.html', {})

def login(request):
    
    form = forms.LoginForm()

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("User name is: " + form.cleaned_data['username'])
        else:
            print("FORM DATA INVALID!")

    return render(request, 'user/login.html', {'form': form}) 

    

    