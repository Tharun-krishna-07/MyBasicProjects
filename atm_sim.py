balance = 10000

while True :
     print("***THARUN ONLINE BANKING SERVICES***")
     print("1. Check bank balance")
     print("2. Deposit")
     print("3. Withdraw")
     print("4. Exit")
     choice = input("Enter your choice : ")
     choice = choice.lower()

     if choice == "check bank balance" or choice == "1":
          print(f"Your bank balance is  ₹{balance}")
          
     elif choice == "depoist" or choice == "2":
          a = int(input("The amount u need to deposit : "))
          balance = balance + a
          print(f"Your bank balance is  ₹{balance}")

     elif choice == "withdraw" or choice == "3":
          b = int(input("Enter it amount you need to withdraw : "))
          if b>balance:
               print("Insufficient funds")
          else:
               balance = balance - b
               print(f"Current balance : ₹{balance}")
     elif choice == "exit" or choice == "4":
          print("Thankyou , pleasure to have business with you")
          break

               

    
          
     
