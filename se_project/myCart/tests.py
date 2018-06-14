from django.test import TestCase

# Create your tests here.
class MyCartModelAppTests(TestCase):
    def test_juan(self):
        self.assertIs(True,True)

from user.models import CART, CART_CONTENT
from .. import (readAuthors, readBookRatings, readBooks, readCart,
readCartContent, readCreditCard, readGenres, readPreferredCreditCard,
readPublishers, readUser, readUserHomeaddress)

import time
class MyMiscTests(TestCase):    
    
    def test_select_related_function(self):
        
        print("Start: " +time.now())
        print("Start: " +time.now())
        
        
        
        
        #This cart_id actually exists in the CART table,
        # additionally, ther CART_CONTENT table has
        # tuples with the same data as cart_id        
        cart_id = "xGwiiFrlmh4cl8DW7MBH5Cm8XmU0i2n0"
        
        c = CART.objects.all()
        print(c)
        c = CART.objects.all().filter(Cart_ID="xGwiiFrlmh4cl8DW7MBH5Cm8XmU0i2n0")

        c = CART.objects.all()
        print(c)
        if c is None:
            print("c is None")
            print(c)
        else:
            print("c is NOT None")
            print(c)
        cart_JOIN_cartContent = CART_CONTENT.objects.select_related()

        isNone = None

        if cart_JOIN_cartContent is None:
            print("It is None :(")
            #print(cart_JOIN_cartContent.get(Quantity=2))
            isNone = True
        else:
            print("It is something... Let's print it out.")
            j = cart_JOIN_cartContent[0].Cart_ID
            print(j)
            print("Done printing")
            isNone = False

        self.assertIs(isNone, False)
        
        
        
