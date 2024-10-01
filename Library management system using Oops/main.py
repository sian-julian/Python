#Admin section
class Admin:
    def __init__(self):
        self.books=[]
        self.admincred={'username':'sian','password':1234}

    def adminlog(self):
        print("**Admin Login**")
        username=input("Enter your Username:")
        password=int(input("Enter your password:"))

        if self.admincred['username']==username and self.admincred['password']==password:
            print("WELCOME SIAN\n")
            self.adminmenu()
        else:
            print("INVALID CREDENTIALS!!\n")
    
    def adminmenu(self):
        while True:
            print("**Admin Menu**")
            print("1.Add Book\n2.Update Book\n3.Delete Book\n4.Display All Books\n5.Exit from the admin menu\n")
            ch=int(input("Enter your choice:"))

            if ch==1:
                self.addbook()
            elif ch==2:
                self.updatebook()
            elif ch==3:
                self.deletebook()
            elif ch==4:
                self.displaybook()
            elif ch==5:
                print("Exiting from the Admin Menu...")
                print()
                break
            else:
                print("INVALID CHOICE!!....try again")
                print()
        
    def addbook(self):
        print("**Add Book**")
        book={}
        while True:
            bookid=input("Enter the Books id:")
            if any(book['bookid']==bookid for book in self.books):
                print("Book id Alreday Exist!!...Try another Book id\n")
            else:
                book['bookid']=bookid
                break
        book['bname']=input("Enter the Book Title:")
        book['bauthor']=input("Enter the Book's Author name:")
        book['bqnty']=int(input("Enter the book quantity:"))

        self.books.append(book)
        print("Book Added Successfully!!\n")
    

    def updatebook(self):
        print("**Update Book**")
        if self.books:
            bid=input("Enter the book id to update:")
            found=False
            
            for book in self.books:
                if book['bookid']==bid:
                    book['bname']=input("Enter the New Book Title:")
                    book['bauthor']=input("Enter the New Author's Name:")
                    book['bqnty']=int(input("Enter the Updated Book Quantity:"))
                    print("Book Updated Successfully!!")
                    found=True
                    break
            if found==True:
                print()
            else:
                print("Book Not Found!!")
                print()
        else:
            print("No Books Added!!")
            print()


    def deletebook(self):
        print("**Delete Book**")
        if self.books:
            bid=input("Enter the book id to delete the book:")
            found=False
            
            for i,book in enumerate(self.books):
                if book['bookid']==bid:
                    del self.books[i]
                    print("Book Deleted Successfully!!")
                    found=True
                    break
                
            if found==True:
                print()
            else:
                print("Book Not Found!!")
                print()
        else:
            print("No Books Added!!")
            print()

    def displaybook(self):
        print("**Display All Books**")
        if self.books:
            for i,book in enumerate(self.books,start=1):
                print(f"Book no: {i}")
                print(f"Book id: {book['bookid']}")
                print(f"Book Name: {book['bname']}")
                print(f"Book Author: {book['bauthor']}")
                print(f"Book Quantity: {book['bqnty']}")
                print()
        else:
            print("No Books Added!!")
            print()


#User Section
class User(Admin):
    def __init__(self,books):
        self.users=[]
        super().__init__()
        self.books=books

    def usersection(self):
        while True:
            print("**User Section**")
            print("1.Registration\n2.Login\n3.Exit from the User Section\n")
            ch=int(input("Enter your choice:"))
            print()

            if ch==1:
                self.uregister()
            elif ch==2:
                self.ulogin()
            elif ch==3:
                print("Exiting From the User Section....")
                print()
                break  
            else:
                print("INVLAID CHOICE!!...try again") 
                print() 
    
    def uregister(self):
        print("**User Registration**")
        user={}
        user['name']=input("Enter your Name:")
        user['age']=input("Enter your Age:")
        user['address']=input("Enter your Address:")
        while True:
            username=input("Enter a Username:")

            if any(user['uname']==username for user in self.users):
                    print("Username already exists....try another Username")
            else:
                user['uname']=username
                break
                
        while True:
            phone=input("Enter your phone number:")

            if any(user['phoneno']==phone for user in self.users):
                print("Phone Number already exists....Try another phone")
            else:
                user['phoneno']=phone
                break
        
        user['pass']=input("Enter a Password:")
        self.users.append(user)
        print("User Registration Successfull!!")
        print()

    
    def ulogin(self):
        print("**User Login**")
        username=input("Enter your Username:")
        password=input("Enter your password:")
        found=False

        for user in self.users:
            if user['uname']==username and user['pass']==password:
                print("WELCOME")
                found=True
                self.usermenu()
                break

        if found==True:
            print()
        else:
            print("INVALID CREDENTIALS!!")
            print()
            
        
    def usermenu(self):
        while True:
            print("**USER MENU**")
            print("1.Display All Books\n2.Search Book by Name\n3.Exit from the User menu")
            ch=int(input("Enter your choice:"))
            print()

            if ch==1:
                self.displaybook()
            elif ch==2:
                self.searchbook()
            elif ch==3:
                print("Exiting from the User Menu...")
                print()
                break
            else:
                print("INVALID CHOICE!!....try again")
                print()

    def searchbook(self):
        print("**Search Book**")
        if self.books:
            bname=input("Enter the Books Name you want to search:")
            found=False

            for book in self.books:
                if book['bname']==bname:
                    print(f"Book Title: {book['bname']}")
                    print(f"Book Author: {book['bauthor']}")
                    print(f"book Quantity: {book['bqnty']}")
                    found=True
                    print()
                    break
            if found:
                print()
            else:
                print("Book not Found!!")
                print()
        else:
            print("No Books Added!!")
            print()


#Main Section
ad=Admin()
us=User(ad.books)

while True:
    print("***LIBRARY MANAGEMENT SYSTEM***")
    print("1.Admin\n2.User\n3.Exit")
    ch=int(input("Enter your choice:"))
    print()

    if ch==1:
        ad.adminlog()
    elif ch==2:
        us.usersection()
    elif ch==3:
        print("Exiting from the program...")
        break
    else:
        print("INVALID CHOICE!!....try again")
    