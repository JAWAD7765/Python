letter = input("Enter one English letter: ")
letter = letter.lower()

if len(letter) != 1 or not letter.isalpha():
    print("Please enter one English letter")
elif letter in "aeiou":
    print("It is a vowel")
else:
    print("It is a consonant")
