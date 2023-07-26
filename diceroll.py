import random

def dice_rolling_simulator():
    print("Welcome to Dice Rolling Simulator!")

    while True:
        input("Press Enter to roll the dice...")
        dice_value = random.randint(1, 6)
        print(f"You rolled a {dice_value}!")

        play_again = input("Do you want to roll again? (y/n): ").lower()
        if play_again != "y":
            break

