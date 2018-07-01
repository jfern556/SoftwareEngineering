import sys, os, csv
project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from BookDetails.models import BOOK, RATING_HISTORY, USER 

count = 0
data = csv.reader(open("/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/sample_data/RATING_HISTORY.csv"),delimiter=",")

for row in data:

	if count == 1:
		print("Reading RATING_HISTORY model ...")

		br = RATING_HISTORY()

		br.RatingID = int(row[0])	
		print("Book_Rating_ID = " + str(br.RatingID))
		
		# Reading ISBN ...
		bList = BOOK.objects.filter(ISBN=row[1]) 
		if bList:
			b = bList[0]

			if b:
				br.ISBN = b;
		else:
			b = BOOK()
			b.ISBN = row[1]
			b.save()
			br.ISBN = b
		print("ISBN = " + br.ISBN.ISBN)
	
		# Reading Username ...
		uList = USER.objects.filter(Username=row[2]) 
		if uList:
			u = uList[0]

			if u:
				br.Username = u;
		else:
			u = USER()
			u.Username = row[2]
			u.save()
			br.Username = u
		print("Username= " + br.Username.Username)

		br.Rating = int(row[3])
		print("br.Rating = " + str(br.Rating))

		br.save()
		print("RATING_HISTORY read SUCCESSFUL")

	count = 1
