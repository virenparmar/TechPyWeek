# Python Program to display calender of given month of the year

#import module

import calendar

#assk of month and year

yy=int(input("Enter the year="))
mm=int(input("Enter the month="))

#display the calender

print(calendar.month(yy,mm))