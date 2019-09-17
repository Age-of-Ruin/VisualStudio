# RichardConstantineA2Q3
#
# COMP 1012 SECTION A01
# INSTRUCTOR Terry Andres
# ASSIGNMENT: A2 Question 3
# AUTHOR Richard Constantine
# VERSION [Date of last change: 2013-Oct-1]
#
# PURPOSE: To list which day the years 2000 - 2100 inclusive start on.


import math
import time

FULL_DAY = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

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


def calcWeekday(excelDate) :
    
    excelDate = int(excelDate) 

    weekday = (excelDate + 6) % 7

    return weekday
        





def isLeapYear(year) :

    isLeap = 0
    year = year
   
    feb28Year, feb28Month, feb28Day = year, 2, 29
    mar1Year, mar1Month, mar1Day = year, 3, 1
    
    feb28ExD = int(calcExcelDate(feb28Year, feb28Month, feb28Day)) 
    mar1ExD = int(calcExcelDate(mar1Year, mar1Month, mar1Day))
    
    if mar1ExD > feb28ExD :
        
        isLeap = 1 # leap year becomes false
    
    return isLeap

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
    
    for year in range(start, ending + 1) :
        
        
        leapCheck = isLeapYear(year)   
        
        if leapYear == leapCheck :
        
            yearList.append(year)    
            
            intExcelDate = int(calcExcelDate(year, month, day))
            intExcelDateList.append(intExcelDate)
        
            intWeekday = calcWeekday(intExcelDate)
            intWeekdayList.append(intWeekday)
        
           
    if weekday == 0 :
    
        for day in intWeekdayList :
            
            if day == weekday :
            
                sundayList.append(yearList[count])
                
            count += 1
    
        print "Sunday  %s" %sundayList
            
    if weekday == 1 :
 
        for day in intWeekdayList :
                    
            if day == weekday :
                    
                mondayList.append(yearList[count])
                        
            count += 1
    
        print "Monday  %s" %mondayList
 
    if weekday == 2 :

        for day in intWeekdayList :
                    
            if day == weekday :
                    
                tuesdayList.append(yearList[count])
                        
            count += 1
    
        print "Tuesday  %s" %tuesdayList 
        
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
    
        print "Thursday  %s" %thursdayList

    if weekday == 5 :

        for day in intWeekdayList :
                    
            if day == weekday :
                    
                fridayList.append(yearList[count])
                        
            count += 1
    
        print "Friday  %s" %fridayList
    
    if weekday == 6 :

        for day in intWeekdayList :
                    
            if day == weekday :
                    
                saturdayList.append(yearList[count])
                        
            count += 1
    
        print "Saturday  %s" %saturdayList
  

#End of Program Script
def theEnd() :
    print "\nProgrammed by Richard Constantine"
    print time.ctime()
    print "End of Processing"
    

        
start = 1901
ending = 2000
isLeap = 0   
weekday = 0

print "Start Year:  %6d" %start
print "End Year:  %6d" %ending

print "Common years; Jan 1 is a ..."

for day in range (0,7) : 
   
    weekday = day
    
    isLeap = 0
    
    genYearList(start, ending, weekday, isLeap)
    
    

print "\nLeap years; Jan 1 is a ..."
for day in range (0, 7) :
    
    weekday = day
    
    isLeap = 1
    
    genYearList(start, ending, weekday, isLeap)
    
    
    
    
    
theEnd()