import math
number=range(2,2000000)

def isprime(a):
    n=int(math.sqrt(a))
    
    for i in range(3,n+1,2):
        if a%i==0:
           return 1
    return 0


#number=range(1,10,2)
sum_prime=0

primes=[2]

for i in range(3,2000000,2):
    flag=isprime(i)
    if flag==0:
        primes.append(i)        
        
print primes
sum_prime=sum(primes)
print " The sum is: %d" %sum_prime
print primes[0]
