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


from user.models import CART_CONTENT
def change_cart_quantity(cart_content_id,new_quantity):
	print("Called [change_cart_quantity] method. ")	
	
	print("Getting cart content object")
	cc = CART_CONTENT.objects.get(Cart_contentID = cart_content_id)
	
	print("cc is: " + str(cc))

	print("current quantity is: " + str(cc.Quantity))

	print("Changing quantity")
	cc.Quantity = new_quantity

	print("New Quantity: " + str(cc.Quantity))
	
	print("Saving instance of cart_content")
	cc.save()

	return None


from user.models import CART

#Calculate subtotal price of the items in a CART objects
#input:
#	CART: CART object
#output:
#	sum: sum of the total cost, factoring in quantity as well
def subtotal(CART):
	cart_content_list = CART.cart_content_set.all()
	sum=0
    	
	for item in cart_content_list:
		sum += (item.Quantity*item.ISBN.Price)
	
	return sum
    	

def get_cart_items(request):

    return
