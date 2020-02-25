# Python 3.7
#jr2r
# Counting Valleys

l = ""
c = 0
myRe = []

#Path list to iterate
path = list("DDUUDDUDUUUD")

for i in path:
    if l == "":
        l = i
        c += 1
    else:
        if l == i:
            c += 1
        else:
            if c >= 3:
                myRe.append(c)
                c = 1
                l = i
            else:
                c = 1
                l = i

print(len(myRe))
            
    

 
    
    

    
    



