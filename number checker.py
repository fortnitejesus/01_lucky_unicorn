#function goes here

def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10"

    valid = False
    while not valid:
        try:
            #ask the question
            response = int(input(question))
            #if the mount is too high or too low give
            if response >= low and response <= high:
                print("you have asked to play with ${}".format(response))
            else:
                print(error)

        except ValueError:
            print(error)


# main routine goes here
how_much =""
how_much = num_check("How much would you like to play with", 1, 10)
ask_money =""
ask_money = num_check("How much will you give me?", 50, 1000)
