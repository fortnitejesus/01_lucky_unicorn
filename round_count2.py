import random

# set balance for testing purposes
balance = 5

rounds_played = 0

play_again = input("press <enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print("*** round #{} ***".format(rounds_played))

for item in range(0, 10):
    chosen_num = random.randint(1, 100)
#testing loop to generate 20 tokens
for item in range (0,10):
    chosen_num = random.randint(1, 100)

#adjust balance
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

print("*** final balance ***", balance)

if balance < 1:
    play_again = "xxx"
    print("*** sorry you have run out of money uwu ***")
else:
    play_again = input("press enter to play again or 'xxx' to quit")
