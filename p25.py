'''
The Fibonacci sequence is defined by the recurrence relation:

Fn=Fn-1 +Fn-2 where F1=1 and F2=1
The first 12 terms are:
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
'''

a=1
b=1
number=1
numbercount=2
flag = True
while (flag==True):
	number=a+b
	numbercount+=1
	a=b
	b=number
	#print "\n",numbercount,"\t",number,"\n"
	count=1
	while (number/1000>0):
		count+=1
		number=number/1000
	if count==334:
		print number
		print numbercount
		flag==False
		break
