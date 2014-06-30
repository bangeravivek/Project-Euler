import time

'''Lets start this'''

print "Hello"

'''Days in Week:7'''
'''Monday=0'''

daycounter=0
sundaycount=0

daycounter=365%7
print daycounter

for i in range(1901,2001):
	print i
	'''time.sleep(5)'''
	for j in range(1,13):
		if (j==4) or (j==6) or (j==9) or (j==11):
			noofdays=30
		elif (j==2):
			if (i==2000):
				noofdays=29
			elif (i%4==0):
				noofdays=29
			else:
				noofdays=28
		else:
			noofdays=31
		week=1
		weektracker=daycounter
		for k in range(1,noofdays+1):
			if (k==1) and (week==1) and (daycounter==6):
				sundaycount=sundaycount+1
				print i," ",j," ",k	 
			daycounter=daycounter+1
			daycounter=daycounter%7
			
			
print sundaycount
