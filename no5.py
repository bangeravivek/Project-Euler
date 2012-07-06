numbers=range(2,9)
print numbers
'''
flag=0
i=2520
j=2 
print i
k=i%j
print i
print j
print "%d" %k
j=j+1
print i, j
k=i%j
print i, j
print "%d" %k
'''

i=2
flag=0
j=2
while flag==0 and j in numbers:
    count=1
    if i%j!=0:
        j=2
        i=i+1
    else:
        count=count+1
        j=j+1
        
    print "%d, %d, %d" %(i,j,count)
    if count==len(numbers):
        flag=1

print "The number you want is: %d" %i

'''
while flag==0:
    count=1
    j=1
    while j<21:
        if i%j==0:
            count=count+1
            print count
            j=j+1
            print j
               
    if count==20:
        print "The number you want is: %d" %i
        flag=1
    
    i=i+1
'''
print "The number is: %d" %(i)            
