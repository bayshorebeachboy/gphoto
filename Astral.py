from astral import *
import datetime
from datetime import date

#setup location
location = Location(info = ('Tidewater', 'Oregon', 44.5, -123.9, 'America/Los_Angeles', 100))
location.timezone = 'America/Los_Angeles'
#parse month, day, year and time from now
now = datetime.datetime.now()
ntime = now.strftime('%H:%M:%S')
year = int(now.strftime('%Y'))
month = int(now.strftime('%m'))
day = int(now.strftime('%d'))
print('It is %d/%d/%d' % (month, day, year))
sun = location.sun(local=True, date=date(year, month, day))
# parse time from sunrise, sunset
sunrise = sun['sunrise']
srtime = sunrise.strftime('%H:%M:%S')
sunset = sun['sunset']
sstime = sunset.strftime('%H:%M:%S')
#daylength = sunset - sunrise
now = datetime.datetime.now()
thedate = now.strftime('%D')
#print thedate
ntime = now.strftime('%H:%M:%S')
print ('Time Now is:\t\t%s' % (ntime))
print ('Sunrise Time is:\t%s' % (srtime))
print ('Sunset Time is:\t\t%s' % (sstime))
if ntime > srtime and ntime < sstime:
    print("So It's Day")
else: print("So It's Night")