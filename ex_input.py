# Exercises, study hard fucker
#
#
# Import date time to obtain current year
import datetime
# Variables
name = ''
age = 0
year = 0
now = None
repeat = 0
# Main script.
now = datetime.datetime.now()
name = input("Enter name: ")
age = int(input("Enter age: "))
repeat = int(input("How many times you want to repeat this message: \n"))
year = (100 - age) + now.year
for i in range(1, repeat + 1, 1):
    print(i,"Your name is ",name,"and your will be 100 in",year)

input("Press enter to exit")
