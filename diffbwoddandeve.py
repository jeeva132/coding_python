def diff(arr):
    if len(arr)<=3 or len(arr) == 0:
        return 0
    evea = []
    odd = []
    for i in range(len(arr)):
        if i%2 == 0:
            evea.append(arr[i])
        else:
            odd.append(arr[i])
            
    evea.sort()
    odd.sort()
    
    print(evea,odd)  
    return evea[-2]+odd[1]
print(diff([3,2,1,7,5,4]))