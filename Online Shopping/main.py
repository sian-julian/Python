#Admin Section

def admin(admin_cred,products):
    print("**ADMIN PAGE**\n")
    admuser=input("Enter your Username:")
    adpass=input("Enter your Password:")
    print()

    for admin1 in admin_cred:
        if admin1['username']==admuser and admin1['password']==adpass:
            print("WELCOME SIAN")
            print()
            admin_menu(products)
        else:
            print("INVALID CREDENTIALS!!")
            print()


def admin_menu(products):
    print("**Admin Menu**\n")
    while True:
        print("1.Add Product\n2.Update Product\n3.Remove Product\n4.View All Products\n5.View Orders\n6.Exit from the Admin menu\n")
        ch=int(input("Enter your Choice:"))
        print()

        if ch==1:
            addprod(products)
        elif ch==2:
            updateprod(products)
        elif ch==3:
            removeprod(products)
        elif ch==4:
            vaprod1(products)
        elif ch==5:
            vieworders(orders)
        elif ch==6:
            print("Exiting from the Admin menu...")
            break
        else:
            print("INVALID CHOICE!!...try again")
            print()


def addprod(products):
    print("**Add Product**")
    product={}

    while True:
        pid=str(len(products)+1)

        if any(product['pid']==pid for product in products):
            print("Product id already exists....try another product id\n")
        else:
            product['pid']=pid
            print(f"this product has been assigned with id: {product['pid']}")
            break

    product['pname']=input("Enter the name of the product:")
    product['pdescr']=input("Enter the description about the product:")
    product['price']=input("Enter the price of the product:")
    # while True:
    #     qnty=int(input("Enter the Product Quantity:"))
    #     if any(product['pid']==pid for product in products):
    #         product['qnty']+=qnty
    #         break
    #     else:
    #         product['qnty']=qnty
    #         break
    product['pavailable']="Available"

    products.append(product)
    print("Product Added Successfully!!")
    print()


def updateprod(products):
    print("**Update Product Details**\n")
    if products:
        pid=input("Enter the product id:")
        found=False

        for product in products:
            if product['pid']==pid:
                product['pname']=input("Enter the new name of the product:")
                product['pdescr']=input("Enter a new description about the product:")
                product['price']=input("Enter the new price of the product:")
                found=True
                print("Product Updated Successfully!!")
                break
        if found==True:
            print()
        else:
            print("Product not found!!")
            print()
    else:
        print("No products Added!!")
        print()


def removeprod(products):
    print("**Remove Products**\n")
    if products:
        pid=input("Enter the product id:")
        found=False

        for i,product in enumerate(products):
            if product['pid']==pid:
                del products[i]
                print("Product Removed Successfully!!")
                found=True
                break
        if found==True:
            print()
        else:
            print("Product not found!!")
            print()
    else:
        print("No products Added!!")
        print()


def vaprod1(products):
    print("**View all Available products**\n")
    if products:
        for i,product in enumerate(products,start=1):
            if product["pavailable"]=="Available":
                print(f"*Product {i}*\n")
                print(f"Product id: {product['pid']}")
                print(f"Product Name: {product['pname']}")
                print(f"Product Description: {product['pdescr']}")
                print(f"Product Price: {product['price']}")
                print()
    else:
        print("No products Added!!")
        print()


def vieworders(orders):
    print("**View Orders**\n")

    if orders:
        for i,order in enumerate(orders,start=1):
            print(f"Order {i}")
            print(f"User id: {order['user id']}")
            print(f"User Name: {order['users name']}")
            print(f"Product: {order['product']}")
            print(f"Product Quantity: {order['qnty']}")
            print(f"Order Status: {order['order status']}")
            print()
    else:
        print("No Orders have been placed!!")
        print()



# User Section

def user(users):
    while True:
        print("**USER SECTION**")
        print("1.Registration\n2.Login\n3.Exit\n")
        ch=int(input("Enter your choice:"))
        print()

        if ch==1:
            register(users)
        elif ch==2:
            login(users)
        elif ch==3:
            print("Exiting From the User Section....")
            print()
            break  
        else:
            print("INVLAID CHOICE!!...try again") 
            print()  


