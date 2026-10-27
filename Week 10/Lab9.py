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