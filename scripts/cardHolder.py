class CardHolder :

    def __init__(self,name,card_number,pin,balance):
        self.name = name
        self.cardNumber = card_number
        self.pin = pin
        self.balance = balance


    #getter functions

    def get_card_number(self):
        return (self.card_number)
    
    def get_pin (self):
        return(self.pin)
    
    def get_balance(self):
        return(self.balance)
    
    #setter functions

    def set_card_number(self, newVal):
        self.card_number = newVal
    
    def set_pin (self, newVal):
        self.pin = newVal
    
    def set_balance(self, newVal):
        self.balance = newVal
