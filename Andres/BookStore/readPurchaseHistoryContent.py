import sys, os, csv
project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from datetime import datetime
from BookDetails.models import BOOK, PURCHASE_HISTORY_CONTENT, USER 

count = 0
data = csv.reader(open("/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/sample_data/PURCHASE_HISTORY_CONTENT.csv"),delimiter=",")

for row in data:

	if count == 1:
		print("Reading PURCHASE_HISTORY_CONTENT model ...")

		phContent = PURCHASE_HISTORY_CONTENT()

		phContent.PHC_ID = int(row[0])	
		print("PHC_ID = " + str(phContent.PHC_ID))
		
		# Reading Username ...
		uList = USER.objects.filter(Username=row[1]) 
		if uList:
			u = uList[0]

			if u:
				phContent.Username = u;
		else:
			u = USER()
			u.Username = row[1]
			u.save()
			phContent.Username = u
		print("Username= " + phContent.Username.Username)


		# Reading ISBN ...
		bList = BOOK.objects.filter(ISBN=row[2]) 
		if bList:
			b = bList[0]

			if b:
				phContent.ISBN = b;
		else:
			b = BOOK()
			b.ISBN = row[2]
			b.save()
			phContent.ISBN = b
		print("ISBN = " + phContent.ISBN.ISBN)

		phContent.Quantity = int(row[3])
		print("Quantityi = " + str(phContent.Quantity))	
	
		phContent.Time = row[4]
		print("Time" + phContent.Time)	
	

		phContent.save()
		print("PURCHASE_HISTORY_CONTENT read SUCCESSFUL")

	count = 1
