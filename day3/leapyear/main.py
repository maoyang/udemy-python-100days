# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# 閏年 = 可以被 4 整除但是不可以被 100 整除, 如果可以被 100 整除也要同時被 400 整除

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def is_leap_year():
    year = int(input("Which year you want to check?"))
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            print("this year is leap year")
        elif year % 100 != 0:
            print("this year is leap year")
        else:
            print("this year is not leap year")
    else:
        print("this year is not leap year")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    is_leap_year()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
