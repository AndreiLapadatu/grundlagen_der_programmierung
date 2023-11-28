import random


def player():
    while True:
        user = input("Chose one! rock, paper, scissors: ").lower().strip()
        if user in ('rock', 'paper', 'scissors'):
            return user
        else:
            print("your choice does not exist")


def robot():
    choice = ['rock', 'paper', 'scissors']
    cpu = random.choice(choice)
    return cpu
