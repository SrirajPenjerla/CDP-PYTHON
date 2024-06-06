
class Atm:
    def __init__(self):
        c=[]
        self.c=c
        # total_amount =1000000
        # self.total_amount=total_amount
        print(":::::::::: Welcome to XYZ atm ::::::::::")
        l=input(":: 1.Total amount in atm\t2.choose card ::\n")
        l=l.lower()
        tm=ac.Auth.total_amount
        if l == "total amount in atm" or l == "1":
            self.tam(tm)
        elif l == 'choose card' or l=="2":
            token,name,pas=ac.Auth.authenticate(self)
            self.token=token
            self.name=name
            self.pas=pas
            val=ac.Auth.card(self)
            self.val=val
            self.display(token,val,tm)
        else:
            print(":::you have entered invalid value please check and enter:::")
            c=Atm()
    def tam(self,tm):
        sa=ac.users.values()
        print(":::: Total amount in the atm is ₹ ",sum(sa)," ::::")
        c=Atm()
    def display(self,token,val,tm):
        if token ==1 :
            print("::::: choose one of the option below :::::" )
            n=input("::: 1 check balance \t2 cash withdrawal \t3 cash deposit\t4 mini statement \t5 exit :::\n")
            n=n.lower()
            if n == "check balance " or n =="1":
                ac.Auth.checkbalance(self,self.name)
                self.c.append("Balance checked")
                self.display(token,val,tm)
 
            elif n == "cash withdrawal" or n =="2":

                ac.Auth.cashwithdrawal(self,int(input("please enter the pin :: ")),self.name,self.val,tm)
                self.c.append("cash is with drawn")
                ac.Auth.checkbalance(self,self.name)
                self.display(token,val,tm)
                
            elif n == "cashdeposit" or n =="3":
                ac.Auth.cashdeposit(self,int(input("please input the pin :: ")),self.name,tm)
                self.c.append("cash is deposited")

                ac.Auth.checkbalance(self,self.name)
                self.display(token,val,tm)
            elif n == "mini statement" or n =="4":
                ac.Auth.mini(self,self.c)
                self.display(token,val,tm)
                # ac.Auth.checkbalance(self,self.name)
            elif n == "exit" or n =="5":
                c=Atm()
            else:
                print("::: please enter valid option ::: ")
                self.display(token,val,tm)
        else:
            ac.Auth.authenticate(self)
import authen as ac    

