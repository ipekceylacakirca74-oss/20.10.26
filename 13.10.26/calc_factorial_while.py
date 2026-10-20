# calc_factorial_while.py

num = int(input("Enter a number: "))

factorial = 1
i = 1

# Loop until i is greater than num
while i <= num:
    factorial = factorial * i
    i = i + 1  # Don't forget to increase i, otherwise it's an infinite loop!

print("The factorial is:", factorial)