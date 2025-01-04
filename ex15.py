def revString(s):
    listS = s.split()
    resS = ""
    for i in range(len(listS)-1,0,-1):
        resS += " "+ listS[i]
        
    resS += " "+ listS[0]    
    print(resS)

revString("My name is Michele")