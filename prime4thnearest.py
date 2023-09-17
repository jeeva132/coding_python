def is_prime(n):
    if n<= 0:
        return False
    if n ==2 or n==3:
        return True
    for i in range(2,n-1):
        if n%i == 0:
            return False
    return True
    

def primes(n):
    primeno = []
    count = 0
    num = n
    nno1 = 0
    while count < 4:
        num -=1
        if is_prime(num):
            nno1 = num
            count +=1
            
    
            
    return nno1
print(primes(100))