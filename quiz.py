import random

def addition_quiz():
    print("Welcome to the Addition Quiz!")
    score = 0

    for _ in range(5):
        num1 = random.randint(2, 200)
        num2 = random.randint(1, 200)
        correct_answer = num1 + num2

        user_answer = int(input(f"What is {num1} + {num2}? "))

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

    print(f"Your final score is: {score}/5")


