# Write your code here
# import the random module
import random

account_details = []  # empty list to store generated card number and pin code


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


def check_luhn(card_number):
    last_digital = card_number[-1]
    card_number = card_number[:-1]
    sum_odd = 0
    for x in range(0, 15, 2):
        k = int(card_number[x]) * 2
        if k > 9:
            sum_odd += (k // 10 + k % 10)
        else:
            sum_odd += k
    sum_even = 0
    for y in range(1, 14, 2):
        sum_even += int(card_number[y])
    if last_digital == str((sum_odd + sum_even) % 10) == "0":
        return True
    elif last_digital == str(10 - (sum_odd + sum_even) % 10):
        return True
    return False


def account_generator():
    # generate uniques card_number
    card_number = str(random.randint(4000000000000000, 4000009999999999))
    # check card_number against the luhn formula
    if not check_luhn(card_number):
        account_generator()

    print('Your card has been created')
    # display uniques card_number details as generated
    print('Your card number:')
    print(card_number)

    pin_code = ''.join(str(random.randint(0, 9)) for _ in range(4))
    # display uniques pin_code as generated
    print('Your card PIN:')
    print(pin_code)
    
    # append the generated details to the account_details list
    account_details.append(card_number)
    account_details.append(pin_code)

    main_menu()


def login():
    user_account_details = []  # empty list to store user credentials input

    print('Enter your card number:')
    # user to input the card_number
    user_card_number = input(" ")
    # append the user-given card_number to the user_account_details
    user_account_details.append(user_card_number)

    print('Enter your PIN:')
    # user to input pin_code
    user_pin = input(" ")
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
