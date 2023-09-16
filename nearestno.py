lst = [1,8,3,4,7]
def find(k,lst):
    
    minno = lst[0]
    mindif = abs(k-minno)
    for i in lst:
        nextmin = abs(i-k)
        if nextmin<mindif:
            mindif = nextmin
            minno = i
            
        
    return minno

print(find(5.9,lst))