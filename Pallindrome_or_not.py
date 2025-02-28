String = input("Enter a string: ").upper()

if String[0:len(String)] == String[::-1]:
    print("The string is pallindrome")
else:
    print("the string is not a pallindrome")


