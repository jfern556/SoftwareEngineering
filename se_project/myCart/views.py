from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader#bucky video

#from .models import myCart

from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from user.models import CART
from user.models import CART_CONTENT


#def shortcut(response):
    
#    response.delete_cookie('CartID')
    
#    return response

#def errorpage(request):
#    return render(request, 'errorpage', {})
from django.contrib.sessions.models import Session

from user.models import CART, CART_CONTENT
from . import utility
#Let's person view cart. Uses session instead of login.
def index(request):
    #eturn run_this_instead_1()

    print("View [index] was called.")
    SESSION_COOKIE_NAME = 'sessionid'        
    CART_COOKIE_NAME = 'CartID'
    cart_cookie_value = ''        

    #ignore this
    print("Calling: request.session.session_key")
    print(request.session.session_key)
    print("Calling: request.session.__contains__(SESSION_NAME)")
    print(request.session.__contains__(SESSION_COOKIE_NAME)) #why return false?    
    
    print("Calling: request.session")
    print(request.session)
       

    
    #Check if the session contains a CART_COOKIE_NAME cookie
    if CART_COOKIE_NAME in request.session:                
        print(CART_COOKIE_NAME + " is a valid cookie name for this session.")
        cart_cookie_value = request.session[CART_COOKIE_NAME]
        print("cart_cokie_value is: " + str(cart_cookie_value))

        #return HttpResponse("A Session was found info:<br>Session_name: %s<br>Session_value%s:"%(SESSION_NAME, str(session_value)))        

        print("call Z1")
        cart = CART.objects.all().get(Cart_ID = cart_cookie_value)
        print(cart)
        
        print("Creating cart_content_list")
        cart_content_list = cart.cart_content_set.all()

        print("Printing: CART_CONTENT.objects.filer(Cart_ID = cart_cookie_value)")
        print(CART_CONTENT.objects.filter(Cart_ID = cart_cookie_value))
        
        context = {
            'cart_content_list': cart_content_list,
            'Cart_ID': cart_cookie_value,                 
            'subtotal': utility.subtotal(cart),
            'form': forms.QuantityChangeForm(), #used to change quantity of an item
        }

        print("subtotal is: " + str(utility.subtotal(cart)))
        

        #return HttpResponse("This session had a cookie for "+CART_COOKIE_NAME+".<br>"+
        #"the value of that cookie is: " + cart_cookie_value)

        #response = response.session.__setitem__("sessionIDDDD", "wakka wakka")        
        
        return render(request, 'myCart/myCart.html', context = context)
    else:
        print("The " + CART_COOKIE_NAME +" was NOT found.")
        print("Creating a " + CART_COOKIE_NAME + " cookie...")
        
        #print("jk lawl tricked")
        utility.create_cart_id_value(request)           
        print("Done creating cookie.")

        #return HttpResponse("CHECK CMD")
        #Take the visitor back to this same page. They should have a sessionid and cookie now
        #if user has cookies disabled, this could be infinite loop
        return HttpResponseRedirect(reverse('index', args=None))

    return HttpResponse("Check CMD")


from . import forms
from . import utility
from django.http import Http404
def cart_quantity_change(request):
    print("Called [cart_quantity_change2] view")    
    
    if request.method == "POST":
        form = forms.QuantityChangeForm(request.POST)

        print("checking if valid:")

        print(request.POST)

        if form.is_valid():
            print("form is valid")
            print("Printing form: " + str(form))            
            cart_content_id = form.cleaned_data['Cart_contentID']
            new_quantity = form.cleaned_data['New_quantity']
            utility.change_cart_quantity(cart_content_id=cart_content_id, new_quantity=new_quantity) #use object or 404
            return HttpResponseRedirect(reverse('index', args=None))
        else:
            print("form is invalid")
            return Http404("Invalid form!")
    else:
        return Http404("Expected POST: request is not POST")

    return HttpResponse("Uhh read CMD")
    

#test
def run_this_instead_1():
    sess = Session.objects.get(pk='mql7dqw7pz26yobweyec343q306xm0gg')    
    print("Undecoded: " + sess.session_data)
    print("Decoded: " + str(sess.get_decoded()))

    print("-------------------------")
    sess = Session.objects.get(pk='486wo45e0h5tinb6as9pqr4juwgrcu9h')    
    print("Coded: " + sess.session_data)
    print("Decoded: " + str(sess.get_decoded()))
    
    return HttpResponse("Read CMD")
    
    
