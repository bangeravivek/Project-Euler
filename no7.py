prime=int(raw_input("Enter the prime number you want:"))
numbers=[2]
count = 1
j=3

while len(numbers) < prime:
    flag=0
    for i in numbers:
        
        if j%i==0:
             flag=1
             break
    if flag==0:
        numbers.append(j)
        count=count+1
        
    j=j+1


print max(numbers)

