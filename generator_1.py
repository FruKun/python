def isprime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True
        
def primes(n):
    i=0
    while(i<n):
        if isprime(i): 
            yield i
        i += 1
a= primes(100)
for i in a:
    print(i)