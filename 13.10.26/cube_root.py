
while True:
    given_number = int(input("Enter an integer: "))
    guess_number = 0

    if given_number >= 0:
        while guess_number * guess_number * guess_number < given_number:
            guess_number = guess_number + 1
    else:
        while guess_number * guess_number * guess_number > given_number:
            guess_number = guess_number - 1

    print("The cube root is", guess_number)
