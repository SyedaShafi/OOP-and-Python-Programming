class Bank:
    users = []
    admins = []
    loan_feature = True
    bank_balance = 0
    transaction_history = {}
    id = 11

    def cal_bank_balance():
        for user in Bank.users:
            Bank.bank_balance+=user.balance


class Admin(Bank):
    def __init__(self, username, email, password) -> None:
        super().__init__()
        self.username = username
        self.email = email
        self.password = password

    def create_admin(self,username, email, password):
        admin = Admin(username, email, password)
        Bank.admins.append(admin)
        if(len(Bank.admins)>1):
            print("Admin account created successfully")
        return admin
    
    def delete_user(self, username, user_email):
        for user in Bank.users:
            if user.email == user_email:
                Bank.users.remove(user)
                print(f"User: {username} is removed.")
                return
        else:
            print("There is no such user available.")

    def user_account_list(self):
        for user in Bank.users:
            print(f'User Information:\nName: {user.name}\nId:{user.account_id}\nCurrent balance: {user.balance}\n\n')
    
        if len(Bank.users) == 0:
            print("There is no users.")

    @classmethod
    def check_total_available_balance(self):
        print('All user balance: ')
        for user in Bank.users:
            print(f'userid: {user.account_id} balance: {user.balance}')
        print("----------------------------------")
        Bank.cal_bank_balance()
        print(f"Total available balance: {Bank.bank_balance}")


    def check_total_loan_amount(self):
        print("All Users loan amount: ")
        total = 0 
        for user in Bank.users:
            total += user.loan_amount
            print(f'username: {user.name} userid: {user.account_id} loan_amount: {user.loan_amount}')
        print("----------------------------------")
        print(f"Total loan amount: {total}")


    def loan_feature(self):
        print("Loan Feature? (on/ off): ")
        str = input()
        if(str == 'on'):
            Bank.loan_feature = True
            print("Loan feature turned on")
        else:
            Bank.loan_feature = False
            print("Loan feature turned off")




