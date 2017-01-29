# Program make a simple calculator that can addition,subtract,multiply and divide using functions

#define functions

def add(x,y):
	
	"""This function add two numbers"""

	return x+y

def sub(x,y):

	"""This function subtract two numbers"""

	return x-y

def mul(x,y):

	"""This function multiply two numbers"""

	return x*y

def div(x,y):

	"""This function divides two number"""

	return x/y

#take input from user

print("Select operation")
print("1.Addition")
print("2.subtraction")
print("3.multiplication")
print("4.Division")
##print("5.Exit")

choice=input("Enter your choice=")

num1=int(input("Enter the first number="))
num2=int(input("Enter the second number="))

if choice==1:
	print(num1,"+","=",add(num1,num2))

elif choice==2:
	print(num1,"-","=",sub(num1,num2))
elif choice==3:
	print(num1,"*","=",mul(num1,num2))
elif choice==4:
	print(num1,"/","=",div(num1,num2))
else:
	print("Sorry This is Invalid input!!!!Please try again")