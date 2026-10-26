number = int(input("Enter a number: "))

if number < 0:
    print("Please enter a non-negative number")
else:
    while number >= 0:
        print(number)
        number = number - 1