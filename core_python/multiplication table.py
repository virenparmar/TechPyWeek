#Python program to find the multiplication table(from 1 to 10) of a number input

#take input from the user

num=int(input("Display multiplication table of?"))

#use for loop to interate 10 times

for i in range(1,11):
	print num,"x",i,"=",num*i