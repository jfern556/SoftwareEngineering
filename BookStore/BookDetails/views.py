from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from BookDetails.models import BOOK

# Create your views here.

def index(request):
	template = loader.get_template('BookDetails/book_details.html')
	
	book_list = BOOK.objects.filter(ISBN="9780261103283")
	# Book to be displayed
	if book_list:
		book = book_list[0]
	# else:
		# no book
		# Add No Book Found Entry to DB
		# set book to No book found
			

	context = { 'book': book, }
	
	return HttpResponse(template.render( context, request))

