import sys, os, csv
project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from BookDetails.models import BOOK, SAVED_FOR_LATER_CONTENT, USER 

count = 0
data = csv.reader(open("/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/sample_data/SAVED_FOR_LATER_CONTENT.csv"),delimiter=",")

for row in data:

	if count == 1:
		print("Reading SAVED_FOR_LATER_CONTENT model ...")

		content = SAVED_FOR_LATER_CONTENT()

		content.Saved_ContentID = int(row[0])	
		print("Saved_ContentID = " + str(content.Saved_ContentID))
		
		# Reading Username ...
		uList = USER.objects.filter(Username=row[1]) 
		if uList:
			u = uList[0]

			if u:
				content.Username = u;
		else:
			u = USER()
			u.Username = row[1]
			u.save()
			content.Username = u
		print("Username= " + content.Username.Username)

	
		# Reading ISBN ...
		bList = BOOK.objects.filter(ISBN=row[2]) 
		if bList:
			b = bList[0]

			if b:
				content.ISBN = b;
		else:
			b = BOOK()
			b.ISBN = row[2]
			b.save()
			content.ISBN = b
		print("ISBN = " + content.ISBN.ISBN)

		content.save()
		print("SAVED_FOR_LATER_CONTENT read SUCCESSFUL")

	count = 1
