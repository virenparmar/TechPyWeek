#Area Of Triangle

a=float(input('Enter the First Side='))
b=float(input('Enter the Second Side='))
c=float(input('Enter the Third Side='))

#Calculate Semi-perimeter

d=(a+b+c)/2

#Calculate the Area

area=(d*(d-a)*(d-b)*(d-c)) ** 0.5

print('The area of the triangle is %0.2f' %area)