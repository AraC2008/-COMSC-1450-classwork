def process_atm_transactions(balance):
    count = 0
    amount = float(input("Enter transaction amount (0 to quit): "))
    while amount != 0:
        if amount > 0:
            balance += amount
            count += 1
        else:
            if balance >= -amount:
                balance += amount
                count += 1
            else:
                print("Insufficient funds.")
        amount = float(input("Enter transaction amount (0 to quit): "))
    return balance,count
def main():
     balance = float(input("Enter starting balance: "))
     final_balance,transactions =  process_atm_transactions(balance)
     print("Final balance:",final_balance)
     print("Successful transactions:",transactions)
main()