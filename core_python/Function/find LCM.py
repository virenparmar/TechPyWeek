# Python program to fing the L.C.M. of two input number

#define a functino

def lcm(x,y):
	"""This functioon takes two integers and returns the L.C.M. """

	#choose the greater number

	if x>y:
		greater=x
	else:
		greater=y

	while(True):
		if((greater%x==0)and(greater%y==0)):
			lcm=greater
			break
		greater+=1
	return lcm

#take input from the user

num1=int(input("Entert first number="))
num2=int(input("Enter seecond number="))

print("The L.C.M. of",num1,"and",num2,"is",lcm(num1,num2))