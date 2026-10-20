while True:
    num = int(input("Enter a number: "))

total_sum = 0
i = 1
while i <= num:
    total_sum = total_sum + i
    i = i + 1
    sum_gauss = int(num * (num + 1) / 2)
if total_sum == sum_gauss:
    print("My running sum code works correctly")
else:
    print("My running sum code failed badly")