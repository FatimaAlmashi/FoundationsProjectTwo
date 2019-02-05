# CLASSES AND METHODS
class Store():

    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        self.name = name
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        self.product = product
        self.products.append(product)

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        for p in self.products:
            print ("\t\t Product name: %s" %(p.name))
            print ("\t\t Discription: %s" %(p.description))
            print ("\t\t Price: %s" %(p.price))
            print()


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        # your code goes here!
        return ""


class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        self.products = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        self.products.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        total_price = 0
        for p in self.products:
            total_price += p.price
        return total_price

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        print()
        print("------------------------------------------")
        print("Here's your receipt :")
        for p in self.products:
            print ("\t\t Product name: %s" %(p.name))
            print ("\t\t Discription: %s" %(p.description))
            print ("\t\t Price: %s" %(p.price))
            print()
        print("Your Total Price is : KD%s" %(self.get_total_price()))
        

    def checkout(self):
        """
        Does the checkout.
        """
        self.print_receipt()
        confirm = input("Confirm? (Y/N) : ")
        if confirm == 'N' or confirm == 'n':
            print("Your order has been canceled.")
        else:   
            print("Your order has been placed.")
        
            








