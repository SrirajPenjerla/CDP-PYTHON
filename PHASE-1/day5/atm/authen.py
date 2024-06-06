import rbalance as reb
users=reb.users




class Auth:
    total_amount = 10000
    def authenticate(self):
        token=0
        self.token=token
        name=input("Enter user name ")
        pas=input("Enter password  ")
        self.name=name 
        self.pas=pas
        if name ==  pas:
            token=1
            print("autenctication sucessfull!!!!! ")
            # val=self.card()
            # self.display(token)
        else:
            token=0
        return token,name,pas
        
    def card(self):
        val=0
        self.val=val
        print("::: select the type of card from below ::: ")
        card=input("::: 1 rupay\t2 visa\t3 master card  :::\n ")
        card=card.lower()
        if card == "rupay" or card == '1':
            val=1
            # self.authenticate(val)
        elif card == "visa" or card == '2':
            val=2
            # self.authenticate(val)
        elif card == "master card" or card == '3':
            val=3
            # self.authenticate(val)

        else:
            print("::: enter the valid card ::: ")
            self.card()
        return val


    # def display(self,token,val):
    #     if token ==1 :
    #         print("choose one of the option below" )
    #         n=input("1 check balance \t2 cash withdrawal \t3 cash deposit\t4 mini statement \t5 exit")
    #         n=n.lower()
    #         if n == "check balance " or n =="1":
    #             self.checkbalance(self.name)
    #         elif n == "cash withdrawal" or n =="2":
    #             self.cashwithdrawal(int(input("please enter the pin ")),self.name,val)
    #         elif n == "cashdeposit" or n =="3":
    #             self.cashdeposit(int(input("please input the pin ")),self.name)
    #         elif n == "mini statement" or n =="4":
    #             self.mini(self.name)
    #         elif n == "exit" or n =="5":
    #             pass
    #         else:
    #             print("please enter valid option ")
    #             self.display()

    def checkbalance(self,name):
        if name in users:
            print(f'your balance is :: ₹ {users[name]}')
            # self.display(1,self.val)
        elif name not in users:
            print("balance is ₹ 0")
            # print("please deposit some money to with draw")
            # self.cashdeposit(int(input("enter the pin"),name))
        

    def cashdeposit(self,pin,name,total_amount):
        if type(pin) is int:
            a=int(input("enter the amount which you want to deposit :: "))
            if name not in users:
                users[name]=a
            else:
                bal=users[name]
                bal=bal+a
                users[name]=bal
                total_amount=total_amount+a
        else:
            print("enter coorect pin :: ")
        return total_amount
        # self.checkbalance(name)
    
    def cashwithdrawal(self,pin,name,val,total_amount):
        if name in users and users[name]!=0:       
            b=int(input("enter amount you want to with draw ::"))
            if val==1 and (b > 2000 ) :
                print("::: card limit(2000) extemded:::")
                print("::: please enter the right amount :::")
                # self.cashwithdrawal(pin,name,val)
            elif users[name] == 0:
                print("::: your balance is 0 please deposit some money :::")
            # else:
            #     print("helloo")
            #     bal=users[name]
            #     if b>bal:
            #         print("you dont have enough money to withdraw that amount")
            #         users[name]=bal
            #     else:
            #         balance= bal-b
            #         users[name]=balance
            #         total_amount=total_amount-b
            if val==2 and (b > 5000 ):
                print("::: card limit(5000) extemded:::")
                print("::: please enter the right amount :::")
                # self.cashwithdrawal(pin,name,val)
            # elif users[name] == 0:
            #     print("your balance is 0 please deposit some money")
            # else:
            #     bal=users[name]
            #     if b>bal:
            #         print("you dont have enough money to withdraw that amount")
            #         users[name]=bal
            #     else:
            #         balance= bal-b
            #         users[name]=balance
            #         total_amount=total_amount-b

            elif val==3 and (b > 8499 ):
                print("::: card limit(8499) extemded:::")
                print("::: please enter the right amount :::")
            #     # self.cashwithdrawal(pin,name,val)
            # elif users[name] == 0:
            #     print("your balance is 0 please deposit some money")
            # else:
            #     bal=users[name]
            #     if b>bal:
            #         print("you dont have enough money to withdraw that amount")
            #         users[name]=bal
            #     else:
            #         balance= bal-b
            #         users[name]=balance
            #         total_amount=total_amount-b
                    
            # self.checkbalance(self,name)
            else:
                bal=users[name]
                if b>bal:
                    print("::: you dont have enough money to withdraw that amount :::")
                    users[name]=bal
                else:
                    balance= bal-b
                    users[name]=balance
                    total_amount=total_amount-b
        else:
            print("::: first deposit some money to withdraw ::: ")
            users[name]=0
            # self.checkbalance(self,name)
        return total_amount
    def mini(self, asd ):
        print("::: Mini Statement :::")
        asd=asd[-3:]
        print("\n".join(asd))
        print("::::::::::::::::::::::")
    
a=Auth()
     
    


