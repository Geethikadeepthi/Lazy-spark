users=["sam","jhon","priya","daniel"]
password=["sam123","jhon456","priya789","daniel465"]
pin=[1234,3425,6752,9087]
balance=[30000,40000,23400,43005]
def login(x):
    if  x in users :          
      return  "user identified"
    else:
      return "users doesnt exsist"
x=input("enter username: ")
print(login(x))
if (login(x)=="user identified"):
    y=input("enter password: ")
    
    def passwords(x,y):
        if (x in users) and (y in password):
            if(users.index(x) == password.index(y)):
                return "valid user"
            else:
                return "incorrect password try again"
        else:
            return "incorrect password try again"
    print(passwords(x,y))
else:
    exit

print("1  withdrawl")
print("2 deposit ")
print("3 check balance")
print("4 change password")
def choice(ch):
    if ch==1:
        z=int(input("enter amount: "))
        pin_code=int(input("enter pin code: "))
        if (pin_code==pin[users.index(x)]):
             if (z<=balance[users.index(x)]):
                 print("transaction successful")
             else:
                 print("insufficient balance")
        else:
            print("END")
    elif ch==2:
        d=int(input("enter amount to be deposited: "))
        pin_code=int(input("enter pin code: "))
        if (pin_code==pin[users.index(x)]):
             print("deposit successful")
             n_balance=d+balance[users.index(x)]
             print(n_balance)
        else:
                 print("wrong pin")
                 print("END")
    elif ch==3:
        pin_code=int(input("enter pin code: "))
        if (pin_code==pin[users.index(x)]):
             print("your available balance = ",end=' ')
             n_balance=balance[users.index(x)]
             print(n_balance)
        else:
                 print("wrong pin")
                 print("END")
    elif ch==4:
        p=input("enter your current password: ")
        np=input("enter new password: ")
        if (p==np):
            print("new password same as old password")
        else:
            cp=input("renter new password")
            p=cp
            print("password changed sucessfully")
ch=int(input("enter your choice"))
print(choice(ch))