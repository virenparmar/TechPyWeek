# Python program to display the fibonacci sequnce up to n-th term using recursive

def recur_fibo(n):
	"""recursive function to print fibonacci sequence"""

	if n<=1:
		return n
	else:
		return(recur_fibo(n-1)+recur_fibo(n-2))

# take imput from the user

nterms=int(input("How many terms?"))

#check if the number of terms is valid

if nterms<=0:
	print("Please enter a positive integer")

else:
	print("fibonacci sequence")

	for i in range(nterms):
		print(recur_fibo(i))