def ds(roll_no,name):
    global lst 
    global t1
    global s1
    global d1
    lst=[roll_no,name]
    t1=(roll_no,name)
    s1={roll_no,name}
    d1={"Roll no ": roll_no , "Name ":name}


def printds():
    print("\nList : ",lst,"\n")
    print("Tuple : ",t1,"\n")
    print("Set : ",s1,"\n")
    print("Dictionary : ",d1,"\n")


def ds_update():
    print("__________________________\n")
    print("Updating the data structures")
    print("__________________________\n")
    x=int(input("Enter the roll no : "))
    y=input("Enter the name : ")
    ds(x,y)
    print("\nList : ",lst,"\n")
    print("Tuple : ",t1,"\n")
    print("Set : ",s1,"\n")
    print("Dictionary : ",d1)

def applyingmeth():
    print("_____________________________________\n")
    print("Applying some method in data structures")
    print("_____________________________________\n")
    lst.append("class")
    print("\n--> appending the List : ",lst)
    lst.pop(0)
    print("--> poping at [0] form the List : ",lst,"\n")

    s1.add("class")
    s1.add("Sycob")
    print("\n--> adding item into Set : ",s1)
    s1.pop()
    print("--> poping the item from Set : ",s1,"\n")

    d1.update({"class":"Sycob"})
    print("\n--> adding the item in Dictionary : ",d1)
    d1.pop("class")
    print("--> poping the item from dictionary : ",d1)

def deletemeth():
    print("________________________________________\n")
    print("Calling the data structures after deleting")
    print("________________________________________\n")
    del lst
    del t1
    del s1
    del d1
    print("\nList : ",lst,"\n")
    print("Tuple : ",t1,"\n")
    print("Set : ",s1,"\n")
    print("Dictionary : ",d1)  

ds(103,"Tejas")
printds()
ds_update()
applyingmeth()
deletemeth()