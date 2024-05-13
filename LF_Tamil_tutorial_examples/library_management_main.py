class Library():
    def __init__(self,list):
        self.all_books_list=list
        self.available_books_list=list[:]
        self.books_lent={}    #shows,which user has which book ; {key:book details,value:user details}

    def display_all_books(self):
        for books in self.all_books_list:
            print(books)

    def display_available_books(self):
        for ava_books in self.available_books_list:
            print(ava_books)

    def lend_books(self,name,book):
        if book not in self.all_books_list:
            print("this book is not in our library,please check book details once again!")
            return
        if book not in self.available_books_list:
            print("this book is not available right now,lent to the user:" + name)

        if book in self.available_books_list:
            self.books_lent.update({book:name})
            self.available_books_list.remove(book)
            print("you can take this book")

    def return_books(self,book):
        del self.books_lent[book]
        self.available_books_list.append(book)

if __name__=='__main__':       #when we like to run ;the function/methods under this ; only when we call in this module/file only
    lib=Library(["harry potter-1","harry potter-2","harry potter-3"])
    lib2=None
    print(__name__)
 #we create many objects ; as our wish when we have many library ; & to display details in it by assinng it.....
    print("\nwelcome to our online library page.Enter the choice")
    while True:
        print("\n1.Display all books")
        print("2.available books")
        print("3.borrow books")
        print("4.return books")
        print("5.Quit")
        user_choice = int(input("enter your choice:"))
        if user_choice==1:
            lib.display_all_books()
        elif user_choice==2:
            lib.display_available_books()
        elif user_choice==3:

            book = input("enter book name:")

            name = input("enter your name:")
            lib.lend_books(name, book)


        elif user_choice==4:
            book=input("Enter the name of the book:")
            lib.return_books(book)
        elif user_choice==5:
            print("Thank you!")
            break
        else:
            print("invalid choice")

#using list for storing data's is waste ; all data's about details of books will be lost ; if we close this file
#instead use a particular file (or) connectivity to database ****(sql)****

