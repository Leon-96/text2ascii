import pyfiglet

from art import logo

import webbrowser

import pandas as pd

import os

import pyperclip


def textconverter():
    os.system('cls')

    print(logo, "\n")
    print("                  Welcome To Text2Ascii \n              ")
    text = input('''>>>>>>>>Enter your Text : \n''')
    choice = input('''>>>>>>>>Would You like to see a list of available fonts? Type 'y' to view available font type 'n'
to continue conversion\n''')
    if choice == 'y':
        print('Here is a list of available fonts')
        pd.set_option("display.max_rows", None, "display.max_columns", None)

        print(pd.Series(pyfiglet.FigletFont.getFonts()))

        choice1 = input('''Would you like to view examples?Type 'y' to view examples type 'n'
to continue conversion \n''')

        if choice1 == 'y':
            print("Opening Browser and taking you to examples of fonts available\n")
            webbrowser.open("www.figlet.org/examples.html")

            print('Now Enter the font name\n')

            font1 = input("Enter the font name : \n")

            print("#Converting your text to ascii art :\n")

            for i in range(1, 5):
                i = i + 1
                print(i * ".")
                print("\n")

            print("Here is your art : \n")

            print(pyfiglet.figlet_format(text, font=font1))
            print("\n")

        if choice1 == 'n':
            print('Now Enter the font name\n')

            font1 = input("Enter the font name : \n")



            print("#Converting your text to ascii art \n")

            for i in range(0, 5):
                i = i + 1
                print(i * ".")
                print("\n")
            print("Here is your art : \n")

            print(pyfiglet.figlet_format(text, font=font1))
            print("\n")

    if choice == 'n':
        print('Now Enter the font name\n')

        font1 = input("Enter the font name : \n")

        print("###Converting your text to ascii art :\n")

        for i in range(1, 5):
            i = i + 1
            print(i * ".")
            print("\n")

        print("###Here is your art : \n")

        print(pyfiglet.figlet_format(text, font=font1))

        print("\n")

    choice2 = input('''Would you like to copy the art to clipboard?Type 'y' to copy : \n''')

    if choice2 == 'y':
        pyperclip.copy(f"{str(pyfiglet.figlet_format(text, font=font1))}")
        print('\n')
        print('Your text has been copied!')

    choice3 = input('''Would you like to go again? Type 'y' to go again type 'n'
to exit\n''')

    if choice3 == 'y':
        textconverter()
    if choice3 == 'n':
        os.system('cls')

        exit()


textconverter()
