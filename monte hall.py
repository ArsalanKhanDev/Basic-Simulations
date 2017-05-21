import random

def monty_hall():

    #-----setup ----#

    prizes = ["Car" , "Goat" , "Goat"]
    random.shuffle(prizes)

    #----person chooses at random----#

    choose_index = random.randint(0,2)

    ##-------host reveals a goat------#

    while True:
        goat_gate = random.randint(0, 2)
        if prizes[goat_gate] == "Goat" and goat_gate != choose_index:
            break

    ##------person switches -------##

    while True  :
        switch_choise = random.randint(0, 2)
        if (switch_choise!= choose_index) & (switch_choise!= goat_gate):
            break

    ## -- check if won---#

    if prizes[switch_choise] == "Car":
        return True



win = 0
games = int(input("enter the number of times you want to play : "))

for times in range(games):
    if monty_hall() == True :
        win += 1

print("percentage of wins : " , win * 100/games)