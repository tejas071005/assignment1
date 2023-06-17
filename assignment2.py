n1=1 
while n1 == 1: 
    print("\n Menu For calculations") 
    print("1) Addition \n2) Subtraction \n3) Multiplication \n4) Division \n5) Exponential \n6) Floor Division") 
    num=int(input("Enter your choice: ")) 
    if num == 1: 
        x=float(input("First Value  :")) 
        y=float(input("Second Value :")) 
        print("Addition is : ",(x+y)) 
    elif num==2: 
        x=float(input("First Value :")) 
        y=float(input("Second Value :")) 
        print("Subtraction is : ",(x-y)) 
    elif num==3 : 
        x=float(input("First Value :")) 
        y=float(input("Second Value :")) 
        print("Multiplication is : ",(x*y)) 
    elif num==4: 
        x=float(input("First Value :")) 
        y=float(input("Second Value :")) 
        print("Division is : ",(x/y))
    elif num==5:
        x=float(input("First Value :"))
        y=float(input("Second Value :"))
        print("Exponential is :",(x**y)) 
    elif num==6:
        x=float(input("First Value :"))
        y=float(input("Second Value :"))
        print("Floor Division is :",x//y)
    else: 
        print("Wrong choice") 
    n=input("If you want to continue press 1 \n otherwise press any key ") 
    if n!="1": 
        exit()
    n1=int(n)