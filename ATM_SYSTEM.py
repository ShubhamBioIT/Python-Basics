Balance = 5000000
Pin = 1234
print("HELLO USER , Welcome to ATM TRANSACTION SYSTEM ")
print("Please Choose The Option Below to continue Transaction \n A = Cheack Balance \n B = Deposit Money \n C = Withdraw Money")
Input = input("Choose your option for Transaction : ")
Pin = int(input("Enter your pin (Should be 1234): "))
def cheack_balance():
     while Input == "A" and Pin == 1234:
         print("Your account balance is ",Balance,"Rs")
         break
def Deposit_Money():
    while Input == "B" and Pin == 1234:
        D = float(input("Enter your ammount to deposit: "))
        print("Your ammount",D ,"has been successfully deposited to your  account")
        print("Your current account balance is", Balance + D,"Rs")
        break
def Withdraw_Money():
    while Input == "C" and Pin == 1234:
        E = float(input("Enter your ammount to Withdraw: "))
        print("Your ammount", E ,"has been successfully Withdrawn from your account")
        print("Your current account balance is", Balance - E,"Rs")
        break   
cheack_balance()
Deposit_Money()
Withdraw_Money()
