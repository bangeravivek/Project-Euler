sum1=0
sum2=0
numbers=range(1,101)

for i in numbers:
    sum1=sum1+i*i
    
for j in numbers:
    sum2=sum2+j

sum2=sum2*sum2

difference=sum2-sum1

print sum1, sum2, difference

