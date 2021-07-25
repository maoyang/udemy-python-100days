# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    print("Welcome to Python Pizza Deliveries")
    size = input("What size pizza do you want? S/M/L")
    add_pepperoni = input("Do you want pepperoni? Y/N")
    extra_cheese = input("Do you want extra cheese? Y/N")
    price = 0

    if size == "S":
        price = 15
    elif size == "M":
        price = 20
    elif size == "L":
        price = 25

    if add_pepperoni == "Y":
        if size == "S":
            price += 2
        else:
            price += 3
    if extra_cheese == "Y":
        price += 1

    print(f"Total price : {price}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
