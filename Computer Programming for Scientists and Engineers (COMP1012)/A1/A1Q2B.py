# RichardConstantineA1Q2B
#
# COMP 1012 SECTION A01
# INSTRUCTOR Terry Andres
# ASSIGNMENT: A1 Question 2B
# AUTHOR Richard Constantine
# VERSION [Date of last change: 2013-Oct-1]
#
# PURPOSE: Calculate properties of a sledge hammer (volume, mass and average
# density) and display these values using the print function to format output.

import math
import time

#Handle Properties
LOFHANDLE = 98.2 # [cm]
BIGAXIS = 3.5 # [cm]
SMALLAXIS = 2.8 # [cm]
DOFHANDLE = .719 # [g/cm^3]

#Calculated Values
AOFHANDLE = math.pi * BIGAXIS * SMALLAXIS / 4 # [cm^2]
AOFHandRound = round (AOFHANDLE, 2) # area adjusted to appropriate sig figs
VOFHANDLE = AOFHandRound * LOFHANDLE # [cm^3]
VOFHandRound = round (VOFHANDLE, 1) # volume adjusted
MOFHANDLE = DOFHANDLE * VOFHandRound # [g]
MOFHandRound = round (MOFHANDLE, 1) # mass adjusted

#Head Properties
CENTRESIZE = 4.5 # [cm]
ROFCYLINDER = 2.25 # [cm]
LOFCYLINDER = 4.00 # [cm]
DOFHEAD = 7.850 # [g/cm^3]

#Calculated Values
AOFCYLINDER = math.pi * (2 * ROFCYLINDER)**2 / 4 # [cm^2]
AOFCylRound = round(AOFCYLINDER, 1) # C.S. area of cylinder adjusted
VOFCYLINDER = LOFCYLINDER * AOFCylRound  # [cm^3]
VOFCylRound = round(VOFCYLINDER, 1) # volume of cylinder adjusted
VOFHEAD = ( (CENTRESIZE**3 - (AOFHandRound * CENTRESIZE)) + 
                2 * VOFCylRound) # [cm^3]
VOFHeadRound = round(VOFHEAD, 1) # volume of head adjusted
MOFHEAD = DOFHEAD * VOFHEAD # [g]
MOFHeadRound = round(MOFHEAD, 0) # mass of head adjusted

#Hammer Properties
VOFHAMMER = VOFHEAD + VOFHANDLE # [cm^3]
VOFHAMRound = round (VOFHAMMER, 1) # volume of hammer adjusted
MOFHAMMER = MOFHEAD + MOFHANDLE # [g]
MOFHAMRound = round(MOFHAMMER, 0) # mass of hammer adjusted
DOFHAMMER = MOFHAMMER / VOFHAMMER # [g/cm^3]
DOFHAMRound = round(DOFHAMMER, 3) # density of hammer


#Print Title
print ("\nB. Volume, Mass and Density of a Sledgehammer")
print ("\nHandle Properties")

#Print Handle Properties
print ("\n\t %20s" "%11.1f" "\t %11s" % 
       ("Length:", LOFHANDLE, "[cm]") )

print ("\t %20s" "%11.1f" "\t %11s" %
       ("Big Axis:", BIGAXIS, "[cm]") )

print ("\t %20s" "%11.1f" "\t %11s" %
       ("Small Axis:", SMALLAXIS, "[cm]") )

print ("\t %20s" "%13.3f" "\t %15s" %
       ("Density of Handle:", DOFHANDLE, "[g/cm^3]") )

print ("\t %20s" "%12.2f" "\t %13s" %
       ("C.S. Area of Handle:", AOFHandRound, "[cm^2]") )

print ("\t %20s" "%11.1f" "\t %13s" %
       ("Volume of Handle:", VOFHandRound, "[cm^3]") )
          
print ("\t %20s" "%11.1f" "\t %10s" %
       ("Mass of Handle:", MOFHandRound, "[g]") )


#Print Head Properties
print ("\nHead Properties")

print ("\t %20s" "%11.1f" "\t %11s" % 
        ("Centre Block Size:", CENTRESIZE, "[cm]") )
       
print ("\t %20s" "%12.2f" "\t %11s" % 
        ("Cylinder Radius:", ROFCYLINDER, "[cm]") )

print ("\t %20s" "%12.2f" "\t %11s" % 
        ("Cylinder Length:", LOFCYLINDER, "[cm]") )

print ("\t %20s" "%13.3f" "\t %15s" % 
        ("Density of Head:", DOFHEAD, "[g/cm^3]") )
       
print ("\t %20s" "%12.2f" "\t %14s" % 
        ("Cylinder Area:", AOFCYLINDER, "[cm ^2]") )

print ("\t %20s" "%12.2f" "\t %14s" % 
        ("Cylinder Volume:", VOFCYLINDER, "[cm ^3]") )

print ("\t %20s" "%11.1f" "\t %13s" % 
        ("Volume of Head:", VOFHEAD, "[cm^3]") )

print ("\t %20s" "%9.0f" "\t %18s" % 
        ("Mass of Head:", MOFHEAD, "[g]") )


#Print Total Hammer Properties
print ("\nHammer Properties")

print ("\t %20s" "%11.1f" "\t %13s" % 
        ("Volume:", VOFHAMMER, "[cm^3]") )
       
print ("\t %20s" "%9.0f" "\t %18s" % 
        ("Mass:", MOFHAMMER, "[g]") )

print ("\t %20s" "%13.3f" "\t %15s" % 
        ("Density:", DOFHAMMER, "[g/cm^3]") )


print "\nProgrammed by Richard Constantine"
print time.ctime()
print "End of Processing"


