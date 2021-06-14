#importing tkinter module
from tkinter import *
from tkinter import ttk

#Creating object - root of Tk()
root = Tk()

#this will make a screen size
root.geometry("750x750")
root.configure(background="Red")
#Providing title to the form
root.title('Registration form')

#this creates 'Label' widget for Registration Form and uses place() method.
label_0 =Label(root,text="Registration form", width=15,font=("bold",20))
#this method used to apply in specific postion
label_0.place(x=145,y=30)



label_1 =Label(root,text="First Name", width=15,font=("bold",10))
label_1.place(x=100,y=100)

entry_1=Entry(root)
entry_1.place(x=250,y=100)

label_2 =Label(root,text="Second Name", width=15,font=("bold",10))
label_2.place(x=100,y=150)

entry_2=Entry(root)
entry_2.place(x=250,y=150)

label_3 =Label(root,text="Email", width=15,font=("bold",10))
label_3.place(x=100,y=200)

entry_3=Entry(root)
entry_3.place(x=250,y=200)

label_4 =Label(root,text="Phone Number", width=15,font=("bold",10))
label_4.place(x=100,y=250)

entry_4=Entry(root)
entry_4.place(x=250,y=250)

label_5 =Label(root,text="Gender", width=15,font=("bold",10))
label_5.place(x=100,y=300)


#the variable 'var' mentioned here holds Integer Value, by deault 0
var=IntVar()

#this creates 'Radio button' widget and uses place() method
Radiobutton(root,text="Male",padx= 5, variable= var, value=1).place(x=250,y=300)
Radiobutton(root,text="Female",padx= 20, variable= var, value=2).place(x=320,y=300)


label_6=Label(root,text="Country",width=15,font=("bold",10))
label_6.place(x=100,y=350)

#this creates list of countries available in the dropdownlist.
list_of_country=[ 'India' ,'Canada' , 'UK' ,'USA' ,'France' , 'Italy']

#the variable 'c' mentioned here holds String Value, by default ""
c=StringVar()
droplist=OptionMenu(root,c, *list_of_country)
droplist.config(width=20)
c.set('Select your Country')
droplist.place(x=250,y=350)

label_7=Label(root,text="Language",width=15,font=("bold",10))
label_7.place(x=100,y=400)

#this creates list of Language available in the dropdownlist.
list_of_language=[ 'English' ,'French' , 'Tamil' ,'Hindi' ,'Others']

#the variable 'z' mentioned here holds String Value, by default ""
z=StringVar()
droplist=OptionMenu(root,z, *list_of_language)
droplist.config(width=20)
c.set('Select your Language')
droplist.place(x=250,y=400)



# Creating Check Box
#the variable 'var1' mentioned here holds Integer Value, by default 0
var1=IntVar()
#this creates Checkbutton widget and uses place() method.
Checkbutton(root,text="Accept Terms and Condition", variable=var1).place(x=350,y=450)


#this creates button for submitting the details provides by the user
Button(root, text='Submit' , width=20,bg="White",fg='black',font=("bold",10)).place(x=100,y=500)

#this will run the mainloop.
root.mainloop()