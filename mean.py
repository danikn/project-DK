# print the mean of the numbes given in a file
import sys

sum = 0
x = 0

# x instaed of n

#Sum input values
for num in open('data.txt'):
	sum += float(num)
	x += 1


#output:
print sum / x


print x


