from django.db import models
import random

class CART (models.Model):
	Cart_ID =  models.CharField(max_length=32, primary_key = True)	

	#Convenient method for generating a cart_ID
	@staticmethod
	def generate_Cart_ID():
		choice = '0123456789abcdefghijklmnopqrstuvwxyz'
		NUMBERS = 10
		LETTERS = 26
		SIZE = NUMBERS+LETTERS

		cartID = ''

		for i in range(0, SIZE):
			c = random.randint(0,SIZE-1)		
			cartID+=choice[c]
		
		return cartID
	
	
class ADDRESS (models.Model):
	Address_ID =  models.IntegerField(primary_key = True)
	Zip_Post =  models.CharField(max_length=16)
	Address_1 =  models.CharField(max_length=32)
	Address_2 =  models.CharField(max_length=32)
	Country =  models.CharField(max_length=32)
	State =  models.CharField(max_length=32)
	City_Town =  models.CharField(max_length=32)
	Name =  models.CharField(max_length=64)

class GENRE (models.Model):
	GenreID =  models.CharField(max_length=3, primary_key = True) # fixed 
	Name =  models.CharField(max_length=32)
	Description =  models.CharField(max_length=256)

class CREDIT_CARD (models.Model):
	C_card_number =  models.CharField(max_length=24, primary_key = True)
	CVV =  models.CharField(max_length=8)
	Exp_day =  models.CharField(max_length=2)  
	Exp_month =  models.CharField(max_length=2)  
	Exp_year =  models.CharField(max_length=4) # fixed
	Fname =  models.CharField(max_length=32)
	Lname =  models.CharField(max_length=32)
	Mname =  models.CharField(max_length=32)

class PUBLISHER_INFO (models.Model):
	PublisherID =  models.IntegerField(primary_key=True)
	Name =  models.CharField(max_length=50)

class AUTHOR (models.Model):
	AuthorID =  models.IntegerField(primary_key=True)
	Bio =  models.CharField(max_length=512)
	Lname =  models.CharField(max_length=20)
	Fname =  models.CharField(max_length=20)
	
class BOOK (models.Model):
	ISBN =  models.CharField(max_length=13, primary_key=True) # fixed
	GenreID =  models.ForeignKey(
		GENRE,
        on_delete=models.SET_NULL, # fixed
		null=True
	)
	AuthorID =  models.ForeignKey(
		AUTHOR,
		on_delete=models.SET_NULL,
		null=True
	)
	PublisherID =  models.ForeignKey(
		PUBLISHER_INFO,
		on_delete=models.SET_NULL,
		null=True
    )
	
	CoverImage =  models.ImageField(upload_to = 'book_images/', default = 'book_images/noImage.png') 
	Copies_sold =  models.IntegerField(default=0)
	Book_description =  models.CharField(max_length=1500, null=True)
	Release_date =  models.DateField(null=True)
	Price =  models.DecimalField(max_digits=(8),decimal_places=2, null=True)
	Title = models.CharField(max_length=128, null=True)


class CART_CONTENT (models.Model):
	Cart_contentID =  models.IntegerField(primary_key=True)
	ISBN =  models.ForeignKey(
            BOOK,
            on_delete=models.CASCADE,
			null=True
		) 
	Cart_ID =  models.ForeignKey(
            CART,
            on_delete=models.CASCADE,
			null=True
    )
	Quantity =  models.IntegerField()

class BOOK_RATING (models.Model):
	Book_rating_id =  models.IntegerField(primary_key=True)
	ISBN =  models.ForeignKey(
		BOOK,
		on_delete=models.SET_NULL,
		null=True		
	) 
	Five_star_count =  models.IntegerField()
	Four_star_count =  models.IntegerField()
	Three_star_count =  models.IntegerField()
	Two_star_count =  models.IntegerField()
	One_star_count =  models.IntegerField()
	Zero_star_count =  models.IntegerField()

class RATING_HISTORY (models.Model):
	RatingID =  models.BigIntegerField(primary_key=True)
	ISBN =  models.ForeignKey(
		BOOK,
		on_delete=models.SET_NULL,
		null=True
    ) #convert this to a fixed
	Username =  models.CharField(max_length=32)
	Rating =  models.IntegerField()

class PREFERRED_CREDIT_CARD (models.Model):
	PCC_ID =  models.IntegerField(primary_key=True)
	C_card_number =  models.ForeignKey(
		CREDIT_CARD,
		on_delete=models.CASCADE,
		null=True
    )

class USER_HOME_ADDRESS (models.Model):
	Home_address_ID =  models.IntegerField(primary_key=True)
	Address_ID =  models.ForeignKey(
		ADDRESS,
		on_delete=models.CASCADE,
		null=True
    )

class USER (models.Model):
	Username =  models.CharField(max_length=32,primary_key=True)
	Home_address_ID =  models.ForeignKey(
            USER_HOME_ADDRESS,
            on_delete=models.SET_NULL,
			null=True
    )
	Preferred_credit_card_ID =  models.ForeignKey(
		PREFERRED_CREDIT_CARD,
        on_delete=models.SET_NULL,
		null=True
    )
	Cart_ID =  models.ForeignKey(
		CART,
        on_delete=models.SET_NULL,
		null=True
    )
	Email  =  models.CharField(max_length=64)
	Password =  models.CharField(max_length=16)
	Lname =  models.CharField(max_length=32)
	Fname =  models.CharField(max_length=32)
	Nick_name =  models.CharField(max_length=32)
	
	
class SAVED_FOR_LATER_CONTENT (models.Model):
	Saved_ContentID =  models.IntegerField(primary_key=True)
	Username =  models.ForeignKey(
		USER,
        on_delete=models.CASCADE,
		null=True
	)
	ISBN =  models.ForeignKey(
		BOOK,
        on_delete=models.CASCADE,
		null=True
	) # fixed

class USER_SHIPPING_ADDRESS (models.Model):
	Shipping_address_ID =  models.IntegerField(primary_key=True)
	Address_ID =  models.ForeignKey(
		ADDRESS,
        on_delete=models.CASCADE,
		null=True
	)
	Username =  models.ForeignKey(
		USER,
        on_delete=models.CASCADE,
		null=True
	)
	

class RESERVED_CREDIT_CARD (models.Model):
    RCC_ID =  models.CharField(max_length=24, primary_key=True)
    C_card_number =  models.ForeignKey(
		CREDIT_CARD,
        on_delete=models.CASCADE,
		null=True
	)
    Username =  models.ForeignKey(
		USER,
        on_delete=models.CASCADE
	)

class COMMENT (models.Model):
	CommentID =  models.IntegerField(primary_key=True)
	ISBN =  models.ForeignKey(
		BOOK,
		on_delete=models.CASCADE
	) 
	Username =  models.ForeignKey(
		USER,
        on_delete=models.CASCADE
	)	
	Time_posted = models.DateTimeField()
	Comment_Text =  models.CharField(max_length=500)
	UseNickname =  models.NullBooleanField(null=True)

class PURCHASE_HISTORY_CONTENT (models.Model):
	PHC_ID =  models.IntegerField(primary_key=True)
	Username =  models.ForeignKey(
		USER,
        on_delete=models.CASCADE,
		null=True
	)
	ISBN =  models.ForeignKey(
		BOOK,
        on_delete=models.SET_NULL,
		null=True
	) 
	Quantity =  models.IntegerField()
	Time =  models.DateTimeField()
	


