import random

number = random.randint(1, 100)

guess = None
while guess != number:
    print("Guess the number:")
    guess = int(input())

    if guess < number:
        print("My number is more")
    elif guess > number:
        print("My number is less")
    else:
        print("Congratulations! Number guessed!")