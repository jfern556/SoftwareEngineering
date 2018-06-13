import sys, os, csv
project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from datetime import datetime
from BookDetails.models import BOOK, COMMENT, USER 

count = 0
data = csv.reader(open("/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/sample_data/COMMENT.csv"),delimiter=",")

for row in data:

	if count == 1:
		print("Reading COMMENT model ...")

		comment = COMMENT()

		comment.CommentID = int(row[0])	
		print("CommentID = " + str(comment.CommentID))
		
		# Reading ISBN ...
		bList = BOOK.objects.filter(ISBN=row[1]) 
		if bList:
			b = bList[0]

			if b:
				comment.ISBN = b;
		else:
			b = BOOK()
			b.ISBN = row[1]
			b.save()
			comment.ISBN = b
		print("ISBN = " + comment.ISBN.ISBN)
	
		# Reading Username ...
		uList = USER.objects.filter(Username=row[2]) 
		if uList:
			u = uList[0]

			if u:
				comment.Username = u;
		else:
			u = USER()
			u.Username = row[2]
			u.save()
			comment.Username = u
		print("Username= " + comment.Username.Username)

		# Ignoring datetime in CSV file
		comment.Time_posted = datetime.now()
		print("Time_posted" + str(comment.Time_posted))	

	#	comment.Comment_Text = row[4]
	#	print("Comment_Text" + comment.Comment_Text)	

	#	comment.UseNickname = row[5]
	#	print("UseNickname" + comment.UseNickname)	



		comment.save()
		print("COMMENT read SUCCESSFUL")

	count = 1
