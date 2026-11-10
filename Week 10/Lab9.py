'''
import tkinter as tk
def evaluate_grade():
    x =int( e2.get())
    if x >= 60:
        l3.config(text = "passed"+"   "+ e1.get())
    else:
        l3.config(text = "failed" +"   " + e1.get())

root = tk.Tk()
root.title("Course Grading Tool")
root.geometry("400x500")
L1 = tk.Label(root, text = "Course name: ", bg = "lightblue", fg = "Navyblue",font=("Times New Roman",14))
L1.grid(row = 0 , column= 0,padx=20,pady=20)
e1 = tk.Entry(root)
e1.grid(row = 0 , column= 1,padx=20,pady=20)
l2 =tk.Label(root, text = "score", bg = "lightblue",fg = "Navyblue",font=("Times New Roman",14))
l2.grid(row = 1 , column= 0,padx=20,pady=20)
e2 = tk.Entry(root)
e2.grid(row = 1 , column= 1,padx=20,pady=20)
b = tk.Button(root, text= "Evaluate", command=evaluate_grade)
b.grid(row = 2 , column= 0,padx=20,pady=20, columnspan=2)
root.config(bg="lightblue" )
l3 = tk.Label(root, bg = "lightblue",fg = "Navyblue",font=("Times New Roman",14))
l3.grid (row = 3, column = 0, )
root.mainloop()
'''
'''
import tkinter as tk
def Convert_currency():
    x = float(e1.get())
    euro = x * 0.92
    l2.config(text =f"Amount in Euro: {euro}" )

root = tk.Tk()
root.title("Currency Exchange Converter")
root.geometry("450x250")
L1 = tk.Label(root, text = "Amount in UDS($): ", bg = "lightblue", fg = "Navyblue",font=("Times New Roman",14))
L1.grid(row = 0 , column=0 ,padx=20,pady=20)
e1 = tk.Entry(root)
e1.grid(row = 0 , column= 1,padx=20,pady=20)
b = tk.Button(root, text= "Convert", command=Convert_currency)
b.grid(row = 1 , column= 0,padx=20,pady=20, columnspan=2)
l2 = tk.Label(root,bg = "lightblue", fg = "Navyblue",font=("Times New Roman",14))
l2.grid(row = 2 , column= 0,padx=20,pady=20, columnspan=2)
root.config(bg="lightblue" )

root.mainloop()
'''
'''
def On_click ():
    x = "You have picked "
    if cv.get() == 1:
       x = x + "Vegetarian"
    if cv1.get() == 1:
         x = x + "Gluten-Free"
    if cv2.get() == 1:
         x = x + "Nut-Free"
    l2.config(text = x)
    
import tkinter as tk
root = tk.Tk()
root.title("GUI")
root.geometry("400x400")
l1 = tk.Label(root, text ="Select your ditetary restrictions")
l1.pack()

cv = tk.IntVar()
cv1 = tk.IntVar()
cv2 = tk.IntVar()
cb1 = tk.Checkbutton(root, text ="Vegetarian", variable=cv)
cb1.pack()

cb2 = tk.Checkbutton(root, text = "Gluten-Free", variable=cv1)
cb2.pack()

cb3 = tk.Checkbutton(root, text = "Nut-Free", variable=cv2)
cb3.pack()

b = tk.Button(root, text ="Ok" , command=On_click)
b.pack()

l2 = tk.Label(root)
l2.pack()

root.mainloop()
'''

'''
import tkinter as tk
def on_click():
    root2 = tk.Toplevel(root)
    root2.title("User Health Analytics")
    root2.geometry("300x300")
    x= float(e.get())*0.453592
    l = tk.Label(root2, text= x)

    l.pack()


root = tk.Tk()
root.title("Fitness intake panel")
root.geometry("300x300")
e = tk.Entry(root, text = "Enter Your Weight in Pounds (lbs):")
e.pack()
b =tk.Button(root, text= "Generate Metric Profile", command=on_click)
b.pack()
root.mainloop()
'''
'''
import tkinter as tk
def display(color):
     l.config(text = color + " "+  "Was selected")

root = tk.Tk()
root.title("Window 1")
root.geometry("300x300")

main_menu = tk.Menu(root)
f1 = tk.Menu(main_menu, tearoff=0)
f1.add_command(label = "Red",command= lambda: display("Red"))
f1.add_command(label = "Blue",command = lambda: display("Blue"))
main_menu.add_cascade(label="colors" , menu= f1)
root.config(menu=main_menu)
l= tk.Label(root,text="No color as selected")
l.pack()
root.mainloop()
'''