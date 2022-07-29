from turtle import update
from student import find, register, update
screen = """
    welcome to well to do student page.
    
    Choose an option below to proceed:
    -Enter R to register student
    -Enter F to find student
    -Enter U to update existing student
    -Enter Q to leave the page

"""
print(screen)

choice = input("Enter a value to continue: ").lower()

while choice != "q":
    if choice == "r":
        register()

    elif choice == "f":
        find()

    elif choice == "u":

        update
        
    choice = input("Enter a value to continue: ")


print("Bye")