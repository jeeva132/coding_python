def count(arr,num,diff):
    if arr is None:
        return -1
    
    count = 0
    for i in arr:
        if abs(i-num)<=diff:
            count +=1
            
    return count

print(count([12,3,14,56,77,13],13,2))