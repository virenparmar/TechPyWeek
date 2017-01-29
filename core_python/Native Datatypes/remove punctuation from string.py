#Program to all punctuations from the string provided by the user

#define punctuation

punctuations='''!()-[]{};:'"\,<>./?@#$%^&*`~_'''

#take input from the user

my_str=input("Enter the string=")

#remove punctuations from thee string

no_punct=""

for char in my_str:
	if char not in punctuations:
		no_punct=no_punct+char

#display thee unpunctuated string
print(no_punct)