# InstructorsA1Q4
#
# COMP 1012  SECTION A01
# INSTRUCTOR Terry Andres
# ASSIGNMENT: A1 Question 4
# AUTHOR    T.H. Andres
# VERSION   2013-Sep-03
#
# PURPOSE: To evaluate sample formulas.

import math
import cmath
import time

STUD_NUMBER = 1234567
print "Evaluating exp, cos and sin series for student number %d" % STUD_NUMBER


# Calculate x
xx = STUD_NUMBER / 1e7
xsq = xx * xx
print "\n  x value is %s" % xx

eps = 1.e-20
print "  eps = %s" % eps

# exp function
count = 0 
total = 0
term = 1
while abs(term) > eps :
    total += term
    count += 1
    term = term * xx / count
    
print "  series exp(x) = %r" % total
print "    math.exp(x) = %r" % math.exp(xx)

# cos function
count = 0 
cosTotal = 0
term = 1
while abs(term) > eps :
    cosTotal += term
    count += 2
    term = -term * xsq / count / (count - 1)
    
print "\n  series cos(x) = %r" % cosTotal
print "    math.cos(x) = %r" % math.cos(xx)

# sin function
count = 0 
sinTotal = 0
term = xx
while abs(term) > eps :
    sinTotal += term
    count += 2
    term = -term * xsq / count / (count + 1)
    
print "\n  series sin(x) = %r" % sinTotal
print "    math.sin(x) = %r" % math.sin(xx)
print "sin**2 + cos**2 = %r" % (sinTotal**2 + cosTotal**2)

# complex exp function
xx = complex(0,xx)
count = 0 
total = 0
term = 1
while abs(term) > eps :
    total += term
    count += 1
    term = term * xx / count
    
print "\n    series exp(x j) = %r" % total
print "     cmath.exp(x j) = %r" % cmath.exp(xx)
expXj = complex(cosTotal, sinTotal)
print "  cos(x) + j sin(x) = %r" % expXj
diffMag = abs(expXj - cmath.exp(xx))
print "       |difference| = %s" % diffMag


print "\n\nProgrammed by The Instructors"
print "Date: " + time.ctime()
print "End of processing"