# Write your code here
# import the random module
import random

account_details = []     # empty list to store generated card number and pin code


def main_menu():
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')

    user_option = input(" ")

    if user_option == '1':
        account_generator()
    elif user_option == '2':
        login()
    else:
        print('Bye!')
        exit()


def generate_card_number():
    
    # generate unique card_number
    card_number = random.sample(range(4000000000000000, 4000009999999999), 1) 
    print(*card_number)
    
    # append the generated card_number to the account_details list
    account_details.append(*card_number)


def generate_pin_code():
    # generate unique pin
    pin_code = random.sample(range(0000, 9999), 1)
    print(*pin_code)
    
    # append the generated pin_code to the account_details list
    account_details.append(*pin_code)


def account_generator():
    print('Your card has been created')
    
    # display uniques card_number details as generated
    print('Your card number:')
    generate_card_number()
    
    # display uniques pin_code as generated
    print('Your card PIN:')
    generate_pin_code()

    main_menu()


def login():
    user_account_details = []    # empty list to store user credentials input

    print('Enter your card number:')
    # user to input the card_number
    user_card_number = int(input(" "))
    # append the user-given card_number to the user_account_details
    user_account_details.append(user_card_number)

    print('Enter your PIN:')
    # user to input pin_code
    user_pin = int(input(" "))
    # append the user-given pin_code to the user_account_details
    user_account_details.append(user_pin)
    
    # compare the generated details with the user given details
    # user should login successfully only if the details match successfully
    if user_account_details == account_details:
        print('You have successfully logged in!')
        login_menu()
    else:
        print('Wrong card number or PIN!')
        main_menu()


def login_menu():
    print('1. Balance')
    print('2. Log out')
    print('0. Exit')

    user_option = input()

    if user_option == '1':
        print('Balance: 0')
        login_menu()
    elif user_option == '2':
        print('You have successfully logged out!')
        main_menu()
    else:
        exit()


main_menu()
