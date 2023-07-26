import webbrowser as wb
from tkinter import * 

obj = Tk(className="Window")

e = Entry(obj,font=("Italic",26))
e.grid()

def submit():
    query=e.get()
    wb.open("https://www.google.com/search?q="+query)
    print("The entered text is: ",query)
    print("Navigating to https://www.google.com/search?q="+query)


b=Button(obj,text="Search",
         command=submit,
         font=("",30))

b.grid()

b1=Button(obj,text="Close",
         command=obj.destroy,
         font=("",30))
b1.grid()
obj.mainloop()

