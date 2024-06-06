''' to design a basic login system for accepting user name and password 
if both are equal login success else again ask for credentials until both are same '''

# def login():          # with recursion
#     username=input("Enter the user name ::  ")
#     password=input("Emter the password :: ")
#     if username == password:
#         print("Login sucessful !!!!")
#     else:
#         print("Creditials are wrong please enter again :: ")
#         login()
# login()

def login():                #with out recursion 
    while(1):
        username=input("Enter the user name :: ")
        password=input("Enter the password :: ")
        if username == password:
            print("Login sucessful !!!!")
            break
        else:
            print("Creditials are wrong please enter again :: ")

login()