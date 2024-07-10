import pyttsx3 
from time import sleep

class ATM_Machine:
    def __init__(self,pin,balance=0) -> None:
        self.Pin=pin
        self.BankBalance=balance
        self.Transaction_History=[]
        self.atm = pyttsx3.init('sapi5')
        voices = self.atm.getProperty('voices')
        self.atm.setProperty('voice', voices[1].id)

    def speak(self, text):
        self.atm.say(text)
        self.atm.runAndWait()
        
    def check_Pin (self,pin):
        if(self.Pin==pin):
            return True
        return False
    def change_PinNumber(self,oldPine,newPin):
        if(self.Pin==oldPine):
            self.Pin=newPin
            self.Transaction_History.append("New PIN Number Changed")
            return("New PIN Number changed successfully.")
        else:
            return("Invalid PIN Number")
           
    def deposit_Amount(self,depositAmt):
        if(self.BankBalance<=0):
            print("Sorry, Your Bank balance is very low. Kindly check your bank balance!!")
        else:
            self.BankBalance+=depositAmt
            self.Transaction_History.append(f"Deposit Amount: ${depositAmt}")
            return depositAmt
          
    def withdraw_Amount(self,withdrawAmt):
         if(self.BankBalance<=0):
            print("Sorry, Your Bank balance is very low. Kindly check your bank balance!!")
            
         else:
             if(self.BankBalance>=withdrawAmt):
                self.BankBalance=self.BankBalance-withdrawAmt
                self.Transaction_History.append(f"Withdraw Amount: ${withdrawAmt}")
                return  f" Kindly Take your Withdraw Amount {withdrawAmt}"
             else:
                 return "Sorry, Your Bank balance is very low. Kindly check your bank balance!!"
    def check_bankBalance(self): 
        self.Transaction_History.append(f"Bank Balance Amount: ${self.BankBalance}")
        return self.BankBalance
        
    def check_transaction_history(self):
        return self.Transaction_History     
def Atm_Machine():
    atm=ATM_Machine(1234,1000)
    print("\n************ STATE BANK OF INDIA ***************")
    atm.speak("Welcome to STATE BANK OF INDIA")
    print("Please insert your atm card")
    atm.speak("Please insert your atm card")
    print("\nATM Menu")
    atm.speak("ATM Menu")
    print("1. Balance Inquiry")
    atm.speak("1. Balance Inquiry")
    print("2. Cash Deposit")
    atm.speak("2. Cash Deposit")
    print("3. Cash Withdrawal")
    atm.speak("3. Cash Withdrawal")
    print("4. Change PIN")
    atm.speak("4. Change PIN")
    print("5. Transaction History")
    atm.speak("5. Transaction History")
    print("6. Exit")
    atm.speak("6. Exit")
    while(True):
        atm.speak("Enter your choice: ")
        choice = int(input("Enter your choice: "))
        atm.speak(f"You chose {choice}")

        if(choice==1):
            atm.speak("Please enter your PIN Number: ")
            pin=int(input("Please enter your PIN Number: "))

            if(atm.check_Pin(pin)):
               print(f"Your Bank Balance is: ${atm.check_bankBalance()}")
               atm.speak(f"Your Bank Balance is: ${atm.check_bankBalance()}")
            else:
                print("Invaild PIN Number")
                atm.speak("Invaild PIN Number")

        elif(choice==2):
            atm.speak("Please enter your PIN Number: ")
            pin = int(input("Please enter your PIN Number : "))

            if(atm.check_Pin(pin)):
               atm.speak("Please Enter your Deposit Amount : $")
               depositAmt = int(input("Please Enter your Deposit Amount : $"))
               print(f"Successfully deposit your Amount: ${atm.deposit_Amount(depositAmt)}")
               atm.speak(f"Successfully deposit your Amount: ${atm.deposit_Amount(depositAmt)}")
            else:
                print("Invaild PIN Number")
                atm.speak("Invaild PIN Number")

        elif(choice==3):
            atm.speak("Please enter your PIN Number: ")
            pin = int(input("Please enter your PIN Number : "))
            if(atm.check_Pin(pin)): 
               atm.speak("Please Enter your Withdraw Amount : $")
               withdrawAmt = int(input("Please Enter your Withdraw Amount : $"))
               print("Transaction is being processed...")
               atm.speak("Please, wait the transaction is being processed")
               print(atm.withdraw_Amount(withdrawAmt))
               atm.speak(atm.withdraw_Amount(withdrawAmt))
            else:
                print("Invaild PIN Number")
                atm.speak("Invaild PIN Number")

        elif(choice==4):
            atm.speak("Please enter your Old PIN Number : ")
            Oldpin = int(input("Please enter your Old PIN Number : "))
            if(atm.check_Pin(Oldpin)):
               atm.speak("Please enter your New PIN Number : ")
               newpin = int(input("Please enter your New PIN Number : "))
               print("New PIN Number changed successfully.")
               atm.speak(f"{atm.change_PinNumber(Oldpin,newpin)}")
            else:
                print("Invaild PIN Number")
                atm.speak("Invaild PIN Number")
        elif(choice==5):
            atm.speak("Please enter your PIN Number : ")
            pin = int(input("Please enter your PIN Number : "))
            if(atm.check_Pin(pin)):
              print(f"{atm.check_transaction_history()}")
              atm.speak(f"{atm.check_transaction_history()}")
            else:
                print("Invaild PIN Number")
                atm.speak("Invaild PIN Number")

        elif (choice==6):
            print("Kindly take Your card . Thank you for visiting the ATM.")
            atm.speak("Kindly take Your card . Thank you for visting the ATM.")
            return

        else:
            print("Invalid choice. Please try again.")
            atm.speak("Invalid choice. Please try again.")
        


if __name__== "__main__":
    Atm_Machine()
