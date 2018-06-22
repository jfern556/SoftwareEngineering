from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader#bucky video

#from .models import myCart



# Create your views here.
def index(request):
    #return HttpResponse('HELLO FROM POSTS')
    
    '''
    posts = Post.objects.all()[0:10]  
    

    context = {
        'title': 'Latest Posts',
        'posts': posts
    }

    
    return render(request, 'post/index.html', context)
    '''    
    
    return HttpResponse('Just text :[')#
    #return render(request, 'myCart/index.html')

def myCart(request):    
    return render(request, 'myCart/myCartSimple.html')

def index2(request):
    return HttpResponse("HELLO WORLD!")

#VIEWS FOR TESTING

def consoleSessionDisplay(request):    
    for key, value in request.session.items():         
        print('{} => {}'.format(key, value))
    return HttpResponse("Check command promt for session information!")

def makeCookieTest(request):
    return ""

def makeCookieWorkedTest(request):
    ""


#can't find the example.html, but can find files like index.html and
def example(request):
    template = loader.get_template('myCart/example.html')
    
    #return render(request, 'myCart/example.html')
    return HttpResponse(template.render({},request))

#test, doesn't work
from user.models import GENRE
def example2(request):
    all_genre=GENRE.objects.all()
    template = loader.get_template('myCart/example.html')
    context = {'all_genre':all_genre}
    #return render(request, 'myCart/example.html')
    return HttpResponse(template.render(context, request))

#test
def createCookieLogin(request):
    return ""

from django.http import HttpResponse
from django.shortcuts import render
def createCookieTest(request):    

    if request.session.test_cookie_worked():
        
        #the cookie worked, let's get information
        #about the session to see if we can find the cookie
        html = "<h1>Test Cookie Worked!<h1><br>"
        html += "<h3>Here's some information about the session: <h3><br>"

        for key in request.session.keys():
            html+=("Session key: "+str(key)+"<br>&emsp;:=> request.session["+str(key) +"]: "+str(request.session[key])+"<br>")
        
        html+="<br> Now I'm going to delete it!"
        
        
        request.session.delete_test_cookie()        
        return HttpResponse(html)
    else:
        request.session.set_test_cookie()        
        return HttpResponse("Test cookie failed or no test cookie set yet"
        "<br>Please reload this page.")
    

def createCookieTest2(request):
    """
    if request.method == 'POST':
        if request.session.test_cookies_worked():
            print("The test cookie worked!")
            return HttpResponse("You're logged in.")
        else:
            return HttpResponse("Please enable cookies and try again.")
    
    print("Request method was not POST. setting up a test cookie!")
    request.session.set_test_cookie()
    """
    
    return HttpResponse("No form detected, setting up a test cookie.")

#http://localhost:8000/myCart/cookieInfo
def cookieInfo(request):
    if request.COOKIES.get("sessionid") is not None:
        print("sessionID was found! It is: "+request.COOKIES.get("sessionid"))
    else:
        print("There was so sessionID cookie!")
        
    return HttpResponse("Done, check CMD for feedback")

'''Creates a CartID cookie used by the Cart. '''
#http://localhost:8000/myCart/makeCartCookie
from user.models import CART
import datetime
def makeCartCookie(request):
    print("Creating cookie CartID...")    

    #Before we continue, if the user already had a CartID cookie
    #   then don't create a new one. Instead just leave their CartID
    #   cookie how it is.
    for key in request.session.keys():
        print(key+" :=> "+request.session.get(key))

    if request.session.get("sessionid"):
        print("There was a session key in request.session")
    else:
        print("There was no session key in request.session...")

    if request.session.get("CartID"):
        print("There was a CartID in request.session")
    else:
        print("There is no CartID in request.session")

    if 'CartID' in request.COOKIES:
        print("In request.COOKIES there is a CartID")
        print("The CarID is: " + request.COOKIES['CartID'])
    else:
        print("In request.COOKIES there is no CartID")

    if request.session.get("CartID") is None:
        print("No CartID cookie detected in client. Creating one now.")
                      
        #generate a random string 32 chars long
        val = CART.generate_Cart_ID()
        print("Value generated is: "+val)

        #set the cookie
        response = HttpResponse("")
        max_age=86400 #1 day
        expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
        response.set_cookie('CartID', val, max_age=86400, expires=expires)
                
        response.write("<h1>Cookie has been set</h1>")
        print("Cookie has been set.")

        return response
    else:
        print("The request already has a CartID cookie.")
        print("The value of the cookie is: "+request.session.get("CartID"))

        return HttpResponse("A cookie had already been set. It will not be changed.")
    
    def myCart2(request):

        
        





        
    



    