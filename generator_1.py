def isprime(n):
    if i<2:
        return False
    for j in range(2, i // 2 + 1):
        if (i % j == 0):
            return False
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
