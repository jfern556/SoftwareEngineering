import sys, os, csv
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'se_project.settings'
django.setup()
#project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
#sys.path.append(project_dir)

from user.models import *

count = 0
data = csv.reader(open("sample_data/PREFERRED_CREDIT_CARD.csv"),delimiter=",")

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
