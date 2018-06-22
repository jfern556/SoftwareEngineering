from django.db import models

# Create your models here.
from django.db import models


# PARSE OUPUT START
class CART(models.Model):
    Cart_ID = models.CharField(max_length=32, primary_key=True)



#	  PRIMARY KEY (`Cart_ID`)

class ADDRESS(models.Model):
    Address_ID = models.IntegerField(primary_key=True)
    Zip_Post = models.CharField(max_length=16)
    Address_1 = models.CharField(max_length=32)
    Address_2 = models.CharField(max_length=32)
    Country = models.CharField(max_length=32)
    State = models.CharField(max_length=32)
    City_Town = models.CharField(max_length=32)
    Name = models.CharField(max_length=64)

#	  PRIMARY KEY (`Address_ID`)

class CREDIT_CARD(models.Model):
    C_card_number = models.CharField(max_length=24, primary_key=True)
    CVV = models.CharField(max_length=8)
    Exp_day = models.CharField(max_length=16)  # fixed
    Exp_month = models.CharField(max_length=16)  # fixed
    Exp_year = models.CharField(max_length=4)  # fixed
    Fname = models.CharField(max_length=32)
    Lname = models.CharField(max_length=32)
    Mname = models.CharField(max_length=32)

#	  PRIMARY KEY (`C_card_number`)


class USER_HOME_ADDRESS(models.Model):
    Home_address_ID = models.IntegerField(primary_key=True)
    Address_ID = models.ForeignKey(
        ADDRESS,
        on_delete=models.CASCADE,
        null=True
    )


#	  PRIMARY KEY (`Home_address_ID`)
#	  KEY `FK` (`Address_ID`)

class PREFERRED_CREDIT_CARD(models.Model):
    PCC_ID = models.IntegerField(primary_key=True)
    C_card_number = models.ForeignKey(
        CREDIT_CARD,
        on_delete=models.CASCADE,
        null=True
    )


#	  PRIMARY KEY (`PCC_ID`)
#	  KEY `FK` (`C_card_number`)


class USER(models.Model):
    Username = models.CharField(max_length=32, primary_key=True)
    Home_address_ID = models.ForeignKey(
        USER_HOME_ADDRESS,
        on_delete=models.SET_NULL,
        null=True
    )
    Preferred_credit_card_ID = models.ForeignKey(
        PREFERRED_CREDIT_CARD,
        on_delete=models.SET_NULL,
        null=True
    )
    Cart_ID = models.ForeignKey(
        CART,
        on_delete=models.SET_NULL,
        null=True
    )
    Email = models.CharField(max_length=64)
    Password = models.CharField(max_length=16)
    Lname = models.CharField(max_length=32)
    Fname = models.CharField(max_length=32)
    Nick_name = models.CharField(max_length=32)


#	  PRIMARY KEY (`Username`)
#	  KEY `FK1` (`Home_address_ID`)
#	  KEY `FK2` (`Preferred_credit_card_ID`)
#	  KEY `FK3` (`Cart_ID`)



class GENRE(models.Model):
    GenreID = models.CharField(max_length=3, primary_key=True)  # fixed
    # GenreID =  models.CharField(max_length=3) # fixed
    Name = models.CharField(max_length=32)
    Description = models.CharField(max_length=256)


#	  PRIMARY KEY (`GenreID`)


class PUBLISHER_INFO(models.Model):
    PublisherID = models.IntegerField(primary_key=True)
    # PublisherID =  models.IntegerField()
    Name = models.CharField(max_length=50)


#	  PRIMARY KEY (`PublisherID`)

class AUTHOR(models.Model):
    AuthorID = models.IntegerField(primary_key=True)
    # AuthorID =  models.IntegerField()
    Bio = models.CharField(max_length=512)
    Lname = models.CharField(max_length=20)
    Fname = models.CharField(max_length=20)


#	  PRIMARY KEY (`AuthorID`)

class BOOK(models.Model):
    ISBN = models.CharField(max_length=13, primary_key=True)  # fixed
    # ISBN =  models.CharField(max_length=13) # fixed
    GenreID = models.ForeignKey(
        GENRE,
        on_delete=models.SET_NULL,  # fixed
        null=True
    )
    AuthorID = models.ForeignKey(
        AUTHOR,
        on_delete=models.SET_NULL,
        null=True
    )
    PublisherID = models.ForeignKey(
        PUBLISHER_INFO,
        on_delete=models.SET_NULL,
        null=True
    )
    CoverImage = models.IntegerField()  # THIS HAS TO BE A BLOB TYPE
    Copies_sold = models.IntegerField()
    Book_description = models.CharField(max_length=1500)
    Release_date = models.DateField()
    Price = models.DecimalField(max_digits=(8), decimal_places=2)


#	  PRIMARY KEY (`ISBN`)
#	  KEY `FK1` (`GenreID`)
#	  KEY `FK2` (`AuthorID`)
#	  KEY `FK3` (`PublisherID`)


