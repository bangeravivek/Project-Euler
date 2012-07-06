
#global variable fibonacci

fibonacci=[1]
fibonacci.append(2)

print fibonacci

sumer=0

flag=0

i=1

while flag==0:
    print i
    sumer=fibonacci[i]+fibonacci[i-1]
    if sumer<4000000:
        fibonacci.append(sumer)
        i=i+1
    else:
        flag=1
        

sumer=0

for i in range(1, len(fibonacci)):
    if fibonacci[i]%2==0:
        sumer=sumer+fibonacci[i]

print " The sum is: %d " %sumer

