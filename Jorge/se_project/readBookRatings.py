import sys, os, csv
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'se_project.settings'
django.setup()
#project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
#sys.path.append(project_dir)

from user.models import *

count = 0
data = csv.reader(open("sample_data/BOOK_RATING.csv"),delimiter=",")

for row in data:

	if count == 1:
		print("Reading BOOK_RATING model ...")

		br = BOOK_RATING()

		br.BOOK_RATING_ID = int(row[0])	
		print("Book_Rating_ID = " + str(br.BOOK_RATING_ID))
		
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

		br.Five_star_count = int(row[2])	
		print("br.Five_star_count = " + str(br.Five_star_count))

		br.Four_star_count = int(row[3])	
		print("br.Four_star_count = " + str(br.Four_star_count))

		br.Three_star_count = int(row[4])	
		print("br.Three_star_count = " + str(br.Three_star_count))

		br.Two_star_count = int(row[5])	
		print("br.Two_star_count = " + str(br.Two_star_count))

		br.One_star_count = int(row[6])	
		print("br.One_star_count = " + str(br.One_star_count))

		br.Zero_star_count = int(row[7])	
		print("br.Zero_star_count = " + str(br.Zero_star_count))


		br.save()
		print("BOOK_RATING read SUCCESSFUL")

	count = 1
