# -*- coding: utf-8 -*-
# ConstantineRichardA4Q2
#
# COMP 1012 SECTION A01
# INSTRUCTOR Terry Andres
# ASSIGNMENT: A4 Question 3
# AUTHOR Richard Constantine
# VERSION [Date of last change: 2013-Nov-1]
#
# PURPOSE: To construct an interactive program that plots a trunnion bracket
# and calculates the area and mass from a user input of the width, thickness, 
# degree of rotation(for plot) and the assumed density of 7.850g/cm^3 of
# hardened steel.


import math
import time
import numpy as np
import matplotlib.pyplot as plt    
    
def theEnd() :
    """Ends the program with summary message."""
    
    print "\nProgrammed by Richard Constantine"
    print time.ctime()
    print "End of Processing"

def circle(xpos) :
    """Evalutes the the top curve of a circle using x-coordinate""" 
    
    yPos = np.array(np.sqrt(1 - xpos**2))
    
    return yPos

def areaUnderCurve(left, right, fcn, numberOfIntervals) :
    """Evaluates the area under function using the sum of trapazoidal intervals"""
    
    xVals = np.linspace(left, right, numberOfIntervals + 1) #numIntervals + 1 
                                                            # in num of values
    yVals = fcn(xVals)                                      # being evaluated
    
    coefficient = float(xVals[1] - xVals[0]) / 2 # equal spaced intervals
    
    
    sumFxAndFxplus1 = np.sum(yVals[1:]) + np.sum(yVals[:-1])
    
    #sumFxAndFxplus1 = np.sum(yVals[0:len(xVals):1]) + np.sum(yVals[1:len(xVals):1])
            # my alternate method
    
    areaUnderCurve = coefficient * sumFxAndFxplus1
    
    return areaUnderCurve

def main() :
    """Main Script"""
    
    decimalPrompt = "Enter the number of decimal places for pi: " 
    intervalPrompt = "Enter the number of intervals to use to start: " 
    
    numDecPlaces = raw_input(decimalPrompt) 
    numIntervals = raw_input(intervalPrompt) 
    intNumDecPlaces = int(numDecPlaces) + 1 # one extra dec space 
    intNumIntervals = int(numIntervals) 
    
    print "\n" 
   
    aa = 0 
    bb = 1 
    
    piRounded = round(math.pi, intNumDecPlaces) 
    piEstimate = 0.0 
    piEstRounded = 0.0
    
    while piEstRounded != piRounded : 
        
        piEstimate = 4 * areaUnderCurve(aa, bb, circle, intNumIntervals) 
        piEstRounded = round(piEstimate, intNumDecPlaces) 
        
        print ("Using %12d intervals, the estimate of pi is: %r" 
               % (intNumIntervals, piEstRounded)) 
        
        intNumIntervals *= 2 
        
    print "\t\t\t\t The value of pi is: %r" %piEstRounded 
        
    # shell commands: 
    # areaUnderCurve(1.0, 100.0, np.log, 10000) 
    # 100. * (math.log(100.) - 1.) + 1.    
    
    theEnd()
    
main()