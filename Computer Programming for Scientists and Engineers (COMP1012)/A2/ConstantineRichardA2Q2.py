# RichardConstantineA2Q2
#
# COMP 1012 SECTION A01
# INSTRUCTOR Terry Andres
# ASSIGNMENT: A2 Question 2
# AUTHOR Richard Constantine
# VERSION [Date of last change: 2013-Oct-20]
#
# PURPOSE: To calculate the number of days since Dec. 31, 1900 at 
# 11:59:59 (i.e. Jan. 1 is 0) till a specified date after said starting point
# (the MS Excel Date) by taking the date as either a number or string and
# converting it to the appropriate count.

import math
import time


FULL_DAY = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday")

FULL_MONTHS = ("January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December")

DATES = ( "1900-03-01", "2013-1-1", "2013-Feb-28", "2013-Oct-17", "9999-12-31",
"10000-Dec-32")            
             

#Abbreviated Months & ADDING ASSOCIATED NUMBER REPRESENTATIONS
def abbreviateMonths() :
    AbrvMonthList = []
    monthAbrv = []
    numOfMonths = []
    numMonthsplus0 =[]
    strCount = ""
    count = 0
    for month in FULL_MONTHS :
        
        count += 1
        strCount = str(count)
        plus0StrCount = "0" + strCount
        
        monthAbrv.append(month[:3])
        numOfMonths.append(strCount) # associated number representation
        numMonthsplus0.append(plus0StrCount) # account for month in '0X' format
    
    AbrvMonthList = monthAbrv + numOfMonths + numMonthsplus0

    
    return AbrvMonthList


#Define function to validate 
def validYearCheck(intYear) :
   
    intYear = intYear 
    validYear = 0

    if intYear <= 9999 and intYear >= 1900 :
    
        validYear = 1

    return validYear
    
#Define function to validate
def validDayCheck(intDay) :
    
    intDay = intDay
    validDay = 0
    
    if intDay <= 31 and intDay > 0 :
        
        validDay = 1

    return validDay


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

    return excelDate

#Define function to calculate weekday from Excel date
def calcWeekDay(excelDate) :
    
    OFFSET = 6 # offset excelDate to give weekday
    
    excelDate = int(excelDate) 

    weekday = (excelDate + OFFSET) % 7

    return weekday

#End of Program Function
def theEnd() :
    print "\nProgrammed by Richard Constantine"
    print time.ctime()
    print "End of Processing"
    
#############################################################################

dateTup = DATES

for date in range(0, len(dateTup)) :

    #Input date
    dateString = dateTup[date]
    dateParts = dateString.split("-")
    
    #Date Formatting (YYYY/MM(MMM)/DD)
        
    #Assign Year
    yearString = dateParts[0]
    intYear = int(yearString)
            
    validYear = validYearCheck(intYear)
        
    #Assign Month 
    monthList = abbreviateMonths()
    monthString = dateParts[1]
    
    monthIndex =  monthList.index(monthString)
    intMonth = (monthIndex % 12) + 1    # find/index month input in a
                                        # abbreviated month list(+1 to correct
                                        # position in list)                              
    #Assign Day
    dayPart = dateParts[2]
    intDay = int(dayPart)
            
    validDay = validDayCheck(intDay)
        
    #rint/Format Date Output
    print "Date: %s" % dateString
    print "\n\nYear: %d" %intYear        
    print "Month: %d" %intMonth                        
    print "Day: %d" %intDay         
            
    #Calculate Excel Date
    
    if validDay == 1 and validYear == 1 :
            
        excelDate = calcExcelDate(intYear, intMonth, intDay)
        print "The Excel date for %s is %d." %(dateString, excelDate)
            
    if validYear == 0 :
                
        print "The year %d is invalid; not from 1900 to 9999." %intYear
    
    if validDay == 0 :
                
            print "The day %d is invalid; not from 1 to 31." %intDay
                    
            
    print "**************************************************************"
                
    
theEnd()