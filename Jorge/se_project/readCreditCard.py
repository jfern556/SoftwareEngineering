import sys, os, csv
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'se_project.settings'
django.setup()
#project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
#sys.path.append(project_dir)

from user.models import *

count = 0
data = csv.reader(open("sample_data/CREDIT_CARD.csv"),delimiter=",")

for row in data:
	
	if count == 1:
		print("Reading CREDIT_CARD model ...")
		cc = CREDIT_CARD()
		
		cc.C_card_number=row[0]
		print("C_card_number = " + cc.C_card_number)
		
		cc.CVV=row[1]
		print("CVV = " + cc.CVV)
		
		cc.Exp_day=row[2]	
		print("Exp_day = " + cc.Exp_day)
		
		cc.Exp_month=row[3]	
		print("Exp_month = " + cc.Exp_month)
		
		cc.Exp_year=row[4]	
		print("Exp_year = " + cc.Exp_year)
		
		cc.Fname=row[5]	
		print("Fname = " + cc.Fname)
		
		cc.Lname=row[6]	
		print("Lname = " + cc.Lname)
		
		cc.Mname=row[7]	
		print("Mname = " + cc.Mname)
		
		cc.save()
		print("CREDIT_CARD read SUCCESSFUL")

	
	count = 1;
