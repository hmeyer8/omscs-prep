filename = 'pi_mil.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    birthday = input("Enter your birthday, in the form mmddyy: ")
    if birthday in lines:
        print("Your birthday appears in the first million digits of pi!")
    else:
        print("Your birthday does not appear in the first million digits of pi.")