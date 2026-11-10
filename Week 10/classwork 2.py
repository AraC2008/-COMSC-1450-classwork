'''
import tkinter as tk
from tkinter import messagebox

def On_click ():
    if e.get().strip() == "":
        messagebox.showwarning("ERROR", "please enter a value")
    else:
        result = 0
        x = float(e.get().strip())
        if r.get() == "EURO":
            result = x * 0.95
        elif r.get() == "CAD":
            result = x * 0.52
        elif r.get() == "ADU":
            result = x * 0.62
        l2.config(text = result)



root=tk.Tk()
root.title("GUI")
root.geometry("400x400")

l = tk.Label(root, text="enter")
l.pack()

e = tk.Entry(root)
e.pack()
r = tk.StringVar()


rb1 = tk.Radiobutton(root, text ="EURO", variable=r , value ="EURO")
rb1.pack()

rb2 = tk.Radiobutton(root, text ="CAD" , variable=r , value = "CAD")
rb2.pack()

rb3 = tk.Radiobutton(root, text = "ADU" , variable=r, value="ADU")
rb3.pack()
b= tk.Button(root, text = "Submit", command = On_click)
b.pack()

l2 = tk.Label(root)
l2.pack()

root.mainloop()
'''
'''
import tkinter as tk
def on_click():
    root2 = tk.Toplevel(root)
    root2.title("Window 2")
    root2.geometry("300x300")
    x = "Welcome "+ e.get()
    l = tk.Label(root2, text= x)
    l.pack()


root = tk.Tk()
root.title("Window 1")
root.geometry("300x300")
e = tk.Entry(root)
e.pack()
b =tk.Button(root, text= "ok", command = on_click)
b.pack()
root.mainloop()
'''
'''
import tkinter as tk
def show_page(frame):
    home_page.pack_forget()
    course_page.pack_forget()
    resistration_page.pack_forget()
    frame.pack(fill="both", expand=1)

root = tk.Tk()
root.title("Window 1")
root.geometry("300x300")

main_menu = tk.Menu(root)
f1 = tk.Menu(main_menu, tearoff=0)
f1.add_command(label = "Open")
f1.add_command(label = "Save")
f1.add_separator()
f1.add_command(label = "Exit" , command = root.destroy)
main_menu.add_cascade(label="File", menu = f1)
root.config(menu=main_menu)



f2 = tk.Menu(main_menu,tearoff=0)
f2.add_command(label = "Courses", command= lambda:show_page(course_page))
f2.add_command(label= "Registration" , command= lambda:show_page(resistration_page))
main_menu.add_cascade(label = "Services", menu=f2)
home_page = tk.Frame(root)
l1 = tk.Label(home_page, text = "home page")
l1.pack()

course_page =tk.Frame(root)
l2 = tk.Label(course_page, text = "Course page")
l2.pack()

resistration_page= tk.Frame(root)
l3 = tk.Label(resistration_page, text = "Resistation page")
l3.pack()

b =tk.Button(home_page, text= "ok")
b.pack()
show_page(home_page)
root.mainloop()
'''
'''
def On_click ():
    result = 0
    x = float(e.get().strip())
    if r.get() == "Standard":
       result = x + 5
    elif r.get() == "Express":
         result = x + 15
    elif r.get() == "Overnight":
         result = x + 30
    l2.config(text = result)

import tkinter as tk
root=tk.Tk()
root.title("GUI")
root.geometry("400x400")

l1= tk.Label ( root, text ="Shipping Methods")
l1.pack()

e = tk.Entry(root)
e.pack()
r = tk.StringVar()

rb1 = tk.Radiobutton(root, text ="Standard", variable=r , value ="Standard")
rb1.pack()

rb2 = tk.Radiobutton(root, text ="Express" , variable=r , value = "Express")
rb2.pack()

rb3 = tk.Radiobutton(root, text = "Overnight" , variable=r, value="Overnight")
rb3.pack()

b= tk.Button(root, text = "Submit", command = On_click)
b.pack()

l2 = tk.Label(root)
l2.pack()

root.mainloop()
'''