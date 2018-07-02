from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from .forms import RegistrationForm
from database.models import USER, ADDRESS, USER_HOME_ADDRESS

from django.contrib.auth.models import User as AuthUser # <-------

def home (request):
    #return render(request, "home.html", {})
    return render(request, "homepage/index.html", {}) #temp

def RegistrationView (request):
    if request.method =="POST":
        
        request.session
        #test
        print("WAS POST")
        form = RegistrationForm(request.POST)
        if form.is_valid():
            First_Name = request.POST.get('First_Name')
            Last_Name = request.POST.get('Last_Name')
            Username = request.POST.get('Username')
            Email = request.POST.get('Email', ' ')
            #Address = request.POST.get('Address', ' ') 
            HomeAddress = request.POST.get('Address', ' ')
            City = request.POST.get('City', ' ')
            Zip_Code = request.POST.get('Zip_Code', ' ')
            psw = request.POST.get('psw')
            #user_obj = USER(Email = Email, Username = Username,Fname= First_Name, Lname= Last_Name, Password= psw ) #won't work with new model, USER attributes changed
            
            #Store Address
            print("creating Address...")
            HomeAddr = USER_HOME_ADDRESS()
            Addr = ADDRESS()
            Addr.Zip_Post = Zip_Code
            Addr.Address_1 = "" #fill this in later when user can fill this in a seperate form
            Addr.Address_2 = "" #fill this in later when user can fill this in a seperate form
            Addr.Country = "" #fill this in later when user can fill this in a seperate form
            Addr.State = "" #fill this in later when user can fill this in a seperate form
            Addr.City_Town = City
            Addr.Name = "" #fill this in later when user can fill this in a seperate form
            
            print("saving address...")
            Addr.save()
            HomeAddr.Address_ID = Addr
            HomeAddr.save()

            #Store AuthUser
            print("creating AuthUser")
            AuthUser_ID = AuthUser()
            AuthUser_ID.first_name = First_Name
            AuthUser_ID.last_name = Last_Name
            AuthUser_ID.email = Email
            AuthUser_ID.set_password(psw)
            AuthUser_ID.username = Username
            print("saving AuthUser...")
            AuthUser_ID.save()
            
            print("creating USER...")
            #Store USER
            user_obj = USER()
            user_obj.AuthUser_ID = AuthUser_ID
            user_obj.Home_address_ID
            user_obj.Preferred_credit_card_ID = None
            user_obj.Cart_ID = None
            user_obj.Nick_name = ''
            print("Saving user_obj....")
            user_obj.save()
            
            print("Sucess!:)")
            
            #return HttpResponse(reversed ('home::register'))
            return HttpResponseRedirect(reverse('homepage:index'))#send to home page for now, i'm not sure what above statement does
        else:
            #test
            print("Form was invalid!!!")
            print(form.errors)
    else:
        #test
        print("NOT POST")
        form = RegistrationForm()

    #return render (request, 'register.html', {'form': form,})
    return render (request, 'prof/register.html', {'form': form,})

def login(request):
    #return render(request, "login.html", {})
    return render(request, "prof/login.html")