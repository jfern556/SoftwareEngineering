import sys, os, csv
project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from BookDetails.models import RESERVED_CREDIT_CARD, CREDIT_CARD, USER

count = 0
data = csv.reader(open("/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/sample_data/RESERVED_CREDIT_CARD.csv"),delimiter=",")

for row in data:

	if count == 1:
		print("Reading RESERVED_CREDIT_CARD model ...")

		rcc = RESERVED_CREDIT_CARD()

	
		rcc.RCC_ID=row[0]
		print("RCC_ID = " + rcc.RCC_ID)

		# Reading Credit Card ...
		ccList = CREDIT_CARD.objects.filter(C_card_number=row[1]) 
		if ccList:
			cc = ccList[0]

			if cc:
				rcc.C_card_number = cc;
		else:
			cc = CREDIT_CARD()
			cc.C_card_number = row[1]
			cc.save()
			rcc.C_card_number=cc
		print("C_card_number = " + rcc.C_card_number.C_card_number)





		# Reading Username ...
		uList = USER.objects.filter(Username=row[2]) 
		if uList:
			u = uList[0]

			if u:
				rcc.Username = u;
		else:
			u = USER()
			u.Username = row[1]
			u.save()
			rcc.Username = u
		print("Username= " + rcc.Username.Username)




		rcc.save()
		print("RESERVED_CREDIT_CARD read SUCCESSFUL")

	count = 1
