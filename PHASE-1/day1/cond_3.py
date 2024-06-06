'''write a program to check the on road price of a bike under the condtions 
if the price is greater than 72000 then income tax is 10% of original price and insurance will be 15% of actal price
if the price is greater than 150000 and less than 200000 the tax would be 25 % and insurance is 20%
if price above 200000 then tax is 35% and insurance will be 28%
other wise minimum price with us starts at 72000 enter a valid price
actual price = tax + insurance+ exshowroom '''

price=int(input("Enter the price of Bike::"))

if price >= 72000 and price < 150000:
    tax=price*(10/100)
    insurance=price*(15/100)
    total_price=price+tax+insurance
    print("on road price: ₹",total_price)
elif price >= 150000 and price < 200000:
    tax=price*(25/100)
    insurance=price*(20/100)
    total_price=price+tax+insurance
    print("on road price: ₹",total_price)
elif price >= 200000:
    tax=price*(35/100)
    insurance=price*(28/100)
    total_price=price+tax+insurance
    print("on road price: ₹",total_price)
else:
    print("Minimum price with us starts at 72000 enter a valid price")

