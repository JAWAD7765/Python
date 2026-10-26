n = int(input("Enter the limit N: "))

first = 0
second = 1

while first < n:
    print(first)

    next_number = first + second
    first = second
    second = next_number