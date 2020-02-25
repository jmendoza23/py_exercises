usrPath = list("UDDDUDUU")


currentPath = 0
result = 0
for elem in usrPath:
    #Dibujar el camino y almacenarlo en una lista
    if elem == "U":
        currentPath += 1
    else:
        if currentPath == 0:
            result += 1
        currentPath -= 1
return result
    




   

        
        

    

    



    