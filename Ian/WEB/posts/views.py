from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Books

# Create your views here.
def index(request):
   # return HttpResponse('HELLO FROM POSTS')

    book_dict = {'record': Books.objects.first().image}
    return render(request, 'posts/browse.html', context=book_dict)
