def rats(r,units,arr):
    if len(arr) is None:
        return 0
    food_req = r * units
    count = 0
    total = 0
    for i in arr:
#         print(count)
        if total>=food_req :
            return count
        total +=i
        count +=1
        
print(rats(7,2,[2,8,3,5,7,4,1,2]))
    