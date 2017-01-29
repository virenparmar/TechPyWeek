#Python program to display the fibonacci sequence up to n-th term where n is provided

#take in input from the user

num=int(input("How many term?"))

no1=0
no2=1
count=2

# check if the number of terms is valid

if num<=0:
	print("please enter a positive integer")
elif num == 1:
	print("fibonacci sequence")
	print(no1)
else:
	print("fibonacci sequence")
	print(no1,",",no2,",")

	while count<num:
		nth=no1+no2
		print(nth,",")

		#update values
		no1=no2
		no2=nth
		count+=1