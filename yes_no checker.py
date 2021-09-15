
show_instructions = ""
while show_instructions != "xxx":
    # ask the user if they played before
    show_instructions = input("have you played this game before?").lower().strip()

        #if they say yes, output 'program continues'
        #if they say no, output 'display instructions'
        #if the answer is invalid, print an error.

    if show_instructions == "yes" or show_instructions =="y":
        print ("program continues")

    elif show_instructions == "no" or show_instructions =="n":
        print ("display instructions")

    else:
        print("Please enter yes or no")
