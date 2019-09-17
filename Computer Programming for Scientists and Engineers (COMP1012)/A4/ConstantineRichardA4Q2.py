# ConstantineRichardA4Q2
#
# COMP 1012 SECTION A01
# INSTRUCTOR Terry Andres
# ASSIGNMENT: A4 Question 2
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
    
DENSITY = 7.850 # [g/cm^3]    
    
def theEnd() :
    """Ends the program with summary message."""
    
    print "\nProgrammed by Richard Constantine"
    print time.ctime()
    print "End of Processing"

def linearSeg(x0, y0, x1, y1) :
    """Organizes x and y values for plotting"""
    
    xs = [x0, x1]
    ys = [y0, y1]
    
    lineSeg = (xs, ys)
    
    return lineSeg

def arc(xCentre, yCentre, radius, startDeg, endDeg) :
    """Creates a circular arc by calculating sin and cos or each 1 degree 
       interval in the curve"""

    angles = np.linspace(startDeg, endDeg+3, abs(endDeg+4 - startDeg))
        
    rads = angles * math.pi/180.
    
    xList = list(xCentre + (radius * np.cos(rads)))
    yList = list(yCentre + (radius * np.sin(rads)))
        
    curve = (xList, yList)

    return curve

def rotate(shape, angle, xCentre, yCentre) :
    """Rotates entire plot with given angle of rotation around the center 
       trunnion hole"""

    title = shape[0]
    title = "Rotated " + title
    
    shapeRotated = shape # create new shape
    shapeRotated = list(shapeRotated) # cast to list to assign new title
    shapeRotated[0] = title
    shapeRotated = tuple(shapeRotated) # cast shape back to tuple
    
    numCurves = len(shape[1])
    rads = (angle * math.pi) / 180.
    
    xList = []
    xArray = 0
    yList = []
    yArray = 0
    newX = []
    newY = []
    
    for curve in range(0, numCurves) :
        
        xArray = np.array(shape[1][curve][0]) # cast x value list to array
        xList.append(xArray) # create list of x arrays
        
    xVals = np.array(xList) # cast list to array (for easy computation)
    
    for curve in range (0, numCurves) :
        
        yArray = np.array(shape[1][curve][1])
        yList.append(yArray)
        
    yVals = np.array(yList)
                                    # perform rotation computation
    xPrime = (xCentre + (xVals - xCentre) * math.cos(rads) - (yVals - yCentre) 
             * math.sin(rads))
             
    
    yPrime = (yCentre + (xVals - xCentre) * math.sin(rads) + (yVals - yCentre) 
             * math.cos(rads))
    
    for curve in range(0, numCurves) :
        
        shapeRotated[1][curve] = list(shapeRotated[1][curve]) # cast curves to 
                                                        # list to make mutable
                                                            
        newX = list(xPrime[curve])# cast array to orignal list form
        
        shapeRotated[1][curve][0] = newX # replace vals with rotated vals
        
    for curve in range(0, numCurves) :
        
        newY = list(yPrime[curve])
    
        shapeRotated[1][curve][1] = newY
        
        shapeRotated[1][curve] = tuple(shapeRotated[1][curve]) # cast back to 
                                                               # tuple
    return shapeRotated 
    

def crop (curve, xlo, xhi, ylo, yhi) :
    """Slices xs and ys of curve to form smaller segments"""
    
    xs = curve[0]
    ys = curve[1]
    
    xVals = []
    yVals = []
    
    for x in xs :
    
        xcropped = max(min(x, xhi), xlo) # maintain all x and y within bounds
            
        xVals.append(xcropped)
            
    for y in ys:
        
        ycropped = max(min(y, yhi), ylo)
    
        yVals.append(ycropped)
     
    croppedCurve = (xVals, yVals)
    
    return croppedCurve
     
def shrink(curve, factor) :
    """Shrinks shape by adjusting x and y values by a shrink factor"""
    
    xArray = np.array(curve[0])
    yArray = np.array(curve[1])
    
    xShrink = list((xArray - np.min(xArray)) * factor + np.min(xArray))
    yShrink = list((yArray - np.min(yArray)) * factor + np.min(yArray))

    curveShrink = (xShrink, yShrink)
    
    return curveShrink

def mirror(curve):
    """Mirrors all x values to reflect shape across y axis"""
    
    xs = np.array(curve[0]) 
    ys = list(curve[1])
    
    xs = list(xs * -1)
    
    mirroredCurve = (xs, ys)
    
    return mirroredCurve
    
def holeOutline(radius) :
    """Produces plottable values for a circle"""
    
    holeOutline = arc(0, 0, radius, 0, 360)
    
    return holeOutline
    
