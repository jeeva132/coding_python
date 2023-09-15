def indexdif(i1,i2):
    total = 0
    for i in range(i1):
        if i%2 == 0:
            total +=i2[i]
        else:
            total -=i2[i]
    return total
i1 = 7

i2 = [10 ,20 ,30 ,40 ,50 ,60 ,70]
print(indexdif(i1,i2))