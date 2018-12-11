# Given 2 lists, compare them and extract common elements to 
# insert in a new list(without duplicates)
# Extras:
# 1. Generate two random lists(same lenght).
#
# Import Random to create random lists.
import random

# Variables and lists.
mylist_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
mylist_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
mylist_c = []
mylist_d = []
mylist_e = []
lenght_list = 12

# Main with Extra 1.
[mylist_c.append(i) for i in mylist_a if i in mylist_b and i not in mylist_c]
for x in range(lenght_list):
    z = random.randint(1,99)
    y = random.randint(1,99)
    mylist_d.append(z)
    mylist_e.append(y)
print(mylist_c)
print(mylist_d)
print(mylist_e)
