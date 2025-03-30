# This replaces the time.localtime() function 
# by returning the actual value of the local 
# time and date (here Belgium), with support 
# for 'summer' and 'winter' time changes.

import sys

_path = sys.path
sys.path = ()

try:
    from time import *
finally:
    sys.path = _path
    del _path

def localtime(secs: int | None = None) -> tuple[int, int, int, int, int, int, int, int]:
    """
    Returns Belgium local time.

    See Wikipedia -> https://en.wikipedia.org/wiki/Time_in_Belgium
    In Belgium, summer and winter time are regulated in this way:
    from: the last Sunday in March (02:00 CET)
    to:   the last Sunday in October (03:00 CEST)
    """
    def last_sunday(year: int, month: int, hour: int, minute: int) -> int:
        # Get the UTC time of the last day of the month
        seconds = mktime((year, month + 1, 0, hour, minute, 0, None, None))

        # Calculate the offset to the last sunday of the month
        (year, month, mday, hour, minute, second, weekday, yearday) = gmtime(seconds)
        offset = (weekday + 1) % 7

        # Return the time of the last sunday of the month
        return mktime((year, month, mday - offset, hour, minute, second, None, None))

    utc = gmtime(secs)

    # Find start date for daylight saving, last Sunday in March (01:00 UTC)
    start_secs = last_sunday(year=utc[0], month=3, hour=1, minute=0)

    # Find stop date for daylight saving, last Sunday in October (01:00 UTC)
    stop_secs = last_sunday(year=utc[0], month=10, hour=1, minute=0)

    utc_secs = mktime(utc)
    
    # 1 hour in seconds is 60 seconds * 60 minutes = 3600 seconds
    if utc_secs >= start_secs and utc_secs < stop_secs:
        delta_secs = 2 * 3600  # Belgium summer time (CEST or UTC + 2h)
    else:
        delta_secs = 1 * 3600  # Belgium normal time (CET or UTC + 1h)

    return gmtime(utc_secs + delta_secs)