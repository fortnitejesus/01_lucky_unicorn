# Imports
import random

# Functions
def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10"

    valid = False
    while not valid:
        try:
            #ask the question
            response = int(input(question))
            #if the mount is too high or too low give
            if response >= low and response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


rounds_played = 0

print("Welcome to Lucky Unicorn")

show_instructions = ""
while show_instructions != "yes":
    show_instructions = input("have you played this game before?").lower().strip()

    if show_instructions == "yes" or show_instructions =="y":
        break
    elif show_instructions == "no" or show_instructions =="n":
        print("*** how to play ***")
        print("Step 1: Insert amount you would like to play with")
        print("Step 2: Press enter to play")
        print("Step 3: Play until you run out of money or till you want to stop")
    else:
        print("Please enter yes or no")

how_much = num_check("How much would you like to play with", 1, 10)
balance = how_much

play_again = input("press <enter> to play...").lower()
while play_again == "":

    rounds_played += 1
    chosen_num = random.randint(1, 100)

    if 1 <= chosen_num <= 5:
     chosen = "unicorn"
     balance += 4
    elif 6 <= chosen_num <= 36:
     chosen = "donkey"
     balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
        else:
            chosen = "zebra"
        balance -= 0.5

    print("You got a {}. Your balance is ${:.2f}".format(chosen,balance))

    if balance < 1:
        play_again = "xxx"
        print("*** sorry you have run out of money ***")
    else:
        play_again = input("Press enter to play again or 'xxx' to quit")

print("starting balance: ${:.2f}".format(how_much))
print("final balance: ${:.2f}".format(balance))

if balance <1:
    print("Thank you for playing lucky unicorn")
