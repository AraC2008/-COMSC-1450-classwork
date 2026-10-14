def calculate_playroll():
    total_payroll = 0.0
    wage = float(input("Enter hourly wage (negative to quit): "))
    while wage >= 0:
        hours = float(input("Enter hours worked: "))
        if hours > 40:
            pay = (40*wage) +((hours-40)*(wage*1.5))
        else:
            pay = hours* wage
        total_payroll += pay
        wage = float(input("Enter hourly wage (negative to quit): "))
    if total_payroll > 5000:
        print("Payroll exceeded the budget.")
    return total_payroll
def main():
    total_payroll = calculate_playroll()
    print("Total payroll: $", round(total_payroll,2))
main()