from cardHolder import  CardHolder

def service_options():
    print("Which service do you want. ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Quit")

def deposit(cardholder):
    amount = input("How much would you like to deposit? ksh.")
    initial_balance = cardholder.get_balance()
    balance = int(amount) + int(initial_balance)
    return balance

def withdraw(cardholder):
    while True:
        amount = input("How much would you like to withdraw? Ksh ")
        initial_balance = cardholder.get_balance()
        if amount > initial_balance :
            print("Insufficient amount in your account. Please try again")
        else:
            balance = int(initial_balance) - int(amount)
            break
    
    return balance

def check_balance(cardholder):
    balance = cardholder.get_balance()

    print(f"Your current balance is {balance}")


def verify(cardHolders):
    card_number = input("Please enter your card number: ").strip()
    for  card_holder_data in cardHolders:
        data_parts = card_holder_data.strip().split(",")
        if len(data_parts) < 4 :
            continue
        name, card_holder_number, pin, balance = data_parts[0].strip(), data_parts[1].strip(), data_parts[2].strip(), data_parts[3].strip()
      
        if card_number == card_holder_number and input("Please enter your PIN: ").strip() == pin:
            print(f"Card number verified.user found {name}")
            return CardHolder(name, card_holder_number, pin, balance)
    else:
        print("Invalid card number or PIN")
        return None

def main():

    holders = """
    njuguna samwel, 2134567937894, 3456, 100
    daniel Muthini, 3543494545656, 2819, 200
    dennis Mutara,  2344589387473, 1780, 400
    """
    cardHolders = [line.strip() for line in holders.splitlines() if line.strip()]
    print(cardHolders)

    user = verify(cardHolders)
    if user is None:
        print("Authentication failed")
        return
    print("Welcome to the ATM\n`")      

    while True:
        
        service_options()
        option = input("Please enter (1-4) ")
        if option.isdigit():
            option = int(option)   
            if 1<= option <= 4:
                if option ==1:
                    balance = deposit(user)
                    user.set_balance(balance)
                    print(f"\nYour new balance is {balance}\n")
                elif option == 2:
                    balance = withdraw(user)
                    user.set_balance(balance)
                    print(f"\nYour new balance is {balance}\n")
                elif option == 3:
                    check_balance(user)
                elif option == 4 :
                    print("\nThank you for using our ATM. Goodbye")
                    break
                else:
                    print("Your choice can only be in the range (1-4)")
        else:
            print("Please make a valid choice!!!")
        


main()


  



