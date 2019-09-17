# InstructorsA2Q2
#
# COMP 1012  SECTION Axx
# INSTRUCTOR [Name of your instructor]
# ASSIGNMENT: A2 Question 2
# AUTHOR    The Instructors
# VERSION   2013-Oct-10
#
# PURPOSE: To calculate a date representation as Excel does.

from time import ctime
import math

DATES = ( "1900-03-01", "2013-1-1", "2013-February-28", "2013-Oct-17", 
         "9999-12-31", "10000-Dec-32")

DAYS = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", 
       "Saturday")
FULL_MONTHS = ("January", "February", "March", "April", "May", "June", "July", 
          "August", "September", "October", "November", "December")
          
MONTHS = ( FULL_MONTHS + tuple( [month[:3] for month in FULL_MONTHS] ) 
          + tuple(["%d" % (nn+1) for nn in range(len(FULL_MONTHS))])
          + tuple(["%02d" % (nn + 1) for nn in range(len(FULL_MONTHS))]) )
          
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

# Script starts here

for date in DATES :
    print "\nDate: %s" % date
    year, month, day = date.split("-")
    year, day = int(year), int(day)
    month = MONTHS.index(month) % len(FULL_MONTHS) + 1
    print("\nyear:  %d" % year) 
    print("month: %d" % month) 
    print("day:   %d" % day)
    
    # checks
    goodDate = True
    if ( year < 1900 or year > 9999 ) :
        print("The year %d is invalid; not from 1900 to 9999" % year) 
        goodDate = False 
    
    if ( month < 1 or month > 12 ) :
        print("The month %d is invalid; not from 1 to 12" % month) 
        goodDate = False 
    
    if ( day < 1 or day > 31 ) :
        print("The day %d is invalid; not in range from 1 to 31" % day) 
        goodDate = False 
    
    if ( goodDate ) :
        # calculate serial representation
        excelDate = calcExcelDate(year, month, day)
    
        # output results
        OFFSET = 6 + (year == 1900 and month <= 2)
        print("\nThe Excel date for %s, %d-%s-%d is %d." %     
            (DAYS[calcWeekDay(excelDate)],          
            year, MONTHS[month-1][:3], day, excelDate) ) 
        print 75 * '.'


print ( "\nProgrammed by The Instructors" )
print ( "Date: " + ctime() )
print ( "** End of processing **" )
