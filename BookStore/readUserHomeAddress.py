import sys, os, csv
project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from BookDetails.models import USER_HOME_ADDRESS, ADDRESS

count = 0
data = csv.reader(open("/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/sample_data/USER_HOME_ADDRESS.csv"),delimiter=",")

for row in data:

	if count == 1:
		print("Reading USER_HOME_ADDRESS model ...")

		usrHomeAddr = USER_HOME_ADDRESS()

	
		usrHomeAddr.Home_address_ID=int(row[0])
		print("Home_address_ID = " + str(usrHomeAddr.Home_address_ID))

		# Reading Credit Card ...
		addrList = ADDRESS.objects.filter(Address_ID=row[1]) 
		if addrList:
			addr = addrList[0]

		if addr:
			usrHomeAddr.Address_ID = addr;
		else:
			addr = ADDRESS()
			addr.Address_ID = int(row[1])
			addr.save()
			usrHomeAddr.Address_ID=addr
		print("Address_ID = " + str(usrHomeAddr.Address_ID.Address_ID))

		usrHomeAddr.save()
		print("USER_HOME_ADDRESS read SUCCESSFUL")

	count = 1
