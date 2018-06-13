import sys, os, csv
project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from BookDetails.models import CART

count = 0
data = csv.reader(open("/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/sample_data/CART.csv"),delimiter=",")



for row in data:
	
	if count == 1:
		print("Reading CART model ...")
		cart = CART()
		
		cart.Cart_ID=row[0]
		print("Cart_ID = " + cart.Cart_ID)
		
		cart.save()
		print("CART read SUCCESSFUL")

	
	count = 1;
