import random

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


	

from user.models import CART
def get_cart_items(request):
    
    return 