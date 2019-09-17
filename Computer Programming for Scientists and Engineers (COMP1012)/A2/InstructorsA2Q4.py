# InstructorsA2Q4
#
# COMP 1012  SECTION Axx
# INSTRUCTOR [Name of your instructor]
# ASSIGNMENT: A2 Question 3
# AUTHOR    The Instructors
# VERSION   2013-Oct-10
#
# PURPOSE: To print a calendar for a given year.

from time import ctime
import math

#******************************************************************calcExcelDate
def calcExcelDate(year, month, day = 1) :
    """Calculate Excel date for a given year (1900 to 9999), month (1 to 12)
    and day (1 to 31)"""
    assert 1900 <= year < 10000, "year %d is out of range 1900 to 9999" % year
    assert 1 <= month < 13, "month %d is out of range 1 to 12" % month
    assert 1 <= day < 32, "day %d is out of range 1 to 31" % day
    y2_after1900  = year - 1900
    # if an early month, treat it as part of previous year
    em_earlyMonth = (14 - month) // 12
    yearAdj    = y2_after1900 - em_earlyMonth 
    m2_monthAdj   = month + 12 * em_earlyMonth
    # count the number of leap years
    l_leapYears   = ( 1 + min(yearAdj,0) + yearAdj // 4 
                  - yearAdj // 100 + (yearAdj + 300) // 400 )
    # adjust for month
    d1_daysToMonth  = math.floor(-1.63 + (m2_monthAdj - 1) * 30.6) 
    d2_excelDate = day + yearAdj * 365 + l_leapYears + d1_daysToMonth
    return int(d2_excelDate)

#********************************************************************calcWeekDay
def calcWeekDay(excelDate) :
    """Find the day of the week (0 to 6) for a given Excel Date"""
    return int(excelDate + 6) % 7

#********************************************************************daysInMonth
def daysInMonth(YEAR, MONTH) :
    """Purpose: to calculate the number of days in a given month
    parameter: year between 1900 and 9999
    parameter: month from 1 to 12
    return number of days (e.g., 31 for month 1, 28 or 29 for month 2
        depending on the year, ...)"""

    # figure out the next month to calculate the month length
    if ( MONTH == 12 ) :
        nextMonth = 1 
        nextMonthYear = YEAR + 1  
    else :
        nextMonth = MONTH + 1 
        nextMonthYear = YEAR 
    
    excelDate = calcExcelDate(YEAR, MONTH) 
    return calcExcelDate(nextMonthYear, nextMonth) - excelDate 
  
#*****************************************************************formatCalendar
def formatCalendar(YEAR, MONTH) :
    """Purpose: to return a string for a calendar for a specific year and month
    parameter: year between 1900 and 9999
    parameter: month from 1 to 12
    return: a string containing a month's calendar"""

    excelDate = calcExcelDate(YEAR, MONTH) 
    startDay  = 1 + calcWeekDay(excelDate) # 1 to 7
    daysToShow = daysInMonth(YEAR, MONTH) + startDay - 1 
    
    calendar = "\n%d %s\n" % ( YEAR, monthName(MONTH) )
    calendar += "Sun\tMon\tTue\tWed\tThu\tFri\tSat\n" 
    date = 1 - startDay   # negative dates at beginning of 1st week

    # handle extra tabs at the beginning of the month by printing extra
    # negative numbered days -2, -1, 0, which are not shown
    for day in range(daysToShow) :
        date += 1
        if ( date > 0 ) :
            calendar += "%2d" % date 
     
        if ( day % 7 == 6 ) : 
            calendar += "\n " 
        else :
            calendar += "\t " 
    return calendar[:-2]  # remove last newline, if any

#**********************************************************************monthName
def monthName(month) :
    """return: month name (January, ...) corresponding to input 1 to 12
    parameter: month from 1 to 12"""
    MONTHS = "JANUARY",   "FEBRUARY", "MARCH",    "APRIL", \
             "MAY",       "JUNE",     "JULY",     "AUGUST",\
             "SEPTEMBER", "OCTOBER",  "NOVEMBER", "DECEMBER" 
    return MONTHS[month - 1]
 
#*************************************************************************theEnd
def theEnd() :
    """Purpose: to print a final message identifying the programmer, 
    giving the date, and saying the program has finished."""
    print ( "\nProgrammed by The Instructors" )
    print ( "Date: " + ctime() )
    print ( "** End of processing **" )


#********************************************the instructions to make a calendar

YEAR = 2013 # year to make the calendar
#YEAR = 2100

for month in range(1, 13) : 
    print ( formatCalendar(YEAR, month) ) 

theEnd( )

