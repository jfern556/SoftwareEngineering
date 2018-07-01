import sys, os, csv
#project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
#sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'se_project.settings'

import django

django.setup()

from user.models import PUBLISHER_INFO

count = 0
data = csv.reader(open("sample_data/PUBLISHER_INFO.csv"),delimiter=",")
for row in data:
	
	if count == 1:

		print("Reading PUBLISHER_INFO model ...")
		pubInfo = PUBLISHER_INFO()
	

		pubInfo.PublisherID=int(row[0])
		print("Publisher ID = " + str(pubInfo.PublisherID))

		pubInfo.Name=row[1]
		print("Name = " + pubInfo.Name)
	
		pubInfo.save()
		print("PUBLISHER_INFO read SUCCESSFUL")

	count = 1;