#test    
def indexOLD(request): 
    #response = HttpResponseRedirect(reverse('index', args=None))
    #shortcut(response)
    
    
    print("View [index] was called.")
    COOKIE_NAME = 'CartID'
    context = {}
    Cart_ID = ''

    #problems: if user has cookies disabled, might be infinite loop
    if COOKIE_NAME in request.COOKIES:
        print(COOKIE_NAME + " is a cookie in the request")
        print("The value of "+COOKIE_NAME+" is: "+request.COOKIES[COOKIE_NAME])
        
        cookieValue = request.COOKIES[COOKIE_NAME]        

        #Search every cart until we find a match
        for cart in CART.objects.all():
            if cart.Cart_ID == cookieValue: #We've found a match
                print("The cookie's value matches a Cart_ID value of a CART object")                
                #Success! Load the page!
                print("TEST:"+str(cart.Cart_ID)+" length = "+str(len(cart.Cart_ID)))

                cart_content_list = cart.cart_content_set.all()
                print("cart_content_list contains: "+ str(cart_content_list))

                context["cart_content_list"] = cart_content_list
                context["Cart_ID"] = cart.Cart_ID

                
                
                

                #create the context later
                print("Context is: "+str(context))        
                return render(request, 'myCart/myCart.html', context=context)
        
        #No match was found in the database
        #   Do: 1)Create cookie  2)Store Data in CART DB table  3)Set the cookie on the response
        print("The cookie value DOES NOT match any Cart_ID value in the CART table")

        
        
        #response = HttpResponseRedirect(reverse('errorpage', args=None))
        #response.delete_cookie('CartID')
        #do nothing for now
        return HttpResponse("ERROR")
                
    else:
        ''' there was no CartID associated with the session, make one, \
            update the DB and then reload the page'''
        
        #This response's cookie will be set below
        response = HttpResponseRedirect(reverse('index', args=None))
        
        print("CartID is not a cookie in the request. Making a cookie now.")
        
        
        
        #max_age = 86400 #Remove this CartID after it has been the the DB for 7 days
        
        #generate a cookie value
        cookie_value = CART.generate_Cart_ID()
        print("Generated a cookie, the value is: "+cookie_value+" setting the key/value pair now.")
        response.set_cookie("CartID", cookie_value)         
        print("Done setting cookie")
        print("Done creating cookie, redirecting user now.")

        print("Creating a cart")
        c = CART()
        value = c.generate_Cart_ID() #generater random string of len 32 via static function
        c.Cart_ID = value
        c.save()
        print("Done creating a cart.")
        
        #test - for not just set it to sometthing that has a lot of items
        
        response.set_cookie('CartID','xGwiiFrlmh4cl8DW7MBH5Cm8XmU0i2n0')

        print("Reloading page.")
        #reload the page now that the cookie has been set
        return response 



def cartItemInfo(Cart_ContentID):
    return ""
        

#test
# Description: 
#   Utility function.
#   Assigns the request a CartID cookie with a randomly generated string as its value.
#       the generated string is 32 chars long.
#   When it is done, it redirects the user back to a page.
# Input: 
#   request-HttpRequest who's cookie will be set
#   cookie_value-The value that you want the CartID cookie to be set to
# Output:
#
def createCookieAndCart(request, cookie_value=""):    
    print("Setting a cookie for the user. Adding ")
    cookie_value=CART.generate_Cart_ID()
    c = CART()
    value = cookie_value
    c.Cart_ID = value
    c.save()
    request.set_cookie("CartID", cookie_value)
    return ""#test
    
    
    

# Create your views here.

def myCart(request):    
    print("View [myCart] was called.")
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

#TEST INDEXS BELOW --------------------------------------------------------------------

def indexTest(request):
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



from django.contrib.auth import authenticate, login    
def login_page_info(request):
    
    print("Got here")   
    username = request.POST['user']    
    password = request.POST['pwd']

    user = authenticate(request, username=username, password=password)

    if user is None:
        print("Invalid user info")
        return HttpResponse("Invalid user info")
    else:
        print("That was a valid user")
        return HttpResponse("Invalid user info")

def homepage(request):
    return render(request, 'myCart/homepage.html', {})
