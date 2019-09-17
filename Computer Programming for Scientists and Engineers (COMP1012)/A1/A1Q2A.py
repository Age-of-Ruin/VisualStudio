# RichardConstantineA1Q2A
#
# COMP 1012 SECTION A01
# INSTRUCTOR Terry Andres
# ASSIGNMENT: A1 Question 2A
# AUTHOR Richard Constantine
# VERSION [Date of last change: 2013-Oct-1]
#
# PURPOSE: To compute the function of R(x,t), the fraction of time it takes 
# a radioactive element to flow past a predetermined point in space
# along a path where all elements move in the same direction (homogenous).
 
import math
import time

X_ = 10.00 #[m] distance along flow path
T_ = 1000 #[y] time of given radioactive element in motion
V_ = .001000 #[m/year] water velocity
D_ = .002000 #[m^2/year] hydrodynamic dispersion
K_ = 2.000 #[-] retardation coeffecient
DECAY = .001200 #[1/year]

A_ = (math.sqrt(K_ / D_)) * X_

C_ = ((V_**2 / 4 * D_ * K_) + DECAY) 

term1 = (A_) / (2.0 * math.sqrt(math.pi * T_**3)) # first term in R(x,t) formula

bracketA = (V_ * X_) / (2 * D_) # first term in square brackets
bracketB = (C_ * T_) # second term
bracketC = (A_**2) / (4 * T_) # third term

R_ = term1 * math.exp(bracketA - bracketB - bracketC)


print ("\nA. Response Function for Radionuclide Transport")
print ("\nInput Values:")

print ("\t %29s" "%8.2f" "\t %11s" % 
       ("Flow Path Distance x:", X_, "[m]") )

print ("\t %29s" "%5d" "\t %14s" %
       ("Time t:", T_, "[year]") )

print ("\t %29s" "%12.6f" "\t %s" %
       ("Water Velocity V:", V_, "[m/year]") )

print ("\t %29s" "%12.6f" "\t %s" %
       ("Hydrodynamic Dispersion D:", D_, "[m^2/year]") )

print ("\t %s" "%9.3f" "\t %11s" %
       ("Retardation Coeffefficient K:", K_, "[-]") )

print ("\t %29s" "%12.6f" "\t %s" %
       ("Decay Constant Lambda:", DECAY, "[1/year]") )
       

print ("\nCalculated Values:")

print ("\t %29s" "%7.1f" "\t %18s" % 
        ("A:", A_, "[year^1/2]") )
       
print ("\t %29s" "%12.6f" "\t %8s" % 
        ("C:", C_, "[1/year]") )

print ("\t %29s" "%13.3e" "\t %8s" % 
        ("R(x, t):", R_, "[1/year]") )



print "\nProgrammed by Richard Constantine"
print time.ctime()
print "End of Processing"