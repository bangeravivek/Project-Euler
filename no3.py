
number=600851475143
factors=[1]

numb=number/2

flag=0

for i in range(2,numb):
    if number%i==0:
        factors.append(i)
        while number%i==0:
            number=number/i
            print "%d is gone" %i

'''while flag==0:
    print "."
    if number%numb==0:
        factors=numb
        flag=1
    else:
        numb=numb-1
'''

print factors