def register(users):
    print("**User Registration Page**\n")
    user={}

    while True:
        uid=input("Enter a User id(username):")

        if any(user['uid']==uid for user in users):
            print("This User id already exits...try another user id\n")
        else:
            user['uid']=uid
            break
    
    user['name']=input("Enter your Name:")
    user['email']=input("Enter your Email id:")
    user['address']=input("Enter your address:")
    user['upass']=input("Enter a password:")

    users.append(user)
    print("User Registration Successfull!!")
    print()


def login(users):
    print("**User Login Page**")
    uid=input("Enter your User id(username):")
    upass=input("Enter your password:")
    found=False

    for user in users:
        if user['uid']==uid and user['upass']==upass:
            print("WELCOME")
            print()
            uname=user['name']
            found=True
            login_menu(products,users,uid,uname)

    if not found: 
        print("Invalid Credentials or User not found!!")
        print()   
    

def login_menu(products,users,uid,uname):
    print("**User Menu**\n")
    while True:
        print("1.View All Products\n2.Place Order\n3.View Order History\n4.Exit\n")
        ch=int(input("Enter your Choice:"))

        if ch==1:
            vaprod2(products)
        elif ch==2:
            placeorder(orders,users,uid,uname,products)
        elif ch==3:
            vohistory(orders,uid)
        elif ch==4:
            print("Exiting from the User menu....")
            break
        else:
            print("Inavlid choice....try again")
            print()


def vaprod2(products):
    print("**View all Available products**\n")
    if products:
        for i,product in enumerate(products,start=1):
            if product["pavailable"]=="Available":
                print(f"*Product {i}*\n")
                print(f"Product id: {product['pid']}")
                print(f"Product Name: {product['pname']}")
                print(f"Product Description: {product['pdescr']}")
                print(f"Product Price: {product['price']}")
                print()
    else:
        print("No products Added!!")
        print()
        

def placeorder(orders,users,uid,uname,products):
    print("**Place An Order**\n")

    if products:
        pid=input("Enter the Product id you want to buy:")
        found=False
        order={}

        for product in products:
            if product['pid']==pid and product['pavailable']=="Available":
                qnty=int(input("Enter the Quantity of the product you want:"))
                order['user id']=uid
                order['users name']=uname
                order['product']=product['pname']
                order['qnty']=qnty
                order['order status']="Processing"
                print(f"Order Status: {order['order status']}")
                print("Order Placed Successfully!!\n")
                order['order status']="Shipped"
                print(f"Order Status: {order['order status']}")
                orders.append(order)
                found=True
                break

        if not found:
            print("Product not Found or unAvailable!!")
            print()

    else:
        print("No Products Available!!")


def vohistory(orders,uid):
    print("**View Order History**\n")

    userorders=[order for order in orders if order['user id']==uid]

    if userorders:
        for i,order in enumerate(userorders,start=1):
            print(f"Order {i}\n")
            print(f"User id: {order['user id']}")
            print(f"User's name: {order['users name']}")
            print(f"product: {order['product']}")
            print(f"Quantity: {order['qnty']}")
            print(f"Order Status: {order['order status']}")
            # if order['qnty']=="Processing":

            print()

    else:
        print("No orders have been placed by this user")
        print()

#Main Section
orders=[]
users=[]
products=[]
admin_cred=[]
admin1={}
admin1['username']="sian"
admin1['password']="1234"
admin_cred.append(admin1)

while True:
    print("***ONLINE SHOPPING***\n")
    print("1.Admin\n2.User\n3.Exit\n")
    ch=int(input("Enter your choice:"))

    if ch==1:
        admin(admin_cred,products)
    elif ch==2:
        user(users)
    elif ch==3:
        print("Exiting from the program...")
        break
    else:
        print("INVALID CHOICE!!....Try again")
        print()