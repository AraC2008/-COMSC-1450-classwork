'''
import tkinter as tk
root = tk.Tk()
root.title("GUI")
root.geometry("500x500")
label1 = tk.Label(root,text = "Welcome to UST, Please enter your name")
label1.pack(pady=20)
entry1 = tk.Entry(root)
entry1.pack()
label1 = tk.Label(root,text = "Please enter a comment")
label1.pack(pady=20)
text = tk.Text(root, height=4,width=50)
text.pack()
b1 = tk.Button(root, text = "Submit", command=root.destroy)
b1.pack(pady = 20 )
root.mainloop()
'''
'''
import tkinter as tk
def welcome():
    l3.config(text = "Welcome" +"   "+ e1.get()+ "   "+e2.get(),)



root = tk.Tk()
root.title("Greeting")
root.geometry("400x500")
L1 = tk.Label(root, text = "First name: ", bg = "lightblue", fg = "Navyblue",font=("Times New Roman",14))
L1.grid(row = 0 , column= 0,padx=20,pady=20)
e1 = tk.Entry(root)
e1.grid(row = 0 , column= 1,padx=20,pady=20)
l2 =tk.Label(root, text = "Last name", bg = "lightblue",fg = "Navyblue",font=("Times New Roman",14))
l2.grid(row = 1 , column= 0,padx=20,pady=20)
e2 = tk.Entry(root)
e2.grid(row = 1 , column= 1,padx=20,pady=20)
b = tk.Button(root, text= "OK", command=welcome)
b.grid(row = 2 , column= 0,padx=20,pady=20, columnspan=2)
root.config(bg="lightblue" )
l3 = tk.Label(root, bg = "lightblue",fg = "Navyblue",font=("Times New Roman",14))
l3.grid (row = 3, column = 0, )
root.mainloop()
'''