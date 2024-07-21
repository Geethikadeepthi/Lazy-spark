user=['abd','vk','maxi','dhoni']
password=['abd999','vk18','maxi111','dhoni7']
pin=['360','50100','2023','2011']
balance=[20000,30000,14000,70000]
d=3
n=input("enter username:")
if(n in user):
    c=user.index(n)
    while(1):
        p=(input("enter password:"))
        if(p==password[c]):
            while(1):
                print("1.withdraw\n2.deposit\n3.balance check\n4.change password\n5.exit")
                choice=int(input("enter your choice:"))
                if(choice==1):
                    amt=int(input("enter amount:" ))
                    p1=(input("enter your pin:"))
                    if(p1==pin[c]):
                        if amt<=balance[c]:
                            print("collect your cash")
                            balance[c]=balance[c]-amt
                            print('available balance is:',balance[c])
                            exit
                        else:
                            print("insufficient balance\navailable balance is:",balance[c])
                            exit
                    else:
                        print("wrong pin")
                        exit
                elif(choice==2):
                    amt=int(input("enter amount to deposit:"))
                    p1=(input("enter your pin:"))
                    if(p1==pin[c]):
                        print(("amount deposited"))
                        balance[c]+=amt
                        print("available balance is :",balance[c])
                        exit
                    else:
                        print("wrong pin")
                        exit
                elif(choice==3):
                    p1=(input("enter your pin:"))
                    if(p1==pin[c]):
                        print("available balance is :",balance[c])
                    else:
                        print("wrong pin")
                        exit
                elif(choice==4):
                    p1=(input("enter your current pin:"))
                    if(p1==pin[c]):
                        n1=(input("enter your new pin:"))
                        n2=(input("reenter to confirm:"))
                    else:
                        exit
                        print("wrong pin")
                        break
                    if(n1==n2):
                        print("pin updated successfully")
                        exit
                    else:
                        print("pins not matched")
                        exit
                elif(choice==5):
                    break
                    exit
                else:
                    print("invalid choice")
            break
        else:
            d-=1
            print("incorrect password",d,"attemps left")
            if(d==0):
                print("account blocked")
                break
else:
    print("invalid user")
    exit