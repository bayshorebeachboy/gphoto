#!/usr/bin/env python

# python-gphoto2 - Python interface to libgphoto2
# http://github.com/jim-easterbrook/python-gphoto2
# Copyright (C) 2015-17  Jim Easterbrook  jim@jim-easterbrook.me.uk
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function
import datetime
import logging
import os
import subprocess
import sys
import gphoto2 as gp
#import datetime    
#from datetime import datetime
from astral import *
#import datetime
from datetime import date
#import ephem  
#o=ephem.Observer()  
#o.lat='45'  
#o.long='-124'  
#s=ephem.Sun()  
#s.compute()  

def copy_files():
    subprocess.call(["mv", "/Users/Neal/Documents/gphoto/IMG_0001.JPG", "/Users/Neal/Documents/gphoto/webcam.jpg"])
    #subprocess.call(["sshpass", "-p", "murphy", "scp", "/Users/Neal/Documents/gphoto/webcam.jpg",  "pi@192.168.1.12:/home/pi"])
    #print('Copied /Users/Neal/Documents/gphoto/webcam.jpg  pi@192.168.1.12:/home/pi')

def delete_files():
    #print('Enter delete_files')
    folder = '/store_00010001/DCIM/100CANON'
    camera = gp.Camera()
    # camera.init()
    # gp.gp_camera_folder_delete_all(camera, folder)
    test = gp.check_result(gp.gp_camera_folder_delete_all(camera, folder))
    #print(test)
    #text = "Deleteing Camera Files..."
    #print(text)

def main():    
    #sunrise = ephem.localtime(o.next_rising(s))
    #sunset = ephem.localtime(o.next_setting(s))
    #now = datetime.now()
    ##print('Next Sunrise ',sunrise)
    ##print('Next Sunset ', sunset)
    ##print(now)
    ##if now > sunset and now < sunrise:    
    ## if sunset < sunrise:
    #print('Day')  
    #####################################
    #setup location
    location = Location(info = ('Tidewater', 'Oregon', 44.5, -123.9, 'America/Los_Angeles', 100))
    location.timezone = 'America/Los_Angeles'
    #parse month, day, year and time from now
    now = datetime.datetime.now()
    ntime = now.strftime('%H:%M:%S')
    year = int(now.strftime('%Y'))
    month = int(now.strftime('%m'))
    day = int(now.strftime('%d'))
    #print('It is %d/%d/%d' % (month, day, year))
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
        print("Therefore ItIs Day")
    #else: print("Therefore It Is Night")    
        #####################################
        logging.basicConfig(
           format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
        gp.check_result(gp.use_python_logging())
        delete_files()
        #print('Entering delete_files')
        #folder = '/store_00010001/DCIM/100CANON'
        #camera = gp.Camera()
        ## camera.init() 
        ## gp.gp_camera_folder_delete_all(camera, folder)
        #test = gp.check_result(gp.gp_camera_folder_delete_all(camera, folder))
        #print(test)
        #text = "Deleteing Camera Files..."
        #print(text)    
        camera = gp.check_result(gp.gp_camera_new())
        gp.check_result(gp.gp_camera_init(camera))
        print('Capturing image')
        file_path = gp.check_result(gp.gp_camera_capture(
           camera, gp.GP_CAPTURE_IMAGE))
        print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
        target = os.path.join('/Users/Neal/Documents/gphoto', file_path.name)
        print('Copying image to', target)
        camera_file = gp.check_result(gp.gp_camera_file_get(
           camera, file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL))
        #gp.check_result(gp.gp_file_save(camera_file, 'webcam.jpg'))
        gp.check_result(gp.gp_file_save(camera_file, target))
        #subprocess.call(['open', target])
        gp.check_result(gp.gp_camera_exit(camera))
        copy_files()
        return 0
    else: print("Therefore It Is Night")
if __name__ == "__main__":
    sys.exit(main())
