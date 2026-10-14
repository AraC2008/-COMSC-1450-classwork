import random
import math
def play_bounded_guessing_game():
    Secret_num =random.randint(1,10)
    for i in range (3):
        Guess = int(input("Enter your guess (1-10): "))
        if Guess == Secret_num:
            print("Congratulations! You won!")
            return
        if i < 2:
            print("Wrong guess! Try again.")
    print(f"Game Over! The secret number was {Secret_num}." )
play_bounded_guessing_game()