def calculate_ticket_sales():
    total_sales = 0
    tickets_sold = 0
    age = int(input("Enter your age (-1 to quit): "))
    while age != -1:
        if age < 5:
            price = 0
        elif age <= 12:
            price = 8
        elif age <= 59:
            price = 12
        else:
            price = 9
        total_sales += price
        tickets_sold += 1
        age = int(input("Enter your age (-1 to quit): "))
    if tickets_sold >= 10:
            total_sales = total_sales * 0.95
    return total_sales,tickets_sold
def main():
    total_sales,tickets_sold = calculate_ticket_sales()
    print("Tickets sold: " , tickets_sold)
    print("Final sales amount: $",total_sales)
main()