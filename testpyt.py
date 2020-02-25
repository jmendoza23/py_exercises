# a = [5, 6, 7]
# b = [3, 6, 10]
# countA = 0
# countB = 0

#     for i in range(0, 3):
#         if a[i] > b[i]:
#             countA += 1
#         elif b[i] > a[i]:
#             countB += 1
#         else:
#             pass

#     print(countA, countB)

# a=[]
# total = 0
# count = int(input("Enter range: "))
# numbers = int(input("Enter number to start:"))
# for i in range(1, count+1):
#     numbers += 1
#     a.append(numbers)
# print(a)
# print(sum(a))

# arr = ([11, 2, 4, 6],
#         [4, 5, 6, 8],
#         [10, 8, -12, 10],
#         [11, 34, 45, 10])


# a = arr[0][0] + arr[1][1] + arr[2][2]
# b = arr[0][2] + arr[1][1] + arr[2][0]
# print(diagt1, ":", diagt2)
# print(sum(diagt1), ":", sum(diagt2))
# n = int(input("number:"))
# diagt1 = []
# diagt2 = []
# c = 0
# print(n)
# for i in range(0, n):
#     diagt1.append(arr[i][i])

# for j in reversed(range(0, n)):
#     diagt2.append(arr[j][c])
#     c += 1 
# print(diagt1, ":", diagt2)
# n1 = sum(diagt1)
# n2 = sum(diagt2)
# print(n1, ":", n2)
# print(abs(n1 - n2))

# arr = [-4, 3, -9, 0, 4, 1]
# ntotal = len(arr)
# c0 = 0
# cP = 0
# cN = 0
# for i in arr:
#     if i == 0:
#         c0 += 1
#     elif i > 0:
#         cP += 1
#     elif i < 0:
#         cN += 1

# print("{:.6f}".format(c0/n))
# print("{:.6f}".format(cP/n))
# print("{:.6f}".format(cN/n))

# n = int(input("Number: "))
# for i in range(1, n + 1):
#         print(str('#'*i).rjust(n))
    

    # minarr = []
    # maxarr = []

    # for i in arr:
    #     minarr.append(i)
    # minarr.remove(min(minarr))
    # print(minarr)

    # for j in arr:
    #     maxarr.append(j)
    # maxarr.remove(max(maxarr))
    # print(sum(minarr), sum(maxarr))
# x = sum(arr)
# print(x-(min(arr)), x-(max(arr)))

# n = int(input("N:"))
# arr = [3, 2, 1, 3]
# c = 0
# for i in arr:
#     if i >= n:
#         pass
#     else:
#         c += 1
# print(c)

# from collections import Counter

# array = ['10', '20', '20', '10', '10', '30', '50', '10', '20']
# def pairSocks(arr):
# c = Counter(array)
# pares = 0
# for i in c:
#     n = c[i]
#     if n %2 == 0:
#         resul = n/2
#         pares += resul
#     else:
#         n = n - 1
#         resul = n / 2
#         if resul >= 1:
#             pares += resul
# return int(pares)
# for values in c.values():
#     print (values)
#     pares+=values//2
#     print (pares)

# print(pairSocks(array))

# n = 7
# x = "0100010"
# mlist = list(x)
# ans = 0
# i = 0

# while i < n - 1:
#     if i + 2 >= n or c[i+2]==1:
#         i = i + 1
#         ans = ans + 1
#     else:
#         i = i + 2
#         ans = ans + 1
# print(ans)

n = 10
s = "aba"
result = s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")
print(result)



    
































        










    
    


    
    
    












        






