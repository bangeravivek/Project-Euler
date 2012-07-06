import math

'''generating a triangular number'''
'''
n=500
tri_number=0

for i in range(n+1):
    tri_number=tri_number+i

print tri_number

#factors=[1,tri_number]
'''
def get_factors(n):
    factors=[1, n]
    for i in range(2,int(math.sqrt(n))):
        if tri_number%i==0:
            factors.append(i)
            factors.append(tri_number/i)
           
    return factors

#print factors

n=1
i=1
tri_number=0
factors=[1]
length=1
while length<500:
    tri_number=tri_number+n
    n=n+1
    factors=get_factors(tri_number)
    length=len(factors)
#print factors
print tri_number
