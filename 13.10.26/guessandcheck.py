while True:
    given_number = int(input("Enter a number: "))
    if given_number < 0:
        print("Please enter a non-negative number.")
    elif given_number == 0:
        print("The square root is 0")

    else:
        guess_number = 1

        while   guess_number * guess_number < given_number:
            guess_number = guess_number + 1

        if guess_number * guess_number == given_number:
            print("The square root is", guess_number)

        else:
            print("The number is not a perfect square.")