def trunnionBracketOutline(width) :
    """Forms the details(x and y values) needed to plot the outline of the 
       bracket""" 
    
    base = linearSeg(-width/3., 0, width/3., 0)
    rightSide = linearSeg(width/2., width/6., width/2., width/2.)
    rightUpper = linearSeg(width/2., width/2., width/6., (5/6.) * width)
    leftUpper = linearSeg(-width/6., (5/6.) * width, -width/2., width/2.)
    leftSide = linearSeg(-width/2., width/2., -width/2., width/6.)
    
    
    brcArc = arc(width/3., width/6., width/6., -90, 0)
    topArc = arc(0, (3/4.) * width, width/(4. * math.sqrt(2)), 45, 135)
    blcArc = arc(-width/3., width/6., width/6., 180, 270)
    
    xVals = (base[0] + brcArc[0] + rightSide[0] + rightUpper[0] + topArc[0] +
            leftUpper[0] + leftSide[0] + blcArc[0])
    yVals = (base[1] + brcArc[1] + rightSide[1] + rightUpper[1] + topArc[1] + 
            leftUpper[1] + leftSide[1] + blcArc[1])
    
    curve = (xVals, yVals)
    
    return curve

def pathCopy(curve, xOffset, yOffset) :
    """Adjusts specific shape to a specific position"""
    
    xArray = np.array(curve[0])
    yArray = np.array(curve[1])
    
    xModded = list(xArray + xOffset)
    yModded = list(yArray + yOffset)
    
    curveModded = (xModded, yModded)

    return curveModded

def trunnionBracket(width) :
    """Returns a shape in the form of a list of details, i.e x and y values
       neccessary to draw the trunnion bracket"""
    
    title = "Trunnion Bracket of width %d" %width  
    
    bracketOutline = trunnionBracketOutline(width)
    
    trunHoleOutline = holeOutline(width/15)
    trunHole = pathCopy(trunHoleOutline, 0, (3/4.) * width)
    
    boltHoleOutline = holeOutline(width/18)
    midHole = pathCopy(boltHoleOutline, -width/3., width/6.)
    leftHole = pathCopy(boltHoleOutline, 0, width/6.)
    rightHole = pathCopy(boltHoleOutline, width/3., width/6.)
    
    cutoutA = crop(bracketOutline, 0, width, 0, width)
    cutoutA = shrink(cutoutA, .35)
    cutoutA = pathCopy(cutoutA, .15 * width, .31 * width)
    
    cutoutB = mirror(cutoutA)
    
    diagram = [bracketOutline, trunHole, midHole, leftHole, rightHole, 
              cutoutA, cutoutB] 
    
    shape = (title, diagram)
    
    return shape

def drawDiagram(shape, label, format, xOffset=0, yOffset=0) :
    """Plots the trunnion bracket with information from trunnionBracket"""
    
    plt.title(shape[0])
    plt.xlabel("x")
    plt.ylabel("y")
    
    firstX = 0.0
    firstY = 0.0
    arrayX = 0
    arrayY = 0
    
    # plot outline
    outlineXs, outlineYs = shape[1][0][0], shape[1][0][1]
    
    firstX, firstY = outlineXs[0], outlineYs[0]           # ensures closed curve
    outlineXs.append(firstX), outlineYs.append(firstY)    # ------------------
    
    arrayX, arrayY = np.array(outlineXs), np.array(outlineYs) # add offsets
    outlineXs, outlineYs = list(arrayX + xOffset), list(arrayY + yOffset) # --
    
    plt.plot(outlineXs, outlineYs, format, label=label) 

    # plot trunnion Hole
    trunHoleXs, trunHoleYs = shape[1][1][0], shape[1][1][1]
    firstX, firstY = trunHoleXs[0], trunHoleYs[0]
    trunHoleXs.append(firstX), trunHoleYs.append(firstY)
    
    arrayX, arrayY = np.array(trunHoleXs), np.array(trunHoleYs)
    trunHoleXs, trunHoleYs = list(arrayX + xOffset), list(arrayY + yOffset)
    
    plt.plot(trunHoleXs, trunHoleYs, format) 
    
    # plot middle bolt hole
    midHoleXs, midHoleYs = shape[1][2][0], shape[1][2][1]
    firstX, firstY = midHoleXs[0], midHoleYs[0]
    midHoleXs.append(firstX), midHoleYs.append(firstY)
    
    arrayX, arrayY = np.array(midHoleXs), np.array(midHoleYs)
    midHoleXs, midHoleYs = list(arrayX + xOffset), list(arrayY + yOffset)
    
    plt.plot(midHoleXs, midHoleYs, format) 
    
    # plot left bolt hole
    leftHoleXs, leftHoleYs = shape[1][3][0], shape[1][3][1]
    firstX, firstY = leftHoleXs[0], leftHoleYs[0]
    leftHoleXs.append(firstX), leftHoleYs.append(firstY)
    
    arrayX, arrayY = np.array(leftHoleXs), np.array(leftHoleYs)
    leftHoleXs, leftHoleYs = list(arrayX + xOffset), list(arrayY + yOffset)
    
    plt.plot(leftHoleXs, leftHoleYs, format) 
    
    # plot right bolt hole
    rightHoleXs, rightHoleYs = shape[1][4][0], shape[1][4][1]
    firstX, firstY = rightHoleXs[0], rightHoleYs[0]
    rightHoleXs.append(firstX), rightHoleYs.append(firstY)
    
    arrayX, arrayY = np.array(rightHoleXs), np.array(rightHoleYs)
    rightHoleXs, rightHoleYs = list(arrayX + xOffset), list(arrayY + yOffset)
    
    plt.plot(rightHoleXs, rightHoleYs, format) 
    
    # plot cutout A
    firstCutoutXs, firstCutoutYs = shape[1][5][0], shape[1][5][1]
    firstX, firstY = firstCutoutXs[0], firstCutoutYs[0]
    firstCutoutXs.append(firstX), firstCutoutYs.append(firstY)
    
    arrayX, arrayY = np.array(firstCutoutXs), np.array(firstCutoutYs)
    firstCutoutXs, firstCutoutYs = list(arrayX + xOffset), list(arrayY + yOffset)
    
    plt.plot(firstCutoutXs, firstCutoutYs, format) 
    
    # plot cutoutB
    secondCutoutXs, secondCutoutYs = shape[1][6][0], shape[1][6][1]
    firstX, firstY = secondCutoutXs[0], secondCutoutYs[0]
    firstCutoutXs.append(firstX), firstCutoutYs.append(firstY)
    
    arrayX, arrayY = np.array(secondCutoutXs), np.array(secondCutoutYs)
    secondCutoutXs, secondCutoutYs = list(arrayX + xOffset), list(arrayY + yOffset)
    
    plt.plot(secondCutoutXs, secondCutoutYs, format) 