class CART_CONTENT(models.Model):
    Cart_contentID = models.IntegerField(primary_key=True)
    ISBN = models.ForeignKey(
        BOOK,
        on_delete=models.CASCADE,
        null=True
    )  # fixed
    Cart_ID = models.ForeignKey(
        CART,
        on_delete=models.CASCADE,
        null=True
    )
    Quantity = models.IntegerField()


#	  PRIMARY KEY (`Cart_contentID`)
#	  KEY `FK1` (`ISBN`)
#	  KEY `FK2` (`Cart_ID`)

class BOOK_RATING(models.Model):
    BOOK_RATING_ID = models.BigIntegerField(primary_key=True)  # BIG INT!
    ISBN = models.ForeignKey(
        BOOK,
        on_delete=models.SET_NULL,
        null=True
    )  # fixed
    Five_star_count = models.IntegerField()
    Four_star_count = models.IntegerField()
    Three_star_count = models.IntegerField()
    Two_star_count = models.IntegerField()
    One_star_count = models.IntegerField()
    Zero_star_count = models.IntegerField()


#	  PRIMARY KEY (`BOOK_RATING_ID`)
#	  KEY `FK` (`ISBN`)

class RATING_HISTORY(models.Model):
    RatingID = models.BigIntegerField(primary_key=True)
    ISBN = models.ForeignKey(
        BOOK,
        on_delete=models.SET_NULL,
        null=True
    )  # convert this to a fixed
    Username = models.CharField(max_length=32)
    Rating = models.IntegerField()


#	  PRIMARY KEY (`RatingID`)
#	  KEY `FK` (`ISBN` `Username`)


class SAVED_FOR_LATER_CONTENT(models.Model):
    Saved_ContentID = models.IntegerField(primary_key=True)
    Username = models.ForeignKey(
        USER,
        on_delete=models.CASCADE,
        null=True
    )
    ISBN = models.ForeignKey(
        BOOK,
        on_delete=models.CASCADE,
        null=True
    )  # fixed


#	  PRIMARY KEY (`Saved_ContentID`)
#	  KEY `FK1` (`Username`)
#	  KEY `FK2` (`ISBN`)

class USER_SHIPPING_ADDRESS(models.Model):
    Shipping_address_ID = models.IntegerField(primary_key=True)
    Address_ID = models.ForeignKey(
        ADDRESS,
        on_delete=models.CASCADE,
        null=True
    )
    Username = models.ForeignKey(
        USER,
        on_delete=models.CASCADE,
        null=True
    )


#	  PRIMARY KEY (`Shipping_address_ID`)
#	  KEY `FK1` (`Address_ID`)
#	  KEY `FK2` (`Username`)


class RESERVED_CREDIT_CARD(models.Model):
    RCC_ID = models.CharField(max_length=24, primary_key=True)
    C_card_number = models.ForeignKey(
        CREDIT_CARD,
        on_delete=models.CASCADE,
        null=True
    )
    Username = models.ForeignKey(
        USER,
        on_delete=models.CASCADE
    )


#	  PRIMARY KEY (`RCC_ID`)
#	  KEY `FK1` (`C_card_number`)
#	  KEY `FK2` (`Username`)

class COMMENT(models.Model):
    CommentID = models.IntegerField(primary_key=True)
    ISBN = models.ForeignKey(
        BOOK,
        on_delete=models.CASCADE
    )  # fixed
    Username = models.ForeignKey(
        USER,
        on_delete=models.CASCADE
    )
    Time_posted = models.DateTimeField()
    Comment_Text = models.CharField(max_length=500)
    UseNickname = models.BooleanField()


#	  PRIMARY KEY (`CommentID`)
#	  KEY `FK1` (`ISBN`)
#	  KEY `FK2` (`Username`)

class PURCHASE_HISTORY_CONTENT(models.Model):
    PHC_ID = models.IntegerField(primary_key=True)
    Username = models.ForeignKey(
        USER,
        on_delete=models.CASCADE,
        null=True
    )
    ISBN = models.ForeignKey(
        BOOK,
        on_delete=models.SET_NULL,
        null=True
    )  # fixed
    Quantity = models.IntegerField()
    Time = models.DateField()


#	  PRIMARY KEY (`PHC_ID`)
#	  KEY `FK1` (`Username`)
#	  KEY `FK2` (`ISBN`)


# PARSE OUTPUT END


# test
#class MyDateField(models.Field):
 #   def db_type(self, connection):
 #       if connection.setting_dict['ENGINE'] == 'django.db.backends.mysql':
 #           return 'datetime'
#        else:
 #           return 'timestamp'


# test
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


# test
# class DateField(models.Field):
#    def db_type(self, connection):
#        if connection.setting_dict['ENGINE'] == 'django.db.backends.mysql':
#            return 'datetime'
#        else:
#            return 'timestamp'

