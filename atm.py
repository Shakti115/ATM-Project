import time
import sys

print("Welcome to X Bank!")
print("Please choose and type a 4-digit pincode:")
while True:
  pin_code = input()
  
  if len(pin_code) == 4:
    while True:
      print("Please confirm your pincode:")
      confirmed_pincode = input()
      if pin_code == confirmed_pincode:
        time.sleep(1.5)
        print("Welcome to your Bank Account!")
        account_balance = 5000
        print("You can now do any of the following: Withdraw(1), Deposit(2), Check Balance(3), Exit(4)")
        choice = input()
        if choice == "1":
          time.sleep(1)
          while True:
            print("How much would you like to withdraw?")
            withdrawal_ammount = float(input())
            if withdrawal_ammount < account_balance:
              time.sleep(1)
              account_balance = account_balance - withdrawal_ammount
              print("Withdrawal success! Your new account balance is:", account_balance, "Thank you for using X Bank!")
              sys.exit()
            if withdrawal_ammount > account_balance:
              print("You do not have enough money in your account to withdraw this ammount.")
        elif choice == "2":
          time.sleep(1)
          while True:
            print("How much would you like to deposit?")
            deposit_ammount = float(input())
            if deposit_ammount < 10000:
              time.sleep(1)
              account_balance = account_balance + deposit_ammount
              print("Your new balance is:", account_balance, "Thank you for using X Bank!")
              sys.exit()
            if deposit_ammount > 10000:
              print("You cannot deposit more than 10000 at a time.")
        elif choice == "3":
          time.sleep(1)
          print("Your account balance is:", account_balance, "Thank you for using X bank!")
          sys.exit()
        elif choice == "4":
          time.sleep(1)
          print("Thank you for using X Bank!")
          sys.exit()
      elif confirmed_pincode != pin_code:
        print("Your pincodes do not match, please try again!")
  elif len(pin_code) != 4:
      print("You did not type a 4-digit pincode, please try again!")
