with open("pi_mil.txt", "r") as text_object:
    contents = text_object.read().strip()

# Keep only the digits after "3."
digits = contents.split(".", 1)[1]

birthday = input("Enter your birthday using digits only, no /: ").strip()

if not birthday or not birthday.isdecimal():
    print("Please enter digits only.")
else:
    position = digits.find(birthday)

    if position != -1:
        print(
            "Great Success! Your birthday starts at decimal digit:",
            position + 1
        )
    else:
        print("Your birthday was not found in this file.")

        