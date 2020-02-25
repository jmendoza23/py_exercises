# usrName = input("Enter your user name: ")
# print("User Name: ", usrName.upper())
# print("User Name: ", usrName.lower())
# print("User Name: ", usrName.capitalize())
#
# edad = input("Cual es tu edad: ")
# while(edad.isdigit()==False):
#     print("Only numbers are allowed, try again...")
#     edad = input("Cual es tu edad: ")
# if (int(edad)<18):
#     print("Not allowed")
# else:
#     print("Welcome")

usrEmail = input("Enter Email: ")

while (usrEmail.startswith("@")) or (usrEmail.endswith("@")) or "@" not in usrEmail or "." not in usrEmail or  usrEmail.count("@") != 1 or usrEmail.count(".") != 1 or "@." in usrEmail or ".@" in usrEmail or (usrEmail.startswith(".")) or (usrEmail.endswith(".")):
    print("Wrong format, try again...")
    usrEmail = input("Enter Email: ")



print (usrEmail, "\nEmail is correct!!")

