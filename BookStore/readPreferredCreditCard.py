import sys, os, csv
project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from BookDetails.models import PREFERRED_CREDIT_CARD, CREDIT_CARD

count = 0
data = csv.reader(open("/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/sample_data/PREFERRED_CREDIT_CARD.csv"),delimiter=",")

for row in data:

	if count == 1:
		print("Reading PREFERRED_CREDIT_CARD model ...")

		pcc = PREFERRED_CREDIT_CARD()

	
		pcc.PCC_ID=int(row[0])
		print("PCC_ID = " + str(pcc.PCC_ID))

		# Reading Credit Card ...
		ccList = CREDIT_CARD.objects.filter(C_card_number=row[1]) 
		if ccList:
			cc = ccList[0]

			if cc:
				pcc.C_card_number = cc;
		else:
			cc = CREDIT_CARD()
			cc.C_card_number = row[1]
			cc.save()
			pcc.C_card_number=cc
		print("C_card_number = " + pcc.C_card_number.C_card_number)

		pcc.save()
		print("PREFERRED_CREDIT_CARD read SUCCESSFUL")

	count = 1
