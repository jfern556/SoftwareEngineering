from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from database.models import BOOK

# Create your views here.

def index(request):
	template = loader.get_template('BookDetails/book_details.html')
	
	#book_list = BOOK.objects.filter(ISBN="374601255-4")
	book_list = BOOK.objects.filter(ISBN="246916072-3")

	# Book to be displayed
	if book_list:
		book = book_list[0]

		#TEST
		print("Book_title: " + str(book.Title))
		print("CoverImage.url: " + book.CoverImage.url)
		print("Book Price: " + str(book.Price))
		print("Book description: " + book.Book_description)
		
		
	# else:
		# no book
		# Add No Book Found Entry to DB
		# set book to No book found

	context = { 'book': book, }
	
	return HttpResponse(template.render(context, request))

def working(request):
	template = loader.get_template('BookDetails/working.html')
	
	#book_list = BOOK.objects.filter(ISBN="374601255-4")
	book_list = BOOK.objects.filter(ISBN="246916072-3")

	# Book to be displayed
	if book_list:
		book = book_list[0]

		#TEST
		print("Book_title: " + str(book.Title))
		print("CoverImage.url: " + book.CoverImage.url)
		print("Book Price: " + str(book.Price))
		print("Book description: " + book.Book_description)
		
		
	# else:
		# no book
		# Add No Book Found Entry to DB
		# set book to No book found

	context = { 'book': book, }
	
	return HttpResponse(template.render(context, request))

def notworking(request):
	template = loader.get_template('BookDetails/notworking.html')
	
	#book_list = BOOK.objects.filter(ISBN="374601255-4")
	book_list = BOOK.objects.filter(ISBN="246916072-3")

	# Book to be displayed
	if book_list:
		book = book_list[0]

		#TEST
		print("Book_title: " + str(book.Title))
		print("CoverImage.url: " + book.CoverImage.url)
		print("Book Price: " + str(book.Price))
		print("Book description: " + book.Book_description)
		
		
	# else:
		# no book
		# Add No Book Found Entry to DB
		# set book to No book found

	context = { 'book': book, }
	
	return HttpResponse(template.render(context, request))
