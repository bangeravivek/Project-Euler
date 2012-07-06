#Using brute force

def check_palindrome(number):
    listing=[]
    flag0=0
    while number/10 >0:
        numb=number%10
        listing.append(numb)
        number=number/10
    listing.append(number)
    listing.reverse()
    print listing
    
    i=0
    j=len(listing)-1
    flag=0
    while flag==0:
        print "not waste"
        if i>=j:
            return 1
        if listing[i]==listing[j]:
            print i,j
            i=i+1
            j=j-1
        else:
            flag=1
            return 0
            
    return 1
'''
result=check_palindrome(9009)
print result
'''
flag1=0
i=999

palind=0

count=0

while flag1==0 and count<10 and i>100:
    #print i
    for j in range(100,999):
        print j
        multi=i*j
        print multi
        result=check_palindrome(multi)
        if(result==1):
            if(multi>palind):
                palind=multi
            else:
                count+=1
    print "This is i: %d" %i
    i=i-1
    
print "The largest palindrome is : %d" %palind                
                    

                
                

