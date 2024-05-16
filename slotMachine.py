
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
            "🍒":2 ,
            '🍊':4, 
            '🍋':6, 
            '🍉':8
            }

symbol_values = {
            "🍒":5,
            '🍊':4, 
            '🍋':3, 
            '🍉':2 
}

def check_winnings(columns,lines,bet,values):
    winnings =0
    winning_lines =[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        
        else:
            winnings =+ values[symbol] *bet
            winning_lines.append(line +1)

    return winnings, winning_lines


def get_slot_machine_spin (rows,cols,symbols):
    all_symbols = []

    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = [] 
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
         
    return columns

def print_slot_machine(columns):
     for row in range(len(columns[0])):
         for i, column in enumerate(columns):
             if 1 != len(columns)-1:
                 print(column[row], end= "| ")
             else:
                 print(column[row], end="")

         print()




def deposit ():
     while True:
        amount = input("How much would you like to deposit? $")
   
        if amount.isdigit():
            amount = int(amount)
            
            if amount > 0:
                print(f"You have deposited ${amount} into your account")
                return amount
            else:
                print("Invalid amount")
        else:
            print("Please enter a valid amount")
        return amount
       


def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to play?(1-3) ")
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines <=3:
                return lines
            else:
                print("Invalid number of lines")
        else:
            print("Please enter a valid number of lines")
            return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            
            if MIN_BET <=amount <= MAX_BET:
                return amount
            else:
                print(f"Invalid bet amount. Your betting amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please enter a valid number")
        
def spin(balance):
    lines = get_number_of_lines()
    while True: 

        bet = get_bet()
        total_bet = bet*lines

        if total_bet > balance:
            print(f"Sorry but you are short on cash. Your balance is{balance}")
        
        else:
            break
    print(f"You made a bet of ${bet} on {lines} lines.Total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS,COLS, symbol_count)

    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}" )
    print(f"You won on lines", *winning_lines)

    return winnings - total_bet



def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play(q to quit)")
        if answer == "q":
            break
        balance +=spin(balance)

main()
