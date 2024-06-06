import csv
class Gen:
    def generate_bill(self,uname,item,price,quan):
        fp=int(price)*quan
        with open ( 'users.csv','r',newline="") as file:
            read=csv.DictReader(file)
            for row in read:
                if row['uname'] == uname:
                    print("=================================")
                    print("YOUR BILL FOR THE ORDER IS ")
                    print("Name :",uname)
                    print("Address :",row['city'])
                    print("COntact number :",row['phnno'])
                    print("Item ordered :",item)
                    print("Original price :",price)
                    print("Total Pieces :",quan)
                    print("final price :: ",fp)
                    print("pay yor bill after receiving the product")
                    print("=================================")



