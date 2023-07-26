from games import diceroll,quiz,mulquiz,numguess

class exception1(Exception):
    def __init__(self, *args):
        super().__init__(*args)

f =open("Record.txt","+at")

a = True
while a == True:
    print("This is a menu driven progrsm")
    print("Games: \n1)Addition quiz \n2)Multiplication quiz \n3)Number guess \n4)Rock paper scissor \n5)Roll dice")
    num = int(input("Enter your choice in num :"))
    if num == 1:
        quiz.addition_quiz()
        f.write("Addition quiz \n")

    elif num == 2:
        mulquiz.multiplication_quiz()
        f.write("Multiplication quiz \n")

    elif num == 3:
        numguess.num_guess()
        f.write("Number guess \n")


    elif num == 5:
        diceroll.dice_rolling_simulator()
        f.write("Roll dice \n")

    else :
        try:
            raise exception1("Invalid choice!")
        except exception1 as e:
            print(e.args[0])
        break
