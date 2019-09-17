# RichardConstantineA1Q4
#
# COMP 1012 SECTION A01
# INSTRUCTOR Terry Andres
# ASSIGNMENT: A1 Question 4
# AUTHOR Richard Constantine
# VERSION [Date of last change: 2013-Oct-1]
#
# PURPOSE: Approximate exp(x), cos (x) and sin(x) by using infinite series
# as well as evalute exp(x j) where j is the root of -1 and x is my student
# number / 10**7.

import math
import cmath
import time

#Constants
SNUMBER = 7686561.0  # student number
X_ = SNUMBER / 10**7 # divide SNUMBER by 10,000,000
EPS = 1.e-20 # epsilon (very small number)
X_COMPLEX = X_ * 1.0j # complex version of SNUMBER (SNUMBER * j)

#Print title
print "\nEvaluating exp, cos and sin series for student number %d" %SNUMBER
print "\n"
print "\tx value is %r" %X_ # print x
print "\teps = %r" %EPS  # print epsilon


#Exp Calculations
expCount = 0 # counting the iterations
expTotal = 0.0 # totals series
expTerm = 1.0 # current term
EXPMATH = math.exp(X_) # exp math function

while abs(expTerm) > EPS  :

    expCount += 1 # iterate count
    
    expTotal += expTerm # total sums terms
    
    expTerm = expTerm * X_ / float(expCount) # next term
    
print "\tseries.exp(x) = %r" %expTotal # print exp total
print "\t  math.exp(x) = %r" %EXPMATH # print exp math function


#Cos Calculations
cosCount = 0 # counting the iterations
cosTotal = 0.0 # totals series
cosTerm = 1.0 # current term
COS_MATH = math.cos(X_) # cos math function

while abs(cosTerm) > EPS  :

    cosCount += 1 # iterate count
    
    cosTotal += cosTerm # total sums terms
    
    cosTerm = ( -(cosTerm * X_**2 / (2. * float(cosCount) - 1) ) / 
                  (2  * float(cosCount) ) ) # next term
    
print "\n\tseries.cos(x) = %r" %cosTotal # print cos total
print "\t  math.cos(x) = %r" %COS_MATH # print cos math function


#Sin Calculations
sinCount = 0 # counting the iterations
sinTotal = 0.0 # totals series
sinTerm = X_ # current term
SIN_MATH = math.sin(X_) # sin math function

while abs(sinTerm) > EPS  :

    sinCount += 1 # iterate count
    
    sinTotal += sinTerm # total sums terms
    
    sinTerm = -(sinTerm  * (X_**2 / (2 * float(sinCount) + 1) ) /
                (2 * float(sinCount) ) ) # next term
    
print "\n\tseries.sin(x) = %r" %sinTotal # print sin total
print "\t  math.sin(x) = %r" %SIN_MATH # print sin math function


#Sum of Squares Calulations
SUMOFSQUARES = sinTotal**2 + cosTotal**2 # S. of S. formula

print ("%24s" "%r") %("cos(x)**2 + sin(x)**2 = ", SUMOFSQUARES)


#Complex Exp Calculations
cExpCount = 0 # counting the iterations
cExpTotal = 0.0 # totals series
cExpTerm = 1.0# current term
cEXPMATH = cmath.exp(X_COMPLEX) # complex exp math function


while abs(cExpTerm) > EPS  :

    cExpCount += 1 # iterate count
    
    cExpTotal += cExpTerm # total sums terms
    
    cExpTerm = cExpTerm * X_COMPLEX / float(cExpCount) # next term

print "\n\tseries.exp(x j) = %r" %cExpTotal # print complex exp total
print "\t  math.exp(x j) = %r" %cEXPMATH # print complex exp math function


#Cos(x) + jsin(x)
cosJsin = cosTotal + sinTotal * 1.0j # cos(x) + jsin(x) formula
print ("%26s" "%r") %("cos(x) + jsin(x) = ", cosJsin) 


#Difference
difference = abs(cExpTotal) - abs(cosJsin)
print ("%26s" "%r") %("|difference| = ", difference) 


print "\nProgrammed by Richard Constantine"
print time.ctime()
print "End of Processing"