def areaOfClosedCurve(curve) :
    """Evaluates the area under function using the sum of trapazoidal intervals"""
    
    xVals = curve[0]                               
    yVals = curve[1]
    
    firstX, firstY = curve[0][0], curve[0][1]            # ensures closed curve
    xVals.append(firstX), yVals.append(firstY)            # ------------------
    
    xArray = np.array(xVals)
    yArray = np.array(yVals)
    
    area = abs(0.5 * np.sum((xArray[1:] - xArray[:-1]) * (yArray[1:] + yArray[:-1])))
    
    return area

def areaOfShape(shape) :
    """Calculates the area of a shape by subtracting the area of the outline
       from the area of any constituent shape"""
       
    areaList = []
    
    for curve in shape[1] :
        
        area = areaOfClosedCurve(curve)
        
        areaList.append(area)
    
    areaArray = np.array(areaList)
    
    outlineArea = np.max(areaArray, 0.)
    constituentArea = np.sum(areaArray) - outlineArea
    
    area = float(outlineArea - constituentArea)
    
    return area    
        
def main() :
    """Main Script"""
    
    # User Input
    width = float(raw_input("Enter the width of a trunnion bracket [cm]: "))
    
    thickness = float(raw_input(
                "Enter the thickness of the trunnion bracket [mm]: "))
    
    rotateAngle = int(raw_input("Enter angle to rotate the bracket [deg]: "))
    
    label = "..."
    labelR = "+%d degrees" % rotateAngle
    labelL = "-%d degrees" % rotateAngle
    standardFormat = ".-b"
    rotatedFormatL = "-r"
    rotatedFormatR = "-g"
    
    # Draw shapes and subplots
 
    fig = plt.figure(1);                  plt.clf()
    
    shape = trunnionBracket(width)
    fig.add_subplot(211, aspect='equal')
    drawDiagram(shape, label, standardFormat, 0, 1)
    
    fig.add_subplot(212,aspect='equal')
    
    shape = trunnionBracket(width)
    shape = rotate(shape, rotateAngle, 0, (3/4.) * width)
    drawDiagram(shape, labelR, rotatedFormatR, 0, 1)
    
    shape = trunnionBracket(width)
    shape = rotate(shape, -rotateAngle, 0, (3/4.) * width)
    drawDiagram(shape, labelL, rotatedFormatL, 0, 1)

    print ("\nPlotting a trunnion bracket rotated plus/minus %.1f degrees"
            % (rotateAngle))
            
    print "\nComputing area of trunnion bracket..."
    
    # Area and Mass Calculations
    area = areaOfShape(shape)
    thicknessCM = thickness/10.
    massG = (area * thicknessCM) * DENSITY
    massKG = massG/1000.
    
    print ("\nThe area of a trunnion bracket width %2.1f cm is %d cm^2."
            %(width, round(area, 0)))
    
    print ("\nAssuming hardened steel with density %r g/cm^3"
            "\nThe mass of a trunnion bracket of thickness %r mm is %r kg."
            % (DENSITY, thickness, round(massKG, 2)))    
    
    plt.legend(fontsize=10)
    
    plt.show()

    theEnd()
    
main()