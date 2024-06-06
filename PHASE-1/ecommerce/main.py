import user_verif
import gene_bill
import place_order
import reg_log
import list_of_items

class ecomerce:
    def __init__(self):
        print("welcome to anveshika")
        print("choose any option from below")
        n=input(" 1.login 2.register \n")
        n=n.lower()
        if n == 'login ' or n== '1':
            uname=input("enter user name ::  ")
            pas=input("enter password :: ")
            a=reg_log.RandL.login(self,uname,pas)
            if a == 1:
                self.dis()
            else:
                print("wrong password or user name ")
                c=ecomerce()
        elif n == 'register'or n =='2':
            uname=input("enter user name :: ")
            pas=input("enter password:: " )
            email=input("enter email :: " )
            city=input("enter your city :: ")
            phno=int(input("enter your phone number :: "))
            reg_log.RandL.Register(self,uname,pas,email,city,phno)
            c=ecomerce()

    def dis(self):
        print("choose one of the options from below")
        n=input(" 1 display products      2 order   3 logout")
        n=n.lower()
        if n == 'display' or n == ' display products' or n =='1':
            self.display()
        if n == 'order ' or n == '2':
            self.order()
        if n=='logout' or n == '3':
            c=ecomerce()



    def display(self):
        z=list_of_items.Items_d.display(self)
        if z == 0:
            print("choose valid options")
            self.display()
        self.dis()

    
    def order(self):
        item=input("enter item name you want to order :: ")
        price=place_order.Order.price_item(self,item)
        quan=place_order.Order.q(self,item)
        if quan !=0:
            gene_bill.Gen.generate_bill(self,input("enter user name :: "),item,price,quan)
        else:
            self.order()
        self.dis()


        # if n == "login/register" or n=='1':
        #     self.log_re()
        # elif n == "display products" or n == '2':
        #     list_of_items.Items_d(self)
        # elif n == "place order" or n=="3":
        #     if auth == 0:
        #         print("please login first to order ")
        #     else :
        #         user_verif.verif(uname)

e=ecomerce()