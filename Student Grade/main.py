while(True):
    mark=int(input("Enter the mark:"))
    
    if(mark>=90 and mark<=100):
        print("A+")
        break
    elif(mark>=80 and mark<90):
        print("A")
        break
    elif(mark>=70 and mark<80):
        print("B+")
        break
    elif(mark>=60 and mark<70):
        print("B")
        break
    elif(mark>=50 and mark<60):
        print("C+")
        break
    elif(mark>=40 and mark<50):
        print("C")
        break
    elif(mark<40 and mark >=0):
        print("FAIL")
        break
    else:
        print("invalid marks")