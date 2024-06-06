'''
::CAR SHOW ROOM PROJECT::

In our show room only 3 car company : Toyota , Mahindra , Mercedes

take the input from the user for the car company name and in the input msg give the user the three options of companies 
this user input comp name goes as the input/argument to model name function ,which welcomes the user accordingly to the 
company name. ask the user to enter the specific model name  for that company 

the second function whose name is variant according to the comp name and the model the user should be asked to enter the 
variant he would like to choose from  petrol diesel 

the last display func acording to the car comp and model name and variant first its ex show room price should be displayd 
and then its on road price which is calc as ex show room + cgst+SGST+insurance.the sgst cgst and the insurance all the three 
have the common value throughout the car show room


'''

class carshowroom:
    def __init__(self):
        print("Welcome to the Raj carshowroom")
        self.in_put()

    def variant(self,car,model):
        print(f'Select the variant for car::{car}  and modelname ::{model}')
        var=input("1.Petrol\t2.Diesel \n ")
        var=var.lower()
        self.display(var,car,model)

    def in_put(self):
        print("Enter one of the car name from the below\n")
        car=input("1.Toyota\t2.Mahindra\t3.Mercedes\n")
        car=car.lower()
        if car.lower() == "toyota" or car.lower() == "1":
            print(f"---- welcome to the Toyota family ----")
            print("---- select the availabe models from below ----\n")
            model=input("1.Supra\t2.Fortuner\t3.Innova\n")
            model=model.lower()
            self.variant(car,model)
        elif car.lower() == "mahindra" or car.lower() == "2":
            print(f"---- welcome to the Mahindra family ----")
            print("---- select the availabe models from below ----")
            model=input("1.Thar\t2.Scorpio\t3.XUV700\n")
            model=model.lower()
            self.variant(car,model)
        elif car.lower() == "mercedes" or car.lower() == "3":
            print(f"---- welcome to the Mercedes family ----")
            print("---- select the availabe models from below ----")
            model=input("1.G-Wagnor\t2.C-Class\t3.S-Class\n")
            model=model.lower()
            self.variant(car,model)
        else:
            print("sorry our showroom does not have that company ")
            print()
            self.in_put()
    

    def display(self,var,car,model):
        p=self.get_price(var,car,model)
        print(f'Ex showroom price of your car is ₹ {p}')
        cgst=(p*(18/100))
        sgst=(p*(17/100))
        ins=(p*(20/100))
        op=p+cgst+sgst+ins
        print("On Road price of your car is ₹",int(op))


    def get_price(self,var,car,model):
        price=0
        if car == "toyota" or car == "1":
            if model == 'supra' or model == '1':
                if var == 'petrol' or var =='1':
                    price=9000000
                elif var =='diesel' or var=='2':
                    price=10000000
            elif model == 'fortuner' or model == '2':
                if var == 'petrol' or var =='1':
                    price=3500000
                elif var =='diesel' or var=='2':
                    price=4000000
            elif model == 'innova' or model == '3':
                if var == 'petrol' or var =='1':
                    price=3300000
                elif var =='diesel' or var=='2':
                    price=3700000
        elif car == "mahindra" or car == "2":
            if model == 'thar' or model == '1':
                if var == 'petrol' or var =='1':
                    price=2500000
                elif var =='diesel' or var=='2':
                    price=3000000
            elif model == 'scorpio' or model == '2':
                if var == 'petrol' or var =='1':
                    price=1300000
                elif var =='diesel' or var=='2':
                    price=1500000
            elif model == 'xuv700' or model == '3':
                if var == 'petrol' or var =='1':
                    price=1800000
                elif var =='diesel' or var=='2':
                    price=2200000
        elif car == "mercedes" or car == "3":
            if model == 'g-wagnor' or model == '1':
                if var == 'petrol' or var =='1':
                    price=10000000
                elif var =='diesel' or var=='2':
                    price=11400000
            elif model == 'c-class' or model == '2':
                if var == 'petrol' or var =='1':
                    price=15000000
                elif var =='diesel' or var=='2':
                    price=15300000
            elif model == 's-class' or model == '3':
                if var == 'petrol' or var =='1':
                    price=22000000
                elif var =='diesel' or var=='2':
                    price=22300000
        if price!=0:
            return price
        else:
            print(f"Sorry we dont have that model number {model} with {var} variant ")
            print("----kindly enter again----")
            self.in_put()
                

c=carshowroom()

