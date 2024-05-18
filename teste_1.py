import random

def number_guesser():
    print("Guess a number between 1 and 100. I'll tell you if the number I chose is lower or higher than your guess.")
    rand_number = random.randint(1,100)
    guess = None
    while rand_number!= guess:
        s = input("Your guess: ")
        guess = int(s)
        if guess < rand_number:
            print("Higher")
        elif guess > rand_number:
            print("Lower")
    print("You guessed it!")

if __name__ == '__main__':
    number_guesser()