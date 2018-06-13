import sys, os, csv
project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from BookDetails.models import BOOK, CART, CART_CONTENT

count = 0
data = csv.reader(open("/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/sample_data/CART_CONTENT.csv"),delimiter=",")

for row in data:

	if count == 1:
		print("Reading CART_CONTENT model ...")

		cc = CART_CONTENT()

		cc.Cart_contentID=int(row[0])
		print("Cart_contentID = " + str(cc.Cart_contentID))

		# Reading ISBN ...
		bList = BOOK.objects.filter(ISBN=row[1]) 
		if bList:
			b = bList[0]

			if b:
				cc.ISBN = b;
		else:
			b = BOOK()
			b.ISBN = row[1]
			b.save()
			cc.ISBN = b
		print("ISBN = " + cc.ISBN.ISBN)

		# Reading Cart_ID ...
		cList = CART.objects.filter(Cart_ID=row[2]) 
		if cList:
			c = cList[0]

			if c:
				cc.Cart_ID = c;
		else:
			c = CART()
			c.Cart_ID = row[2]
			c.save()
			
		print("Cart_ID = " + cc.Cart_ID.Cart_ID)

		cc.Quantity = int(row[3])
		print("Quantity = " + str(cc.Quantity))
 
		cc.save()
		print("CART_CONTENT read SUCCESSFUL")

	count = 1
