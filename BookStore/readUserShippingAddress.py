import sys, os, csv
project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from BookDetails.models import USER_SHIPPING_ADDRESS, ADDRESS, USER

count = 0
data = csv.reader(open("/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/sample_data/USER_SHIPPING_ADDRESS.csv"),delimiter=",")

for row in data:

	if count == 1:
		print("Reading USER_SHIPPING_ADDRESS model ...")

		usrShipAddr = USER_SHIPPING_ADDRESS()

	
		usrShipAddr.Shipping_address_ID=int(row[0])
		print("Shipping_address_ID = " + str(usrShipAddr.Shipping_address_ID))

		# Reading Address ...
		addrList = ADDRESS.objects.filter(Address_ID=row[1]) 
		if addrList:
			addr = addrList[0]

		if addr:
			usrShipAddr.Address_ID = addr;
		else:
			addr = ADDRESS()
			addr.Address_ID = int(row[1])
			addr.save()
			usrShipAddr.Address_ID=addr
		print("Address_ID = " + str(usrShipAddr.Address_ID.Address_ID))


		# Reading Username ...
		uList = USER.objects.filter(Username=row[2]) 
		if uList:
			u = uList[0]

			if u:
				usrShipAddr.Username = u;
		else:
			u = USER()
			u.Username = row[2]
			u.save()
			usrShipAddr.Username = u
		print("Username= " + usrShipAddr.Username.Username)




		usrShipAddr.save()
		print("USER_SHIPPING_ADDRESS read SUCCESSFUL")

	count = 1
