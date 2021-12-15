class bank:
    
    
    def __init__(self,Bankname,Name,Accno,Deposit,Withdraw,Enquiry):

        self.bankname=Bankname
        self.name=Name
        self.accno=Accno
        self.deposit=Deposit
        self.withdraw=Withdraw
        self.enquiry=Enquiry
        a["bankname"] = self.bankname 
        a["name"] = self.name
        a["accno"] = self.accno
        database.append(a)
       
        
    def bankname_verification(self):
        name = str(input("Enter firstname:"))
        con.append(name)
        if not name.isalpha():
            raise TypeError("Firstname contain only letters")
            
        
        
    def name_verification(self):
        name = str(input("Enter Lastnamename:"))
        con.append(name)
        if not name.isalpha():
            raise TypeError("Lastname contain only letters")
        
        
    def accno_verification(self):
        number=input("Enter Phonenumber:")
        if type(number) == str:
            if (len(str(number)) <= 10):
                con.append(number)
                print("valid phonenumber")
            else:
                raise TypeError ("phonenumber not valid")   
        
    def deposit(self):
        amount=int(input('Enter the amount to deposit:'))
        self.balance+=amount
        print('Your New Balance =%d' %self.balance)
    def withdraw(self):
        amount=int(input('Enter the amount to withdraw:'))
        if(amount>self.balance):
            print('Insufficient Balance!')
        else:
            self.balance-=amount
            print('Your Remaining Balance =%d' %self.balance)
    def enquiry(self):
        print('Your Balance =%d' %self.balance)
       
        
               
    
a={}
con=[]

database=[{"Firstname":"Abi","Lastname":"Rithinyaa","Phno":9854268725,"Groups":"Family"},            
       {"Firstname":"Anu","Lastname":"priyaa","Phno":9987968234,"Groups":"Friends"},
       {"Firstname":"Aarthi","Lastname":"M","Phno":9172653411,"Groups":"Friends"},
       {"Firstname":"Abiani","Lastname":"Kumar","Phno":9813245678,"Groups":"Friends"},
       {"Firstname":"Akash","Lastname":"Kumar","Phno":7985432876,"Groups":"Friends"},
       {"Firstname":"Abirami","Lastname":"N","Phno":8765431987,"Groups":"Friends"},]

       
       
database.append(con)

 
mano=bank("bb","mano",2345678,450,100,350)
mano.bankname_verification()
mano.name_verification()
mano.accno_verification()
mano.deposit()
mano.withdraw()
mano.enquiry()


    


print(database)
