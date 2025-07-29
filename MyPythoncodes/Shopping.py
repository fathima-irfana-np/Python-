class Product:
    def __init__(self,product_no,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity   
        self.product_no=product_no 
    #    .,index,{},class
class shopPingCart(Product):

    def __init__(self):
         self.dictionary={}
        
    def add(self,product_no,name,price,quantity):
        if product_no in self.dictionary:
            print("\n The item already exist")
            self.dictionary[product_no]["quantity"]+=quantity
            print("\nAdded quantity",quantity)
            return
        statement="\nsuccessfully added: {}to list, +{} with price {}"
        print(statement.format(name,quantity,price))
        product=Product(product_no,name,price,quantity)
        self.dictionary[product_no]=product

    def remove(self,product_no):
        if product_no not in self.dictionary:
            print("\n The item does not exist")
            return
        statement="\n Successfully removed : {} from list, +{} with price {}"
        print(statement.format(self.dictionary[product_no].name,self.dictionary[product_no].quantity,self.dictionary[product_no].price))
        self.dictionary.pop(product_no)

    def sum_total(self):
        if not self.dictionary:
            print("\nYou cannot Calculate Empty Cart")
            return 0
        result=0
        for product in self.dictionary.values():
            result+=product.price*product.quantity
        print(" the cart Summary price is :",result)
      

    def display(self):
        if not self.dictionary:
            print("\nCart is Empty")
        else:
            for product_no, product in self.dictionary.items():
                print(f"ID: {product_no}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

object1=shopPingCart()
object1.add(990,"Sugar",30,2)
object1.add(991,"Milk",50,1)
object1.add(992,"Rice",32,2)
object1.add(993,"Wheat",24,1)
object1.add(994,"Gua",175,4)
print("\n-------------\n",end='')
object1.display()
print("\n-------------\n",end='')
object1.sum_total()
print("\n-------------\n",end='')
object1.remove(993)
object1.remove(992)
print("\n-------------\n",end='')
object1.display()
print("\n-------------\n",end='')
object1.sum_total()
print("\n-------------\n",end='')

"""
hello, Dictionary porth anel self. illathe anu accessing, display okke sadharana pole, 
kaykaryam cheyyalum sadha dictionary pole anu.
ivde nested dictionary anu upayogichath .eg:books.py

Ennaal, self verika anenkil ,parent class okke vechitaan mothathil working, pinne
nested dict alla.ee program anu example

"""


