import sys, os, csv
project_dir = "/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/BookStore/"
sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from BookDetails.models import USER, USER_HOME_ADDRESS, PREFERRED_CREDIT_CARD, CART

count = 0
data = csv.reader(open("/home/HOMEGROUP/adelg000/school/CEN4010/BookStore/sample_data/USER.csv"),delimiter=",")

for row in data:

	if count == 1:
		print("Reading USER model ...")

		user = USER()

	
		user.Username=row[0]
		print("Username = " + user.Username)

		# Reading User Home Address...
		usrHomeAddrList = USER_HOME_ADDRESS.objects.filter(Address_ID=row[1]) 
		if usrHomeAddrList:
			usrHomeAddr = usrHomeAddrList[0]

			if usrHomeAddr:
				user.Home_address_ID = usrHomeAddr;
		else:
			usrHomeAddr = USER_HOME_ADDRESS()
			usrHomeAddr.Address_ID = int(row[1])
			usrHomeAddr.save()
			user.Home_address_ID=usrHomeAddr
		print("Home_address_ID = " + str(user.Home_address_ID.Address_ID))

		# Reading Preferred Credit Card...
		pccList = PREFERRED_CREDIT_CARD.objects.filter(PCC_ID=row[1]) 
		if pccList:
			pcc = pccList[0]

			if pcc:
				user.Preferred_credit_card_ID = pcc;
		else:
			pcc = PREFERRED_CREDIT_CARD()
			pcc.PCC_ID = int(row[1])
			pcc.save()
			user.Preferred_credit_card_ID=pcc
		print("Preferred_credit_card_ID = " + str(user.Preferred_credit_card_ID.PCC_ID))


		# Reading Cart...
		cartList = CART.objects.filter(Cart_ID=row[1]) 
		if cartList:
			cart = cartList[0]

			if cart:
				user.Cart_ID = cart;
		else:
			cart = CART()
			cart.Cart_ID = row[1]
			cart.save()
			user.Cart_ID=cart
		print("Cart_ID = " + str(user.Cart_ID.Cart_ID))


		user.save()
		print("USER read SUCCESSFUL")

	count = 1
