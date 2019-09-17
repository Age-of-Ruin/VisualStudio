# Instructors A1Q3
#
# COMP 1012  SECTION A01
# INSTRUCTOR Terry Andres
# ASSIGNMENT: A1 Question 3
# AUTHOR    T.H. Andres
# VERSION   2013-Sep-03
#
# PURPOSE: To evaluate  the square root of 2 using continued fractions.

import math
import time

NUMBER = 2
NUM_DIGITS = 40
print "Evaluating the Square Root of %d Using Continued Fractions" % NUMBER
print

# The next assignments are after the first step of the continued fraction for
# 2, which has coefficients 1, 2, 2, 2, 2, 2, 2, ...
COEF = 2
ncur = dcur = 1 # current numerator and denonimator in continued fraction
nprev = 1  # previous nominator
dprev = 0  # previous denominator
prevApprox = 0 # previous approximation to ratio
approx = 1  # current approximtion to ratio
count = 1
while approx != prevApprox :
    nprev, ncur = ncur, COEF * ncur + nprev
    dprev, dcur = dcur, COEF * dcur + dprev

    prevApprox = approx
    approx = 10**NUM_DIGITS * ncur // dcur
    
    print "%3d: 10**%d times square root of 2 is about %d" % (count, NUM_DIGITS, 
                                                        approx)
    count += 1
    
print "\nThe square of the approximation: %d" % approx**2


print "\n\nProgrammed by Terry Andres"
print "Date: " + time.ctime()
print "End of processing"


