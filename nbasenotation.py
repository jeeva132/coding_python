def dectonbase(n,num):
    
    newstr = ''
    while num!=0:
        rem = num%n
        if rem>=10:
            newstr =chr(rem+55)+newstr
        else:
            newstr =str(rem)+newstr
        num = num//n
    return newstr

print(dectonbase(21,5678))