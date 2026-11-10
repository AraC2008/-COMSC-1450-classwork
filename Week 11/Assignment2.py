import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Personal Health & Travel Assistant")
root.geometry("500x400")
L1 = tk.Label(root, text=" Select an application from the top menu to begin")
L1.pack()

Fitness_Page = tk.Frame(root)
Flight_Page = tk.Frame(root)

activity_label = tk.Label(Fitness_Page, text="Activity Name")
activity_label.grid(row=0, column=0)

activity_entry = tk.Entry(Fitness_Page)
activity_entry.grid(row=0,column=1)

duration_label = tk.Label(Fitness_Page, text="Duration(Minutes)")
duration_label.grid(row=1,column=0)

duration_entry = tk.Entry(Fitness_Page)
duration_entry.grid(row=1,column=1)

intensity_var = tk.StringVar()
intensity_var.set("Low")
low_radio = tk.Radiobutton(Fitness_Page, text="Low", variable=intensity_var, value="Low")
low_radio.grid(row=2,column=0)

Medium_radio = tk.Radiobutton(Fitness_Page, text="Medium", variable=intensity_var, value="Medium")
Medium_radio.grid(row=2,column=1)

High_radio = tk.Radiobutton(Fitness_Page,text="High", variable=intensity_var, value="High")
High_radio.grid(row=2,column=2)

def log_workout():
    activity = activity_entry.get()
    duration = duration_entry.get()
    if activity =="" or duration =="":
        messagebox.showwarning("Warning", "Please complete all fields")
        return
    duration = int(duration)
    if intensity_var.get() == "Low":
        calories = duration * 5
    elif intensity_var.get() == "Medium":
        calories = duration * 8
    elif intensity_var.get() == "High":
        calories = duration * 12
    result_label.config(text=f"Logged: {activity} for {calories} Calories!")
    file = open("user_logs.txt","a")

    file.write(f"[FITNESS] Activity: {activity} | Calories Burned: {calories}\n")
    file.close()


log_button = tk.Button(Fitness_Page, text="Log workout",command=log_workout)
log_button.grid(row=3,column=0,columnspan=3)

result_label = tk.Label(Fitness_Page, text="")
result_label.grid(row=4,column=0,columnspan=3)


price_label = tk.Label(Flight_Page, text="Base Ticket Price($)")
price_label.grid(row=0,column=0)

price_entry = tk.Entry(Flight_Page)
price_entry.grid(row=0,column=1)

baggage_var = tk.IntVar()
meal_var = tk.IntVar()
boarding_var = tk.IntVar()

baggage_check = tk.Checkbutton(Flight_Page, text="Checked Baggage", variable= baggage_var)
baggage_check.grid(row=1,column=0)

meal_check = tk.Checkbutton(Flight_Page, text="In-Flight Meal", variable= meal_var)
meal_check.grid(row=2,column=0)

boarding_check = tk.Checkbutton(Flight_Page, text="Priority Boarding", variable= boarding_var)
boarding_check.grid(row=3,column=0)

def calculate_fare():
    if price_entry.get() =="":
        messagebox.showwarning("Warning", "Base ticket price is required.")
        return
    try:
        total = float(price_entry.get())
        if baggage_var.get() == 1:
            total += 35
        if meal_var.get() == 1:
            total += 15
        if boarding_var.get() == 1:
            total += 20
        fare_label.config(text=f"Total Fare: ${total}", fg="black")
        file = open("user_logs.txt", "a")
        file.write(f"[FLIGHT] Base: {price_entry.get()} | Total Fare: {total}\n")
        file.close()
    except ValueError:
        fare_label.config(text="Error: Please enter a numeric base price!", fg ="red")

fare_button = tk.Button(Flight_Page, text="Calculate Total Fare", command=calculate_fare)
fare_button.grid(row=4,column=0,columnspan=2)

fare_label = tk.Label(Flight_Page, text="",font=("Arial", 10, "bold"))
fare_label.grid(row=5,column=0,columnspan=2)



def reset_logs():
    file = open("user_logs.txt","w")
    file.close()
    L1.config(text="System Activity Logs Reset Successfully!",fg="dark green")













def show_page(frame_to_show):
    """Hides all application pages, then packs the chosen one."""
    Fitness_Page.pack_forget()
    Flight_Page.pack_forget()

    frame_to_show.pack(fill="both", expand=True, padx=20, pady=20)

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Reset Activity Logs",command=reset_logs)
file_menu.add_command(label="Exit Application", command=root.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)

App_menu = tk.Menu(menu_bar,tearoff=0)
App_menu.add_command(label="Fitness Tracker", command=lambda: show_page(Fitness_Page))
App_menu.add_command(label="Flight Fare Estimator", command=lambda: show_page(Flight_Page))

menu_bar.add_cascade(label="Applications", menu=App_menu)
root.config(menu=menu_bar)








show_page(Fitness_Page)
tk.mainloop()
