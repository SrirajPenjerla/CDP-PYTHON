import csv 
class Order:
    def price_item(self,item):
        # price=0
        with open("items.csv",'r',newline="") as file: 
            read=csv.DictReader(file)
            # write=csv.DictWriter(file)
            for row in read:
                if row['item'] == item :
                    # row['quan']-=quan
                    return row['price']
    def q(self,item):
        with open("items.csv",'r',newline="") as file:
            reader=csv.DictReader(file)
            products=list(reader)
            for row in products:
                if row['item'] == item and int(row['quan']) >0:
                    n=int(input("enter the quantity of the products you want to purchase :"))
                    quan=int(row['quan'])
                    if n < quan:
                        row['quan']=str(quan-n)
                        with open("items.csv", "w", newline="") as f:
                            writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
                            writer.writeheader()
                            writer.writerows(products)
                        return quan
                    else :
                        print("we donot have that many pieces")
                        return 0
        


                

        