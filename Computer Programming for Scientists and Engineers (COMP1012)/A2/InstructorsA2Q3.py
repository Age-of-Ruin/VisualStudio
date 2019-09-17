# InstructorsA2Q3
#
# COMP 1012  SECTION [Section number]
# INSTRUCTOR [Instructor name]
# ASSIGNMENT: A2 Question 3
# AUTHOR    The Instructors
# VERSION   2013-Oct-10
#
# PURPOSE: To find out which years use which calendars

from time import ctime
import math

DAYS = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", 
       "Saturday")
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", 
         "Oct", "Nov", "Dec")

def calcExcelDate(year, month, day) :
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

def calcWeekDay(excelDate) :
    """Find the day of the week (0 to 6) for a given Excel Date"""
    return int(excelDate + 6) % 7

def genYearList(start, ending, weekDay, isLeap) :
    """Return a list of years from start to ending-1 that start on weekDay
    and are/are not leap years according to isLeap."""
    yearList = [ ]
    for year in range(start, ending) :
        jan1Day = calcWeekDay(calcExcelDate(year,1,1))
        yearIsLeap = calcExcelDate(year, 2, 29) < calcExcelDate(year, 3, 1)
        yearList += (jan1Day == weekDay and yearIsLeap == isLeap) * [year]
    return yearList

START_YEAR = 2000
END_YEAR   = 2100

YEAR = 2014

print("START YEAR:  %d" % START_YEAR) 
print("END YEAR:    %d" % END_YEAR) 

print("Common years; Jan 1 is a ...")

for day in range(7) :
    years = genYearList(START_YEAR, END_YEAR + 1, day, False)
    print "  %-10s" % DAYS[day], years
          
print("Leap years; Jan 1 is a ...")

for day in range(7) :
    years = genYearList(START_YEAR, END_YEAR + 1, day, True)
    print "  %-10s" % DAYS[day], years

print ( "\nProgrammed by The Instructors" )
print ( "Date: " + ctime() )
print ( "** End of processing **" )
