import sys, os, csv
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'se_project.settings'
django.setup()
#project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
#sys.path.append(project_dir)

from user.models import *

count = 0
data = csv.reader(open("sample_data/CART.csv"),delimiter=",")
for row in data:	
	if count == 1:
		print("Reading CART model ...")
		cart = CART()
		
		cart.Cart_ID=row[0]
		print("Cart_ID = " + cart.Cart_ID)
		
		cart.save()
		print("CART read SUCCESSFUL")

	
	count = 1;
