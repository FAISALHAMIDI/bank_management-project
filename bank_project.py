a=input("You Have Account? :")
if a=="no":
    print(" Creat Account ")
# while(True):
    lst=list()
    value = input("enter your Full Name:"),int(input("enter your mobile number:")),input("enter your Gmail ID:"),int(input("enter addhar number:"))
    print(value)
    lst.append((value))
    if lst !=0:
        print("youe data is sessusfully addfas")
        print("="*50)
        print("your account number is :>",123)
elif a=="yes":
    class Account:
        def __init__(self,balance,acc):
            self.balance=balance
            self.account=acc
        def debit(self,amount):
            self.balance-=amount
            print("RS",amount,"was debited")
            print("total balance=",self.get_balance())
        def credit(self,amount):
            self.balance+=amount
            print("RS",amount,"was credit")
            print("total balance=",self.get_balance())

        def get_balance(self):
            return self.balance
        
    acc=Account(0,123456)
    print("*" * 50)
    print("ENTER YOUR CHOICE")
    while(True):
         print("*" * 50)
         print("\t1.debite")
         print("\t2.cradit")
         print("\t3.balance enquri")
         ch = int(input("Enter Ur Choice:"))
        
         match (ch):
             case 1:
                a = float(input("hou many amount credit you= "))
                print(a)
                acc.credit(a)

             case 2:
                b = float(input("hou many amount debit you= "))
                print(b)
                acc.debit(b)
    
             case 3:
            # print(acc)
                acc.debit(0.0)
            # acc.debit(b)

             case _:  # Default Case Bloc
                print("Ur Selection of Operation is wrong-try again")

else:
     print("Enter Currect Answer")