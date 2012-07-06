import operator
numbers=range(2,21)

i=0
j=0

while i < len(numbers):
    j=i+1
    while j < len(numbers):
        if numbers[j]%numbers[i]==0:
            numbers[j]=numbers[j]/numbers[i]
        
        j=j+1
    i=i+1           
print numbers
product=reduce(operator.mul, numbers)
print product

