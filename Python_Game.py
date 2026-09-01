#python game


import winsound

# WIN sound
def win_sound():
    winsound.Beep(1000, 300)
    winsound.Beep(1200, 300)
    winsound.Beep(1500, 500)


# LOSE sound
def lose_sound():
    winsound.Beep(500, 400)
    winsound.Beep(350, 500)
    winsound.Beep(200, 700)

#this start function will call the get number function as seen
#on bottom
def start(nice=0,mean=0,name=""):
    #get user's name
    name = describe_game(name)
    nice_mean(nice,mean,name)

def describe_game(name):
    """
        check if this is a new game or not,
        If it is new, get the user's name,
        If it is not a new game, thank the player for
        playing again and continue with the game
    """
    #meaning, if we do not already have this user's name,
    #then they are a new player and we need to get their name
    if name != "":  #quotation mark means not equal but we no its empty
      print("n\Thank you for playing again, ()!".format(name)) #so this wont fire off
    else: #since the above is empty thats why we use the else statement here
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, ()!".format(name))
                    print("\nIn this gameyou will be greeted \nby several people. \nyou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
                    
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approches you a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: :").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
            if pick == "m":
                print("\nThe stranger glares at you \nmenacingly and storms off...")
                mean = (mean + 1)
                stop = False
    score(nice,mean,name) # pass the 3 vairbles to the score


def show_score(nice,mean,name):
    print("\n{}, your current total: \n{}, Nice and {}, Mean)".format(nice,mean,name))


def score (nice,mean,name):
    # score function is being passed the values stored within the 3 vaiable
    if nice > 2: # if condition is valid, call lose function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:         # else, call nice_mean function passing in the variable so it can use them
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    # Substitute the () wildcards with our variable values
    print("\nNice job (), you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter (Y) for 'YES', (N) for 'NO':\n>>> ")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    #Notice I do not reset the name variable as the same user has elected to play again
    start(nice,mean,name)



        

                




if __name__ == "__main__":
    start()
