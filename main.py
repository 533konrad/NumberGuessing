
#TODO: counting tries and errors

def NumberGuessing():

    from random import random

    secret = int(random()*100)
    print("Secret number is: ", secret)
    guess = int(input("Can you guess secret number? Remember, you have only 7 trials. What's your guess? "))
    count = 0

    while guess != secret and count < 7:
        if guess < secret:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        guess = int(input("What's your guess? "))
    #    guess = int(guess)
        count+=1
        print(count)
    return("Correct! You WON!")

print(NumberGuessing())
