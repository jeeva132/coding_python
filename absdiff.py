def absdiff(inp1,inp2,inp3):
    total = 0
    for i in range(inp3-1,inp1-1):
        if(i+1)!= None:
            total +=abs(inp2[i]-inp2[i+1])
    return total

i1 = 7
i2 = [11 ,22 ,12 ,24 ,13 ,26 ,14]
i3 = 5

print(absdiff(i1,i2,i3))