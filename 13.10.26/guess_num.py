from secret_number import secretNum

attempts = 0

while attempts < 5:
5
    guess = int(input("Guess the secret number: "))
    attempts += 1

    if guess < secretNum:
        print("Too low!")
    elif guess > secretNum:
        print("Too high!")
    else:
        print("You guessed it!")
        break
if attempts == 5 and guess != secretNum:
    while True:
        print("Oh! Noooooo...")