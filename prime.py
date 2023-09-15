def prime(n):
    if n==0:
        return 'not a prime'
    
    for i in range(2,n-1):
        if n%i==0:
            return 'not a prime'
    return 'prime'
print(prime(0))