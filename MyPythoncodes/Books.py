dictionary={}
class Book:
    def __init__(self,title,author,is_borrowed):
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed

class Library(Book):

    def __init__(self, title, author, is_borrowed,book_id):
        super().__init__(title, author, is_borrowed)
        self.book_id=book_id
    
    def add(self, book_id, title, author):
        global dictionary
        if(book_id in dictionary):
            print("This book id exist,create an another log")    
            return 
        dictionary[book_id]={"title":title, "author":author, "is_borrowed":False } #not borrowed
        print(f"we succesfully added {title} written by {author}")

    def borrow(self,book_id):
        global dictionary
        if book_id not in dictionary:
            print("Does not exits") 
            return
        if not (dictionary[book_id]["is_borrowed"]):
            print(f"You borrowed {dictionary[book_id]['title']} by {dictionary[book_id]['author']}, Successfully.")
            dictionary[book_id]["is_borrowed"] = True  # borrowed
        else:
            print("Cannot Borrow, Its already Taken,OOps hehe")

    def remove(self,book_id):
        global dictionary
        if book_id not in dictionary:
            print("Doesnt exists_ book id")
        else:
            print(f"we succesfully deleted {dictionary[book_id]['title']} written by {dictionary[book_id]['author']}")
            dictionary.pop(book_id)

    def display(self):
        global dictionary
        if not dictionary:
            print("\n Hey, Our library is Empty")
            return
        print(dictionary)

lib = Library("", "", False, 0) 
while True:
    print("Welcome To Library\n")
    print("1.Add Book\n")
    print("2.Borrow Book\n")
    print("3.Delete Book\n")
    num=int(input("choose a number or Press 0 to exit"))
    if num == 0:
        print("Closing Library, Bye")
        break
    elif num == 1:
        print("\nEnter Details To Add")
        book_id=int(input("\nenter the book id"))
        title=input("\nenter the title")
        author=input("\nenter the author")
        
        lib.add(book_id,title,author)
        lib.display()
    elif num == 2:
        book_id=int(input("\nenter the book id for borrow"))
        
        lib.borrow(book_id) 
        lib.display()  
    elif num == 3:
        book_id=int(input("\nenter the book id for delete"))
        
        lib.remove(book_id)   
        lib.display()
    else:
        print("Wrong Input")  