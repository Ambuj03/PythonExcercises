def numList(llist,num):

    for i in range(0,len(llist)-1):
        if num ==llist[i]:
            return True

    return False

def numListBinary(llist,num):
    l = 0
    r = len(llist)-1

    while(l<=r):
        idx = int((l+r) / 2)
        if num ==llist[idx]:
            return True
        elif num > llist[idx]:
            l = idx + 1
        else:
            r = idx-1    

    return False

a = [1,2,3,45,23,76,98,34]
target = 98

print(numListBinary(a,target))