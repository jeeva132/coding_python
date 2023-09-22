def findproduct(arr,sum):
    
    minsum = sum
    pro = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j and (arr[i]+arr[j])<= minsum:
                minsum = arr[i]+arr[j]
                pro = arr[i]*arr[j]
                
    return pro

print(findproduct([5 ,2 ,4 ,3 ,9 ,7 ,1],7))
                
        