import random


def generate_Cart_ID():
    choice = '0123456789abcdefghijklmnopqrstuvwxyz'
    NUMBERS = 10
    LETTERS = 26
    SIZE = NUMBERS+LETTERS

    cartID = ''

    for i in range(0, SIZE):
        c = random.randint(0, SIZE-1)
        cartID += choice[c]

    return cartID


from user.models import CART


def create_cart_id_value(request):
	print("generating cart_value...")
	cart_value = generate_Cart_ID()
	print("Done, cart_value is: "+cart_value)

	#while cart_value in CART.objects.get(CartId=cart_value):
	#	cart_value = generate_Cart_ID()

	print("Generated value was unique, great!")

	request.session['CartID'] = cart_value

	#add cart_value to the CART database
	c = CART(Cart_ID=cart_value)
	c.save()


	return cart_value


from user.models import CART


def get_cart_items(request):

    return
