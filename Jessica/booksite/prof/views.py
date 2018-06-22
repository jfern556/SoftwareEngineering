from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegistrationForm
from .models import USER, ADDRESS, USER_HOME_ADDRESS



def home (request):

    return render(request, "home.html", {})

def RegistrationView (request):
    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            First_Name = request.POST.get('First_Name')
            Last_Name = request.POST.get('Last_Name')
            Username = request.POST.get('Username')
            Email = request.POST.get('Email', ' ')
            Address = request.POST.get('Address', ' ')
            City = request.POST.get('City', ' ')
            Zip_Code = request.POST.get('Zip_Code', ' ')
            psw = request.POST.get('psw')
            user_obj = USER(Email = Email, Username = Username,Fname= First_Name, Lname= Last_Name, Password= psw )
            user_obj.save()

            return HttpResponse(reversed ('home::register'))

    else:
        form = RegistrationForm()

    return render (request, 'register.html', {'form': form,})

def login(request):
    return render(request, "login.html", {})



