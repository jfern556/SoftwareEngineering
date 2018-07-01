import sys, os, csv
project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from BookDetails.models import BOOK, AUTHOR, PUBLISHER_INFO, GENRE

count = 0
data = csv.reader(open("/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/sample_data/BOOK.csv"),delimiter=",")

for row in data:

	if count == 1:
		print("Reading BOOK model ...")

		book = BOOK()

	
		book.ISBN=row[0]
		print("ISBN = " + book.ISBN)

		# Reading Genre ...
		gList = GENRE.objects.filter(GenreID=row[1]) 
		if gList:
			g = gList[0]

			if g:
				book.GenreID = g;
		else:
			g = GENRE()
			g.GenreID = row[1]
			g.save()
			book.GenreID=g
		print("GenreID = " + book.GenreID.GenreID)

	
		# Reading Author...	
		aList = AUTHOR.objects.filter(AuthorID = row[2]) 
		if aList:
			a = aList[0]

			if a:
				book.AuthorID=a
		else:
			a = AUTHOR()
			a.AuthorID = row[2]
			a.save()
			book.AuthorID=a
		print("AuthorID = " + str(book.AuthorID.AuthorID))

		# Reading Publisher...	
		pList = PUBLISHER_INFO.objects.filter(PublisherID = row[3]) 
		if pList:	
			p = pList[0]		
	
			if p:
				book.PublisherID=p
		else:
			p = PUBLISHER_INFO()
			p.PublisherID = row[3]
			p.save()
			book.PublisherID=p
		print("PublisherID = " + str(book.PublisherID.PublisherID))

		# Will add images later...
		book.CoverImage=row[4]
		print("CoverImage = " + book.CoverImage.url)	

		# Gets initialized to 0
		book.Copies_sold = int(row[5])
		print("Copies_sold = " + str(book.Copies_sold))

		book.Book_description = row[6]
		print("Book_description = " + book.Book_description)

		book.Release_date = row[7]
		print("Release_date = " + book.Release_date)


		book.Price = float(row[8])
		print("Price = " + str(book.Price))

	
		# Need to add titles too...
		book.Book_title=row[9]
		print("Book_title = " + book.Book_title)

		book.save()

		print("BOOK read SUCCESSFUL")




	count = 1
