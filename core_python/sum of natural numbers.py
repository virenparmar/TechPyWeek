#Python program to find the sum of natural numbers up ti n where n is by user

#take input from the user

num=int(input("Enter the number="))

if num<0:
	print("Enter a positive number=")

else:
	sum=0

	#use while loop to iterate un till zero

	while(num>0):
		sum+=num
		num-=1

	print("The sum is",sum)