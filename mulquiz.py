import random

def multiplication_quiz():
    print("Welcome to the Multiplication Quiz!")
    score = 0

    for _ in range(5):
        num1 = random.randint(2, 15)
        num2 = random.randint(2, 9)
        correct_answer = num1 * num2

        user_answer = int(input(f"What is {num1} x {num2}? "))

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

    print(f"Your final score is: {score}/5")
