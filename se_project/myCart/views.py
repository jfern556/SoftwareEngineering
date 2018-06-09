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

def index2(request):
    return HttpResponse("HELLO WORLD!")

#test

def consoleSessionDisplay(request):    
    for key, value in request.session.items():         
        print('{} => {}'.format(key, value))
    return HttpResponse("Check command promt for session information!")

def makeCookieTest(request):
    return ""

def makeCookieWorkedTest(request):
    ""

def myCart(request):    
    return render(request, 'myCart/myCartSimple.html')

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