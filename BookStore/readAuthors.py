import sys, os, csv
project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from BookDetails.models import AUTHOR

count = 0
data = csv.reader(open("/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/sample_data/AUTHOR.csv"),delimiter=",")

for row in data:


	if count == 1:

		print("Reading AUTHOR model ...")
		
		author = AUTHOR()
		author.AuthorID= row[0]
		print("Author ID = " + author.AuthorID)
		
		author.Bio=row[1]
		print("Bio = " + author.Bio)
		
		author.Lname=row[2]
		print("Lname = " + author.Lname)
		
		author.Fname=row[3]
		print("Fname = " + author.Fname)
		
		author.save()
		print("AUTHOR read SUCCESSFUL")

	count = 1;
