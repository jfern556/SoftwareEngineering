import sys, os, csv
project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from BookDetails.models import GENRE

count = 0
data = csv.reader(open("/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/sample_data/GENRE.csv"),delimiter=",")



for row in data:
	
	if count == 1:
		print("Reading GENRE model ...")
		genre = GENRE()
		
		genre.GenreID=row[0]
		print("GENRE ID = " + genre.GenreID)
		
		genre.Name=row[1]
		print("Name = " + genre.Name)
		
		genre.Description=row[2]	
		print("Description = " + genre.Description)
		
		genre.save()
		print("GENRE read SUCCESSFUL")

	
	count = 1;
