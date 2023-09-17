def  is_prime(n):
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True

def printprime(n):
    primes = []
    for i in range(2,n-1):
        if is_prime(i):
            
                
            primes.append(i)
            
    for i in primes:
        print(i)
printprime(10)