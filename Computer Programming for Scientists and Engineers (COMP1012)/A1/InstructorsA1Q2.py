# InstructorsA1Q2
#
# COMP 1012  SECTION A01
# INSTRUCTOR Terry Andres
# ASSIGNMENT: A1 Question 2
# AUTHOR    T.H. Andres
# VERSION   2013-Sep-03
#
# PURPOSE: To evaluate sample formulas.

import math
import time

print "A. Response Function for Radionuclide Transport"
print
XX = 10.0 # [m] position in flow-path
TT = 1000. # [year] time of measurement
VV = 0.001 # [m/year] water velocity
DD = 0.002 # [m^2/year] hydrodynamic dispersion coefficient
KK = 2.0   # [-] retardation coefficient
LAMBDA = 0.0012 # [1/year] rate of radionuclide decay

COEF_A = XX * math.sqrt(KK / DD) # [year^0.5] coefficient A
COEF_C = VV**2 / (4.0 * DD * KK) + LAMBDA # [1/year] coefficient C
R_X_T = (COEF_A / (2.0 * math.sqrt(math.pi * TT**3)) 
        * math.exp(VV * XX / (2.0 * DD) - COEF_C * TT - COEF_A**2 / (4.0 * TT)))
        
print "INPUT VALUES"
print "       Flow path distance x: %9.3f  \t[m]" % XX
print "                     Time t: %5.0f\t\t[year]" % TT
print "           Water velocity V: %12.6f\t[m/year]" % VV
print "  Hydrodynamic dispersion D: %12.6f\t[m^2/year]" % DD
print "  Retardation coefficient K: %9.3f\t\t[-]" % KK
print "      Decay constant lambda: %12.6f\t[1/year]" % LAMBDA

print "\nCALCULATED VALUES"
print "                          A: %7.1f\t\t[year^0.5]" % COEF_A
print "                          C: %12.6f\t[1/year]" % COEF_C
print "                     R(x,t): %13.3e\t[1/year]" % R_X_T


print "\nB. Volume, Mass and Density of a Sledgehammer"
print
HANDLE_LENGTH = 98.2 # [cm] length of handle
HANDLE_BIG_AXIS = 3.5 # [cm] max thickness of handle
HANDLE_WEE_AXIS = 2.8 # [cm] min thickness of handle
HANDLE_DENSITY = 0.719 # [g/cm^3] density of white ash wood

HANDLE_AREA = math.pi * HANDLE_BIG_AXIS * HANDLE_WEE_AXIS / 4.0 # [cm^2]
HANDLE_VOL = HANDLE_AREA * HANDLE_LENGTH # [cm^3]
HANDLE_MASS = HANDLE_VOL * HANDLE_DENSITY # [g]

HEAD_BLOCK = 4.5 # [cm] size of centre block of head
HEAD_CYL_RADIUS = 2.25 # [cm] radius of each head cyclindrical part
HEAD_CYL_LENGTH = 4.0 # [cm] length of each head cyclindrical part
HEAD_DENSITY = 7.850 # [g/cm^3] density of heat hardened steel

HEAD_BLOCK_VOL = HEAD_BLOCK**3 - HANDLE_AREA * HEAD_BLOCK # [cm^3]
HEAD_CYL_VOL   = HEAD_CYL_RADIUS**2 * math.pi * HEAD_CYL_LENGTH # [cm^3]
HEAD_VOL =  HEAD_BLOCK_VOL + 2.0 * HEAD_CYL_VOL # [cm^3]
HEAD_MASS = HEAD_VOL * HEAD_DENSITY # [g]

HAMMER_VOL = HANDLE_VOL + HEAD_VOL # [cm^3]
HAMMER_MASS = HANDLE_MASS + HEAD_MASS # [g]
HAMMER_DENSITY = HAMMER_MASS / HAMMER_VOL # [g/cm^3]

print "HANDLE PROPERTIES"
print "                Length: %8.1f\t[cm]" % HANDLE_LENGTH
print "              Big axis: %8.1f\t[cm]" % HANDLE_BIG_AXIS 
print "            Small axis: %8.1f\t[cm]" % HANDLE_WEE_AXIS 
print "               Density: %10.3f\t[g/cm^3]" % HANDLE_DENSITY
print "  Cross sectional area: %9.2f\t[cm^2]" % HANDLE_AREA 
print "                Volume: %8.1f\t[cm^3]" % HANDLE_VOL
print "                  Mass: %8.1f\t[g]" % HANDLE_MASS

print "\nHEAD PROPERTIES"
print "     Centre block size: %8.1f\t[cm]" % HEAD_BLOCK
print "       Cylinder radius: %9.2f\t[cm]" % HEAD_CYL_RADIUS 
print "       Cylinder length: %9.2f\t[cm]" % HEAD_CYL_LENGTH 
print "               Density: %10.3f\t[g/cm^3]" % HEAD_DENSITY
print "                Volume: %8.1f\t[cm^3]" % HEAD_VOL
print "                  Mass: %7.0f\t\t[g]" % HEAD_MASS

print "\nHAMMER PROPERTIES"
print "                Volume: %8.1f\t[cm^3]" % HAMMER_VOL
print "                  Mass: %6.0f\t\t[g]" % HAMMER_MASS
print "               Density: %10.3f\t[g/cm^3]" % HAMMER_DENSITY




print "\n\nProgrammed by Terry Andres"
print "Date: " + time.ctime()
print "End of processing"


