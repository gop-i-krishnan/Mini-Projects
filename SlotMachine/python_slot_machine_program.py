import random

def spin_row():
    symbols=['🍇','🍌','🍍','🥭','⭐']

    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print('*************')
    print(' | '.join(row))
    print('*************')


def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍌':
            return bet*3
        elif row[0]=='⭐':
            return bet*4
        elif row[1]=='🥭':
            return bet*5
        elif row[1]=='🍍':
            return bet*10
        elif row[0]=='🍇':
            return bet*20

    return 0

def main():
    balance=100
    print('************************')
    print('Welcome to Python Slots')
    print('Symbol: 🍇 🍌 🍍  🥭 ⭐')
    print('************************')

    while balance>0:
        print(f'\nCurrent balance:  ₹{balance}\n')

        bet=input('Enter your bet amount: ₹')

        if not bet.isdigit():
            print('Please enter a valid digit!')
            continue

        bet=int(bet)
        if bet>balance:
            print('Insufficient balance!')
            continue
        if bet<=0:
            print('Bet must be greater than 0')
            continue

        balance-=bet

        row=spin_row()
        print('\nSpinning...')
        print_row(row)

        payout=get_payout(row,bet)

        if payout>0:
            print(f'You won ₹{payout}')

        else:
            print('Sorry you have lost this round!🥹')

        balance+=payout

        play_again=input('Press enter to play again or type quit to exit: ').strip().lower()
        if play_again =='quit':
            break

    print('\n********************************************')
    print(f'Game over !Your current balance is ₹{balance}')
    print('********************************************\n')


if __name__=='__main__':
    main()