class User(Bank):
    def __init__(self, name, email, address, account_type, account_id) -> None:
        super().__init__()
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_id = account_id
        self.balance = 0
        self.loan_count = 0  
        self.loan_amount = 0
       
    @classmethod
    def create_account(self, name, email, address, account_type):
        self.transaction_history[email] = []
        self.account_id = email + str(Bank.id)
        Bank.id += 1
        user = User(name, email, address, account_type, self.account_id)
        Bank.users.append(user)  
        print("User account created successfully")

    def deposit(self, amount, user):
        self.balance += amount
        self.msg = f'Diposited {amount}'
        Bank.cal_bank_balance()
        Bank.transaction_history[user.email].append(self.msg)
        print("Deposit Successful.")


    def withdraw(self, amount, user):

        if self.balance == 0:
            print(f"You cannot make withdraw. You have {amount} money")
        elif amount > self.balance:
            print("Withdrawal amount exceeded")
        else:
            self.balance -= amount
            Bank.cal_bank_balance()
            Bank.transaction_history[user.email].append(f"Withdrew {amount}")
            print("Withdraw Successful.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def all_transaction_history(self, email):
        print("All transaction History: ")
        print("----------------------------")
        for trn in Bank.transaction_history[email]:
            print(trn)

    def take_loan(self, amount, user):
        if self.loan_feature == False:
            print("Loan Feature is not avaiable.")
           
        else:
            if self.loan_count < 2:
                self.balance += amount
                self.loan_amount += amount
                Bank.cal_bank_balance()
                self.loan_count += 1
                Bank.transaction_history[user.email].append(f"Loan taken: {amount}")
                print("Loan taken successfully")
            else:
                print(f"You can take a loan from the bank at most two times.You have already taken loan: {self.loan_count} times.")


    def transfer_money(self, other_account, amount):
        for user in Bank.users:
            if(user.email == other_account):   
                if amount > self.balance:
                    print("Money transfer amount exceeded")
                else:
                    self.balance -= amount
                    user.balance += amount
                    Bank.transaction_history[self.email].append(f"Transfer money : {amount} to {user.name}")
                    Bank.transaction_history[user.email].append(f"Received money : {amount} from {self.name}")
                    Bank.cal_bank_balance()
                    print("Money Transfer Successful.")


    def deposit_all_money(self, amount, user):
        Bank.cal_bank_balance()
        if amount > Bank.bank_balance:
            print("The bank is bankrupt")
        else:
            self.withdraw(self.balance, user)




admin = Admin('admin', 'admin@gmail.com', 'admin123')
admin = admin.create_admin('admin', 'admin@gmail.com', 'admin123')
i = 1
while 1:
    if  i >= 3 or i<0:
        break
    print("--------------Welcome to the Bank XYZ----------------")
    print("1. You are an admin")
    print("2. You are a User")
    print("3. Exit")

    i = int(input())

    if(i == 1):
        a =1
        while 1:
            if a>=7 or a<0:
                break
            print("-----------------Admin Panel---------------")
            print("1. create an admin account")
            print("2. delete any user account")
            print("3. see all user accounts list")
            print("4. check the total available balance of the bank")
            print("5. check the total loan amount.")
            print("6. on or off the loan feature of the bank.")
            print("7. Exit.")

            a = int(input())

            if(a == 1):
                print("Enter admin name:")
                username = input().lower()
                print("Enter email")
                email = input().lower()
                print("Enter password")
                password = input().lower()
                new_admin = admin.create_admin(username, email, password)

            elif(a == 2):
                print("Enter the user name: ")
                username = input().lower()
                print("Enter the email: ")
                email = input().lower()
                admin.delete_user(username, email)

            elif(a == 3):
                admin.user_account_list()

            elif(a== 4):
                admin.check_total_available_balance()
            
            elif(a==5):
                admin.check_total_loan_amount()
            
            elif(a==6):
                admin.loan_feature()

    elif i==2:
        a = 1
        while 1:
            if a < 0 or a >= 8:
                break
            print("----------------Bank Users-----------------")
            print("1. Create an user account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Avaiable balance")
            print("5. Check Transaction History")
            print("6. Take a loan")
            print("7. Transfer money to another account")
            print("8. Withdraw All Money")
            print("9. Exit")
            a = int(input())

            if a==1:
                print('Enter name: ')
                name = input().lower()
                print('Enter email: ')
                email = input()
                print('Enter address: ')
                address = input().lower()
                print('Enter account type (Savings or current): ')
                type = input().lower()
                User.create_account(name, email, address, type)

            
            elif a==2:
                print("Enter email: ")
                f = True
                email = input().lower()
                for user in Bank.users:
                    if user.email == email:
                        print("Enter deposit amount: ")
                        amount = int(input())
                        user.deposit(amount, user)
                        f = False
                        break
                if f:
                    print("Invalid email address")

            elif a==3:
                print('Enter email: ')
                email = input().lower()
                f = True
                for user in Bank.users:
                    if user.email == email:
                        print("Enter withdraw amount: ")
                        amount = int(input())
                        user.withdraw(amount, user)
                        f = False
                        break
                if f:
                    print("Invalid email address")

            elif a==4:
                print('Enter email: ')
                f = True
                email = input().lower()
                for user in Bank.users:
                    if user.email == email:
                        f = False
                        user.check_balance()
                        break
                if f:
                    print("Invalid email address")

            elif a==5:
                print('Enter email: ')
                f = True
                email = input().lower()
                for user in Bank.users:
                    if user.email == email:
                        user.all_transaction_history(email)
                        f = False
                        break
                if f:
                    print("Invalid email address")

            elif a==6:
                print('Enter email: ')
                f = True
                email = input().lower()
                for user in Bank.users:
                    if user.email == email:
                        print("Enter Amount: ")
                        amount = int(input())
                        user.take_loan(amount, user)
                        f = False
                        break
                if f:
                    print("Invalid email address")

            elif a==7:
                print('Enter email: ')
                f = True
                email = input().lower()
                for user in Bank.users:
                    if user.email == email:
                        print("Enter other account email address: ")
                        str = input().lower()
                        other_account = ""
                        f = False
                        for user1 in Bank.users:
                            if user1.email == str:
                                f = True
                                other_account = str
                                break
                        if not f:
                            print("Account doesn't exist")
                        else:
                            print("Enter amount: ")
                            amount = int(input())
                            user.transfer_money(other_account, amount)
                            f = False
                        break
                if f:
                    print("Invalid email address")

            elif a==8:
                print("Enter email: ")
                f = True
                email = input().lower()
                for user in Bank.users:
                    if user.email == email:
                        amount = user.balance
                        user.deposit_all_money(amount, user)
                        f = False
                        break
                if f:
                    print("Invalid email address")

            else:
                break

    else:
        break
    
