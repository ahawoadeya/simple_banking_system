import random
# import sqlite3 python module
import sqlite3

# create a connection object
db = sqlite3.connect('card.s3db')
# create a cursor object
sql = db.cursor()
sql.execute('''CREATE TABLE IF NOT EXISTS card
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            number TEXT,
            pin TEXT,
            balance INTEGER DEFAULT 0)''')
db.commit()


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
        sql.close()
        exit()


# luhn algorithm to check validity of credit card numbers.
def check_luhn(card_number):
    last_digit = card_number[-1]
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
    if last_digit == str((sum_odd + sum_even) % 10) == '0':
        return True
    elif last_digit == str(10 - (sum_odd + sum_even) % 10):
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

    default_balance = 0
    sql.execute(f'INSERT INTO card (number, pin, balance) VALUES ({card_number}, {pin_code}, {default_balance})')
    db.commit()

    main_menu()


def check_account(card_number):
    # sql.execute('SELECT number FROM card')
    list_cards = [x[0] for x in sql.execute("SELECT number FROM card")]
    if card_number in list_cards:
        return True
    return False


def check_pin(card_number, pin_code):
    sql.execute(f'SELECT pin FROM card WHERE number ={card_number}')
    pin = ''.join(sql.fetchone())
    if pin == pin_code:
        return True
    return False


def login():
    print('Enter your card number: ')
    card_number = input(' ')
    print('Enter your PIN: ')
    pin_code = input(' ')

    if check_account(card_number):
        if check_pin(card_number, pin_code):
            print('You have successfully logged in!')
            login_menu(card_number)
        pass
    print('Wrong card number or PIN!')

    main_menu()


def check_balance(card_number):
    sql.execute(f'SELECT balance FROM card WHERE  number={card_number}')
    money = sql.fetchone()
    print(f'Balance: {money}')

    login_menu(card_number)


def add_income(card_number):
    print('Enter income: ')
    income = int(input(' '))
    sql.execute(f'UPDATE card SET balance=balance+{income} WHERE number={card_number}')
    db.commit()
    print('Income was added!')

    login_menu(card_number)


def do_transfer(card_number):
    print('Transfer')
    print('Enter card number: ')
    to_card = input(' ')
    if card_number == to_card:
        print('You can\'t transfer money to the same account!')
        login_menu(card_number)
    elif not check_luhn(to_card):
        print('Probably you made mistake in the card number. Please try again!')
        login_menu(card_number)
    elif not check_account(to_card):
        print('Such a card does not exist.')
        login_menu(card_number)

    transfer_money(card_number, to_card)


def transfer_money(from_card, to_card):
    print('Enter how much money you want to transfer: ')
    money = int(input(' '))
    sql.execute(f'SELECT balance FROM card WHERE number={from_card}')
    money_from_card = [int(i[0]) for i in sql.fetchall()]
    if money > money_from_card[0]:
        print('Not enough money!')
        login_menu(from_card)
    sql.execute(f"UPDATE card SET balance=balance+{money} WHERE number={to_card}")
    sql.execute(f"UPDATE card SET balance=balance-{money} WHERE number={from_card}")
    db.commit()
    print('Success!')
    login_menu(from_card)


def close_account(card_number):
    sql.execute(f'DELETE FROM card WHERE number={card_number}')
    db.commit()

    main_menu()


def login_menu(card_number):
    print('1. Balance')
    print('2. Add income')
    print('3. Do transfer')
    print('4. Close account')
    print('5. Log out')
    print('0. Exit')

    user_option = input()

    if user_option == '1':
        check_balance(card_number)
    elif user_option == '2':
        add_income(card_number)
    elif user_option == '3':
        do_transfer(card_number)
    elif user_option == '4':
        close_account(card_number)
    elif user_option == '5':
        print('You have successfully logged out!')
        main_menu()
    sql.close()
    exit()


main_menu()
