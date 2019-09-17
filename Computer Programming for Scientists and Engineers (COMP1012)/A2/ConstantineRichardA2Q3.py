# RichardConstantineA2Q3
#
# COMP 1012 SECTION A01
# INSTRUCTOR Terry Andres
# ASSIGNMENT: A2 Question 3
# AUTHOR Richard Constantine
# VERSION [Date of last change: 2013-Oct-20]
#
# PURPOSE: To list which day the years 2000 - 2100 inclusive start on.


import math
import time

FULL_DAY = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday")

#Define how to Calculate the Excel Date
def calcExcelDate(year, month, day) :
    
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

    return  excelDate

#Define function to calculate weekday from Excel date
def calcWeekDay(excelDate) :
    
    OFFSET = 6 # offset excelDate to give weekday
    
    excelDate = int(excelDate) 

    weekday = (excelDate + OFFSET) % 7 

    return weekday
        
#Define function to check if year is a leap year (used to sort common and leap)
def isLeapYear(year) :

    isLeap = 0
    year = year
   
    feb28Year, feb28Month, feb28Day = year, 2, 29 #assign date values
    mar1Year, mar1Month, mar1Day = year, 3, 1
    
    feb28ExD = int(calcExcelDate(feb28Year, feb28Month, feb28Day)) #calculate
    mar1ExD = int(calcExcelDate(mar1Year, mar1Month, mar1Day))     #Excel date
    
    if mar1ExD > feb28ExD : 
        
        isLeap = 1 # leap year becomes true
    
    return isLeap

#Function that generates a list of years appropriate to starting weekday and
# isLeap values
def genYearList(start, ending, weekday, isLeap) :
    
    intExcelDate = 0       
    intExcelDateList = []
    intWeekday = 0
    intWeekdayList = []
    yearList = []
    leapYear = isLeap 
    
    sundayList = []
    mondayList = []
    tuesdayList = []
    wednesdayList = []
    thursdayList = []
    fridayList = []
    saturdayList = []
    
    year = start
    month = 1
    day = 1
    
    count = 0
    
    for year in range(start, ending + 1) : #start to end inclusive
        
        
        leapCheck = isLeapYear(year) 
        
        if leapYear == leapCheck : #check if assigning leap year values
        
            yearList.append(year)  #create year list
            
            intExcelDate = int(calcExcelDate(year, month, day))
            intExcelDateList.append(intExcelDate) 
                                                   # create subsequent Excel
            intWeekday = calcWeekDay(intExcelDate) # date and weekday list
            intWeekdayList.append(intWeekday)     
            
        
    #sort and print year with starting weekday, 
    #formated with spaces (b/c each list is different in length)
    if weekday == 0 :
    
        for day in intWeekdayList :
            
            if day == weekday :
            
                sundayList.append(yearList[count])
                
            count += 1
    
        print "Sunday     %s" %sundayList
            
    if weekday == 1 :
 
        for day in intWeekdayList :
                    
            if day == weekday :
                    
                mondayList.append(yearList[count])
                        
            count += 1
    
        print "Monday     %s" %mondayList
 
    if weekday == 2 :

        for day in intWeekdayList :
                    
            if day == weekday :
                    
                tuesdayList.append(yearList[count])
                        
            count += 1
    
        print "Tuesday    %s" %tuesdayList 
        
    if weekday == 3 :

        for day in intWeekdayList :
                    
            if day == weekday :
                    
                wednesdayList.append(yearList[count])
                        
            count += 1
    
        print "Wednesday  %s" %wednesdayList

    if weekday == 4 :

        for day in intWeekdayList :
                    
            if day == weekday :
                    
                thursdayList.append(yearList[count])
                        
            count += 1
    
        print "Thursday   %s" %thursdayList

    if weekday == 5 :

        for day in intWeekdayList :
                    
            if day == weekday :
                    
                fridayList.append(yearList[count])
                        
            count += 1
    
        print "Friday     %s" %fridayList
    
    if weekday == 6 :

        for day in intWeekdayList :
                    
            if day == weekday :
                    
                saturdayList.append(yearList[count])
                        
            count += 1
    
        print "Saturday   %s" %saturdayList
  

#End of Program Script
def theEnd() :
    print "\nProgrammed by Richard Constantine"
    print time.ctime()
    print "End of Processing"
    

###########################################################################        

start = 2000
ending = 2100
isLeap = 0 # starting declaration  
weekday = 0 #  ""       ""

print "Start Year:  %6d" %start
print "End Year:  %6d" %ending

print "Common years; Jan 1 is a ..."

for day in range (0,7) : 
   
    weekday = day
    
    isLeap = 0 # used to check that leap year is false
    
    genYearList(start, ending, weekday, isLeap)
    
    

print "\nLeap years; Jan 1 is a ..."
for day in range (0, 7) :
    
    weekday = day
    
    isLeap = 1 # used to check that leap year is true
    
    genYearList(start, ending, weekday, isLeap)
    
    
theEnd()