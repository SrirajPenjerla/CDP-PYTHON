# import csv
# f=open("data_pri.csv",'a',newline="")
# a=csv.writer(f)
# a.writerow(["StudentId","email","phone number","name"])
# studentId=int(input("Enter the student id :: "))
# email=input("enter email :: ")
# phn=int(input("enter phone number :: "))
# name=input("enter the name of student :: ")
# a.writerow([studentId,email,phn,name])
# print("student record saved ")


import csv 
with open("data_pri.csv",'a',newline="") as file :
    w=csv.writer(file)
    # if w.row == ["StudentId","email","phone number","name"]:
    #     pass
    # else:
    # w.writerow(["StudentId","email","phone number","name"])
    studentId=int(input("Enter the student id :: "))
    email=input("enter email :: ")
    phn=int(input("enter phone number :: "))
    name=input("enter the name of student :: ")
    w.writerow([studentId,email,phn,name])

with open("data_pri.csv",'r',newline="") as file:
    read=csv.DictReader(file)
    for row in read:
        print(f' name ::{row['name']} , id ::{row['StudentId']}')



