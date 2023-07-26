from tkinter import *
import webbrowser

def search():
    entered_text = e1.get()
    shop_app_dict = {
         "amazon" : "https://www.amazon.in/" ,
        "flipkart" : "https://www.flipkart.com/" ,
        "meesho" : "https://www.meesho.com/",
        "myntra" : "https://www.myntra.com/",
    }
    if entered_text.lower() in shop_app_dict:
        webbrowser.open(shop_app_dict[entered_text.lower()])
    else :
        l2.config(text= "No such app found")
        

obj = Tk(className="Link finder")

l1 = Label(obj,text="Shopping app",font=("Italic",26))
l1.grid()

e1 = Entry(obj,font=("Italic",24))
e1.grid()

l2 = Label(obj,text=" ",font = ("Italic",24),fg ="red")
l2.grid()

b1 = Button(obj,text= "Search",font = ("Italic",26),command=search)
b1.grid()

obj.mainloop()
