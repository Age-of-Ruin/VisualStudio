# RichardConstantineA1Q3
#
# COMP 1012 SECTION A01
# INSTRUCTOR Terry Andres
# ASSIGNMENT: A1 Question 3
# AUTHOR Richard Constantine
# VERSION [Date of last change: 2013-Oct-1]
#
# PURPOSE: To use repeating fractions to approximate the value of the square
# root of two by iterating the fraction multiple times. Ratio values are  
# multiplied by 10^40 so as to minimize error by increasing the number of 
# accurate decimal places.

import math
import time

intConversion = 10**40 # for integer calculations
count = 0 # counting the iterations
ratio = 1 # ratio between terms in the numerator and denominator
prevRatio = 0 # track ratio of previous iteration
currNumer = 0 # current numerator value (ni)
currDenom =0 # current denominator value (di)
numerm1 = 1 # the ni-1 value
denomm1 = 0 # the di-1 value
numerm2 = 0 # the ni-2 value
denomm2 = 1 # the di-2 value
qn = 1 # integer coefficent

print "\nEvaluating the Square Root of 2 Using Continued Fractions"
print "\n"

while ratio != prevRatio  :

    count += 1
    
    prevRatio = ratio
    
    currNumer = qn * numerm1 + numerm2  # numerator calculation
    currDenom = qn * denomm1 + denomm2 # denominator calculation
    
    ratio = (currNumer) * intConversion / currDenom # converted ratio
    
    qn = 2 
    
    numerm1, numerm2 = currNumer, numerm1 # numer-1 becomes currNumer
                                          #and numer-2 becomes numer-1    
    denomm1, denomm2 = currDenom, denomm1 #denom-1 becomes currDenom
                                          #denom-2 becomes denom-1
    
    print ("%3d: 10^40 times the square root of 2 is about %40d" %
           (count, ratio) ) # print approximation

print "\nThe square of the approximation:" # print approximation**2
print ratio**2

print "\nProgrammed by Richard Constantine"
print time.ctime()
print "End of Processing" 