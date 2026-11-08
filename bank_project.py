class Account:
  def __init__(self,username,password,balance=0.):
    self.username = username
    self.password = password
    self.balance = balance
    self.get_mini_statement = []

    def deposit(self,amount):
      self.balance += amount
      print(f"\nAmount deposited:{amount}\nTotal Balance:{self .balance}")

      def withdraw(self,amount):
        if self.balance >= amount:
         self.balance -= amount
         print(f"\nAmount withdrawn:{amount}\nRemaing Balance:{self.balance}")
        else:
         print("Insufficient balance")
      def get_mini_statement(self): 
        print("mini statement:")
      print(f"username:{self.username}")
      print(f"current balance:{self.balance}")

  class BankingSystem:
    def __init__(self):
      self.accounts = {}

      def create_account(self,username,password):
        if username in self.accounts:
          print("username already exists")
        else:
          self.accounts[username] = Account(username,password)
          print("\n Account created successfully")
          print("-------Welcome to python Bank-----")

      def login(self,username,password):
        if username in self.accounts:
            self.accounts[username]
        if account.password == password:
           print("login sucess ....")
           return account
        else:
            print("Invaild password")
        return None


  bank  = BankingSystem() 

  while True:
    print("\n")
    print("1. create account")
    print("2. login")
    print("3.Exit")
    choice = input("enter your choice(1-3):")

    if choice == '1':
      username = input("enter username:")
      password = input("enter password:")
      bank.create_account(username,password)
    elif choice =='2':
      username = input("enter username:")
      password = input("enter password:")
      account = bank.login(username,password)
      if account is not None:
        while True:
          print("\n-----welcome to PYTHON bank-----")
          print("1. Deposit")
          print("2. withdraw")
          print("3. check balance")
          print("4. ministatement")
          print("5.logout\n")
          choice  = input("enter your choice(1-5):")

          if choice == '1':
            amount = int(input("enter amount to deposit:"))
            account.deposit(amount)
          elif choice == '2':
            amount = int(input("enter amount to withdraw:"))
            account.withdraw(amount)
          elif choice == '3':
            print(f"current balance:{account.get_balance()}")

          elif choice =='4':
            account.get_mini_statement()

          elif choice =='5':
            print("\n----THANK YOU VISIT AGAIN")
            break
          else:
            print("Invaild choice")
      elif choice == '3':
        print("\n----- thank you-----")
        break
      else:
        print("invaild choice")

        import random
        obj = random.randint(127000000,127999999)
        acc_number = []
        acc_number.append(obj)
        print(obj)
        print(acc_number)
