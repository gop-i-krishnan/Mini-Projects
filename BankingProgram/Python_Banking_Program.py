#PYTHON BANKING PROGRAM
from random import choice


def show_balance(balance):
    print('*************************')
    print(f'Your current balance is ₹{balance:0.2f}😎')
    print('*************************')

def withdraw(balance):
    print('*************************')
    amount=float(input('Enter an amount to withdraw: ₹'))
    print('*************************')

    if amount>balance:
        print('*************************')
        print('  Insufficient balance!🥲  ')
        print('*************************')
        return 0
    elif amount<0:
        print('**************************************')
        print('Withdraw amount must be greater than 0❌')
        print('**************************************')
        return 0
    else:
        return amount

def deposit(balance):
    print('*************************')
    amount= float(input('Enter an amount to deposit: ₹'))
    print('*************************')

    if amount<0:
        print('*************************')
        print("That's not a valid amount❌")
        print('*************************')
        return 0
    else:
        return amount

def main():
    balance=0
    is_running=True

    while is_running:
        print('\n****************************\nWelcome to our Bank💰💰💰\n****************************\n1.Balance Enquiry\n2.Withdraw\n3.Deposit\n4.Exit\n*************************')

        choice=input('\nPlease Enter your choice(1-4): ')

        if choice=='1':
            show_balance(balance)
        elif choice=='2':
            balance-=withdraw(balance)
            print(f'Your new balance is {balance}')
        elif choice=='3':
            balance+=deposit(balance)
            print(f'Your new balance is {balance}')
        elif choice=='4':
            is_running=False
        else:
            print('You choice is invalid \n')

    print('*************************')
    print('Thank you! Have a nice day🙏')
    print('*************************')

if __name__=='__main__':
    main()