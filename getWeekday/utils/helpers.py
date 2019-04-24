import utils

__name__ = "GETWEEKDAY"
__version__ = "1.0.0"

from datetime import datetime

from utils import configprovider as config

__all__ = [

]


def fetchCurrentWeekday(self,*args):
    print ""


def validateIfLeapYear(self,year=None):
    print ""

    if year is not None:
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    else:
        return

def calculateDayOfYear(self,day=None,month=None):
    print ""

    if day is not None:
        month = self._getMonth(self, month)
        monthMap = self._mapLoader(self,"monthMap")
        if month.__ne__(self,"February") and month.__ne__(self,"January"):
            dayOfYear = monthMap.get(self,monthMap.get(self,list(monthMap)[list(monthMap).index(month)-1])) + day
        elif month.__eq__(self,"February"):
            dayOfYear = 31 + day
        elif month.__eq__(self,"January"):
            dayOfYear = day
        return dayOfYear

    else:
        return



def getMonth(self,*args):
    print ""

    if args in None:
        month = datetime.now().month

    else:
        month = args

    return month

def getYear(self,*args):

    print ""

    if args in None:
        year = datetime.now().year

    else:
        year = args

    return year

def mapLoader(self,*args):
    print ""
    if args.__eq__(self, "monthMap"):
        return config.DAYS_OF_YEAR_MAP
    elif args.__eq__(self, "weekDayMap"):
        return config.WEEK_DAY_ENUM
    else:
        return







