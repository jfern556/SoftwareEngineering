import sys, os, csv
project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from BookDetails.models import ADDRESS

count = 0
data = csv.reader(open("/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/sample_data/ADDRESS.csv"),delimiter=",")



for row in data:
	
	if count == 1:
		print("Reading ADDRESS model ...")
		addr = ADDRESS()
		
		addr.Address_ID=int(row[0])
		print("Address_ID = " + str(addr.Address_ID))
		
		addr.Zip_Post=row[1]
		print("Zip_Post = " + addr.Zip_Post)
		
		addr.Address_1=row[2]	
		print("Address_1  = " + addr.Address_1)
		
		addr.Address_2=row[3]	
		print("Address_2  = " + addr.Address_2)

		addr.Country=row[4]	
		print("Country  = " + addr.Country)
	
		addr.State=row[5]	
		print("State  = " + addr.State)

		addr.City_Town=row[6]	
		print("City_Town  = " + addr.City_Town)

		addr.Name=row[7]	
		print("Name  = " + addr.Name)


		addr.save()
		print("ADDRESS read SUCCESSFUL")

	
	count = 1;
