import random

def num_guess():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Number of attempts allowed
    max_attempts = 5

    print("Welcome to the Guess the Number game!")
    print("I have picked a number between 1 and 100. Can you guess it?")

    for attempt in range(max_attempts):
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempt + 1} attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
    else:
        print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")

