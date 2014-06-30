'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

1 2 3 4
1 2 4 3 
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2
2 1 3 4
2 1 4 3
2 3 1 4
2 3 4 1
2 4 1 3
2 4 3 1

1023 987654
6^6
7^7 > 10^6 ?
'''

import numpy as np
import time
count = 0

numbers=np.array([0,1,2,3,4,5,6,7,8,9])
print "First permutation is:\n",numbers
size=len(numbers)-1
flag=True
index1=size-1
count=1
while flag==True:
#	descending=sorted(numbers,reverse=True)
#	for a in range(0,len(descending)):
#		if descending[a]!=numbers[a]:
#			break;
#	if a>=len(descending)-1:
#		flag=False	

	if numbers[index1]<numbers[index1+1]:
		minmax=10
		index2=index1
		for j in range(index1,size+1):
			if numbers[j]>numbers[index1] and numbers[j]<minmax:
				minmax=numbers[j]
				index2=j
		temp = numbers[index1]
		numbers[index1]=numbers[index2]
		numbers[index2]=temp
		numbers[index1+1:size+1].sort()
		count+=1
		#print count," combination: ", numbers
		if count == 1000000:
			flag=False
			break
		index1=size-1
	else:
		index1-=1
#	time.sleep(2)
		
print "1,000,000th combination is:",numbers
				
		
		
