import datetime
# from datetime import datetime
import ephem  
o=ephem.Observer()  
o.lat='45'  
o.long='-124'  
s=ephem.Sun()  
s.compute()



sunrise = ephem.localtime(o.next_rising(s))
sunset = ephem.localtime(o.next_setting(s))
now = datetime.datetime.now()
print('Next Sunrise ',sunrise)
print('Next Sunset ', sunset)
print(now)
if now > sunset and now < sunrise:
    print('Day') 
else:
    print('Night')

