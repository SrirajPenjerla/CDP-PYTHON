import csv 
class Items_d:
    def display(self):
        print(" :: slect one of the category :: ")
        n=input("1.Mobiles\t2.Tvs\t3.Watches \n")
        n=n.lower()
        with open("items.csv",'r',newline="") as file:
            a=csv.DictReader(file)
            if n == "mobiles" or n == '1':
                for row in a:
                    if row['cat'] == "mobile":
                        print(f'Item ::  {row['item']}   price :: {row['price']}  stock left :: {row['quan']}')
            elif n == "tvs" or n == '2':
                for row in a:
                    if row['cat'] == "tv":
                        print(f'Item ::  {row['item']}   price :: {row['price']}  stock left :: {row['quan']}')
            elif n == "watches" or n == '3':
                for row in a:
                    if row['cat'] == "watch":
                        print(f'Item ::  {row['item']}   price :: {row['price']}  stock left :: {row['quan']}')
            else:
                print("enter valid option ")
                return 0
