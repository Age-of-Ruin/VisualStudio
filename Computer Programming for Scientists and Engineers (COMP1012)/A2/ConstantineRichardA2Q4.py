# RichardConstantineA2Q4
#
# COMP 1012 SECTION A01
# INSTRUCTOR Terry Andres
# ASSIGNMENT: A2 Question 4
# AUTHOR Richard Constantine
# VERSION [Date of last change: 2013-Oct-20]
#
# PURPOSE: Print a formatted, full-year calender for any year between 1900 and
# 9999.

import math
import time


FULL_MONTHS = ("January", "February", "March", "April", "May", "June",
"July", "August", "September", "October", "November", "December")

DAYS = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday")

#Define how to Calculate the Excel Date
def calcExcelDate(year, month, day=1) :
    
    totalYears = year - 1900 # years sinc 1900
    
    earlyMonthCorrect = math.floor ((14 - month) / 12) # corrects if month is
                                                       # jan or feb
    
    yearCorrected = totalYears - earlyMonthCorrect # year with EMC
    
    monthCorrected = month + 12 * earlyMonthCorrect  # month with EMC
    
    leapYears =  (1 + min(yearCorrected, 0) + math.floor(yearCorrected/4) -
                  math.floor(yearCorrected/100) + math.floor((yearCorrected
                  + 300) / 400)) # number of leap years since 1900
                  
    numDays = math.floor(-1.63 + (monthCorrected - 1) * 30.6) # days preceding
                                                              # month (non LY)
    
    excelDate = day + yearCorrected * 365 + leapYears + numDays # ExcelDate

    return excelDate

#Define function to calculate weekday from Excel date
def calcWeekDay(excelDate) :
    
    OFFSET = 6 # offset excelDate to give weekday
    
    excelDate = int(excelDate) 

    weekday = (excelDate + OFFSET) % 7

    return weekday

#Calculates the number of days in a given month
def daysInMonth(YEAR, MONTH) :

    intYear = int(YEAR)
    
    intMonth = int(MONTH) # integer value of month being calculated
    monthDay = 1 # first of the month
    
    nextMonth = intMonth + 1 # used in calculating Excel date of next month 
    nextMonthDay = 1 # first of next month
    
    exDofMonth = int(calcExcelDate(intYear, intMonth, monthDay))
    
    exDofNextMonth =  int(calcExcelDate(intYear, nextMonth, nextMonthDay))
    
    intNumofDays = exDofNextMonth - exDofMonth
    
    return intNumofDays

#Funtion that recieves integer month value and returns month name as string
def monthName(MONTH):

    intMonth = int(MONTH)
    
    monthTup = FULL_MONTHS
    
    monthName = monthTup[intMonth - 1] # index correct position
    
    return monthName
    
    
#Function that abbreviates day names to XXX format
def abrvDay(DAYS) :
    
    dayTup = DAYS
    abrvDayTup = ()
    day = ""
    
    for day in dayTup :
        
        abrvDayTup += (day[:3],)
        
    return abrvDayTup
    
#Define format calender function    
def formatCalendar(YEAR, MONTH):
    
    intYear = int(YEAR)
    intMonth = int(MONTH)
    
    firstOfMonth = 1 # first of everymonth
    abrvDayString = "" # declaration
    
    sundayString = ""                   
    mondayString = "\t"
    tuesdayString = "\t\t"
    wednesdayString = "\t\t\t"        # declarations with starting formatting
    thursdayString = "\t\t\t\t"
    fridayString = "\t\t\t\t\t"
    saturdayString = "\t\t\t\t\t\t"
    
    numDays = daysInMonth(intYear, intMonth) # calc numDays in given month
    
    nameofMonth = monthName(intMonth) # name given month
    
    excelDate = calcExcelDate(intYear, intMonth, firstOfMonth) 
    
    dayofWeek = calcWeekDay(excelDate)
    
    abrvDayTup = abrvDay(DAYS) # create a tuple of abbreviated days
    
    
    # Print year and month
    print "%d  %s" %(intYear, nameofMonth)
    
    # Print abbreviated days
    for day in abrvDayTup :
            
        abrvDayString += "%s\t" %day
    
    
    print abrvDayString 
    
    
    # Stores appropriate values along with initial formatting and returns
    # the given month's calender as a formatted string
    for day in range (1,numDays + 1) :    
            
        if dayofWeek == 0 :
            
            sundayString += "%d\t" %day 
  
            if (day % 7) == 0 :
            
                sundayString += "\n"      
     
            
        if dayofWeek == 1:
            
            mondayString += "%d\t" %day 
  
            if day <= 6 and (day % 6) == 0 :
            
                    mondayString += "\n"
            else :        
                
                if (day % 7) == 6 :
                
                    mondayString += "\n"
                                            
                                 
        if dayofWeek == 2:
            
            tuesdayString += "%d\t" %day 
  
            if day <= 5 and (day % 5) == 0 :
            
                    tuesdayString += "\n"
            else :        
                
                if (day % 7) == 5 :
                
                    tuesdayString += "\n"
                                                                            
                                                                              
        if dayofWeek == 3:
            
            wednesdayString += "%d\t" %day 
  
            if day <= 4 and (day % 4) == 0 :
            
                    wednesdayString += "\n"
            else :        
                
                if (day % 7) == 4 :
                
                    wednesdayString += "\n" 
                                                         
                                    
        if dayofWeek == 4:
            
            thursdayString += "%d\t" %day
            
            if day <= 3 and (day % 3) == 0 :
            
                    thursdayString += "\n"
            else :        
                
                if (day % 7) == 3 :
                
                    thursdayString += "\n"  
                                                       
                                                      
        if dayofWeek == 5:
            
            fridayString += "%d\t" %day
            
            if day <= 2 and (day % 2) == 0 :
            
                    fridayString += "\n"
            else :        
                
                if (day % 7) == 2 :
                
                    fridayString += "\n"   
                
        if dayofWeek == 6:
            
            saturdayString += "%d\t" %day 
  
           
            if day <= 1 and (day % 1) == 0 :
            
                    saturdayString += "\n"
            else :        
                
                if (day % 7) == 1 :
                
                    saturdayString += "\n"  
                                                           
     #Return Statements                                              
    if dayofWeek == 0 :
        return sundayString
    if dayofWeek == 1 :
        return mondayString
    if dayofWeek == 2 :
        return tuesdayString
    if dayofWeek == 3 :
        return wednesdayString
    if dayofWeek == 4 :
        return thursdayString
    if dayofWeek == 5 :
        return fridayString
    if dayofWeek == 6 :
        return saturdayString

#End of Program Script
def theEnd() :
    print "\nProgrammed by Richard Constantine"
    print time.ctime()
    print "End of Processing"
    
    
#****************************************the instructions to make a calendar

YEAR = 2100 # year to make the calendar between 1900 and 9999 inclusive

for month in range(1, 13) :
    
    print(formatCalendar(YEAR, month))  
    print "\n"
   
    
theEnd()