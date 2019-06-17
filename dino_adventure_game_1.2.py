#############
# Dev: Jeremy Cabrera #
# Project: Dino Adventure Game #
# Assignment:  Udactiy Nanodegree #
# Date: June 2019 #
#############


import random
import time


####################
# Variables #
####################

posResponse = ['yes', 'y', 'yup', 'ok', 'sure', 'fine', 'affirmative']
negResponse = ['nope', 'no', 'n', 'negative']
leftDir = ['left', 'l', 'not right']
rightDir = ['right', 'r', 'not left']
digResponse = ['dig', 'd']
passResponse = ['pass', 'p']

normalSleepTime = 4


greetings = ["Good Day!", "Good Morning!", "Good Afternoon!"]


#############
# Functions #
#############

def greeting():
    print(random.choice(greetings))


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def cleanResponse(response):
    return response.lower().strip()


def gameIntro():
    greeting()
    print()
    print_pause("Welcome to the text-based game Dinosaur Discovery! \n")
    print_pause("You are the Team Leader of the Dinosaur Coders Expedition \n")
    print_pause("Team, aka DCET, and you get to choose the riverbed in \n")
    print_pause("which you and your team would like to dig. Your choice  \n")
    print_pause("could have life changing results for you and your team,  \n")
    print_pause("or it could be the end of your paleontology career as a \n")
    print_pause("Team Leader!")
    print()
    choosePlay()


def choosePlay():
    play = input("Would you like to play Dinosaur Discovery?")
    print()
    if cleanResponse(play) in posResponse:
        print_pause("Great! Let's get started...")
        print()
        chooseAction()

    elif cleanResponse(play) in negResponse:
        print_pause("I'm sorry to hear that. You are terrible. Goodbye")
        exit()

    else:
        print_pause("""I'm sorry, I didn't understand your response. Could you \n
please try again?""")
        time.sleep(normalSleepTime)
        choosePlay()


def chooseAction():
    print_pause("""You have come upon the end of the dry river bed \n
where it splits in two directions.""")
    print()
    answer = input("What direction would you like to go? (left or right):")
    print()
    if cleanResponse(answer) in leftDir:
        print("Great decision!")
        print()
        digOrPass()
    elif cleanResponse(answer) in rightDir:
        print("Wrong choice.  Sorry game over!")
        playAgain()
    elif cleanResponse(answer) == 'center':
        print("Awww, not so fast. Try again")
        time.sleep(normalSleepTime)
        chooseAction()
    else:
        print("""Sorry, I didn't understand the response. Please choose left\n
or right""")
        time.sleep(normalSleepTime)
        chooseAction()


def digOrPass():
    print("""You've located an unusual rock area. You can either choose to \n
dig at the site and see what you find, or you can pass by like a \n
wimp. Your choice here Mr. Team Leader!""")
    print()
    choice = input("What will you choose?")
    print()
    if cleanResponse(choice) in digResponse:
        print("""Congratulations, you've WON!.  You just \n
unearthed a Spinosaurus!""")
        time.sleep(1)
        playAgain()
    elif cleanResponse(choice) in passResponse:
        print("Oh jeees, wimpin' out again like you always do. YOU LOSE!")
        time.sleep(normalSleepTime)
        playAgain()
    else:
        print("Huh? C'mon now...it's dig or pass! Try again.")
        time.sleep(normalSleepTime)
        digOrPass()


def playAgain():
    answer = input("Would you like to play again? (Y or N):")
    print()
    if cleanResponse(answer) in posResponse:
        print("Great!")
        gameIntro()
    elif cleanResponse(answer) in negResponse:
        print("Ok. Have a great day!")
        time.sleep(normalSleepTime)
        exit()
    else:
        print("It's a simple Yes or No question. Why you gotta be like that?")
        time.sleep(normalSleepTime)
        playAgain()

gameIntro()
############
# Adventure Gameplay #
############
