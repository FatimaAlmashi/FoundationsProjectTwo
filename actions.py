# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "Noon"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    print()
    for s in stores:
        print("- %s" %s.name)
    print()

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    for s in stores:
        if store_name == s.name:
            return s
    return False


def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    print_stores()
    print('Pick a store by typing its name. Or type "checkout" to pay your bills and say your goodbyes.')
    answer = input()
    while True:
        if answer == 'checkout' or answer == 'ch':
            return "checkout"
        else:
            if get_store(answer):
                return get_store(answer)
            else:
                print("Not a valid store")
        answer=input()

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    print ("------------------------------------------")
    print("%s :"%(picked_store.name))
    picked_store.print_products()
    print("Pick the items you'd like to add in your cart by typing the product name exactly as it was spelled above.")
    print("Type 'back' to go back to the main menu where you can checkout.")
    inp = input()
    while True:
        if inp == 'back' or inp == 'b':
            break
        for p in picked_store.products:
            if inp == p.name:
                cart.add_to_cart(p)         
        inp = input()


def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    while True:
        picked_store = pick_store()
        if picked_store == "checkout":
            break
        elif picked_store != False:
            pick_products(cart, picked_store)
    cart.checkout()

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
