#LESSON 1
#we are creating the manual type objects
class Animal:#all functions will contain self
    def mammals(self):
        print(f"i am a mammal, {self.name}")

obj1=Animal()
obj1.name="Kangaroo"

obj2=Animal()
obj2.name="Platipus"

obj1.mammals()
obj2.mammals()

#LESSON 2
#now we are creating __init___ based automatic objects
class Animal:#all functions will contain self
    def __init__(self,animal_name):
        self.name=animal_name
    
    def mammals(self):
        print(f"i am a mammal, {self.name}")

obj1=Animal("I am Platipus")
obj2=Animal("I am Kangaroo")


obj1.mammals()
obj2.mammals()


#LESSON 3
#we are linking two objects so do their classes
#linking one new object to other


class Animal():
    def __init__(self,animal_name):
        self.name=animal_name

    def mammal(self):
        print(f"MAMMAL: i am a mammal,{self.name}")

class Person():

    def __init__(self,owner_name):
        self.owner_=owner_name
          
    def owner(self):
        print(f"OWNER: hey i am the owner {self.owner_}")

object_Animal=Animal("Elephant")
object_Animal.mammal()
object_Animal=Animal("Mammoth")

object_Person=Person("James")
object_Person.owner()

#object_person owns the object_animal, ie, owner owns animal
object_Person.owns=object_Animal
object_Person.owns.mammal()
print("this code works")


#summary
#1.class with manual objects
#2.class with automatic objects
#3.links one objects to another object
#4. use super().__init___
#5. inherit cheyyumbol super() allel parent nte per kodkanm. childe class(parent name)