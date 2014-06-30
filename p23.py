'''Non-abundant sums
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
import math

def isabundant(number):
	limits=number/2
	initsum=1
	for i in range(2,limits+1):
		if (number%i==0):
			initsum=initsum+i
	if initsum>number:
		return 1
	else:
		return 0

def opt_isabundant(number):
	limits=int(math.sqrt(number))+1
	n=number
	prod=1
	for i in range(2,limits):
		p=1
		while(n%i==0):
			p=p*i+1
			n=n/i
		prod=prod*p
	
	if (n>1):
		prod=prod*(1+n)
	
	if prod>2*number:
		return 1
	else:
		return 0

n=28123
totalsum=n*(n+1)/2

abundantsums=[]

limit=n

for i in range(1,limit):
	if (opt_isabundant(i)==1):
		abundantsums.append(i)
		
print abundantsums
sums=[]
sizes=len(abundantsums)
for i in range(0,sizes):
	for j in range(i,sizes):
		newsum=abundantsums[i]+abundantsums[j]
		sums.append(newsum)
'''
maxsize=max(abundantsums)
for i in range(1,maxsize):
	for j in range(i, maxsize):
		temp=i+j
'''		

newsums=set(sums)
#print newsums
newsum1=list(newsums)
newsum=0
sumstouse=[]
for i in range(0,len(newsum1)):
	if (newsum1[i]<=28123):
		sumstouse.append(newsum1[i])

print sumstouse
newsize=len(sumstouse)
for i in range(0,newsize):
	newsum=newsum+sumstouse[i]
print totalsum
print newsum
nonabundantsum=totalsum-newsum

print nonabundantsum
