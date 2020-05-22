# clear captured gphoto image
import os
import subprocess
import os, os.path
import glob
import shutil
import logging
import sys
import gphoto2 as gp
import re
import datetime
from datetime import datetime
import ephem  
o=ephem.Observer()  
o.lat='45'  
o.long='-124'  
s=ephem.Sun()  
s.compute()  


path_to_images = '/Users/Neal/Documents/gphoto2_testing/captured_image'
path_for_movie = '/Users/Neal/Documents/gphoto2_testing/ForMovie'
####################
#fix base_file
####################
base_file = '/Users/Neal/Documents/gphoto2_testing/ForMovie/IMG_'

import smtplib

# Use sms gateway provided by mobile carrier:
# at&t:     number@mms.att.net
# t-mobile: number@tmomail.net
# verizon:  number@vtext.com
# sprint:   number@page.nextel.com

# Establish a secure session with gmail's outgoing SMTP server using your gmail account
server = smtplib.SMTP( "smtp.gmail.com", 587 )

server.starttls()

server.login( 'nealm040@gmail.com', 'DuneGirl$4' )



camera_list = []
for name, addr in gp.check_result(gp.gp_camera_autodetect()):
    camera_list.append((name, addr))
if not camera_list:
    #print('No camera detected')
    theMsg = 'No camera detected'
    #print('The message is :', theMsg)
    #server.sendmail( 'gphoto2', '5418706584@mms.att.net', 'A620 Camera is not connected')    



camera_list.sort(key=lambda x: x[0])
# ask user to choose one
for index, (name, addr) in enumerate(camera_list):
    print('{:d}:  {:s}  {:s}'.format(index, addr, name))
    if name == 'Canon PowerShot A620 (PTP mode)':
        print(addr)
        #set_camera(addr)  

camera = gp.Camera()
port_info_list = gp.PortInfoList()
port_info_list.load()
idx = port_info_list.lookup_path(addr)
print('idx='+str(idx))
#idx = 2
camera.set_port_info(port_info_list[idx])
gp.check_result(gp.gp_camera_init(camera))

#def capture_image():
    #logging.basicConfig(format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
    #gp.check_result(gp.use_python_logging())
    #camera = gp.check_result(gp.gp_camera_new())
    #gp.check_result(gp.gp_camera_init(camera))
    #print('Capturing image')
    #file_path = gp.check_result(gp.gp_camera_capture(camera, gp.GP_CAPTURE_IMAGE))
    #print('File Path: ', file_path)
    #print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
    #target = os.path.join(path_to_images, file_path.name)
    #print('Copying image to', target)
    #camera_file = gp.check_result(gp.gp_camera_file_get(camera, file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL))
    ##gp.check_result(gp.gp_file_save(camera_file, 'webcam.jpg'))
    #gp.check_result(gp.gp_file_save(camera_file, target))
    ##subprocess.call(['open', target])
    ##print('Delete File From Camera')
    ##gp.check_result(gp.gp_camera_file_delete(camera, folder, name))
    #gp.check_result(gp.gp_camera_exit(camera))
    #return 0

def delete_files():
    os.chdir(path_to_images)
    #print(os.curdir)
    subprocess.call('rm -r ./*', shell=True)
    print('Existing image files deleted...')
    return 0

#def set_camera(addr):
    #camera = gp.Camera()
    #port_info_list = gp.PortInfoList()
    #port_info_list.load()
    #idx = port_info_list.lookup_path(addr)
    #print('idx='+str(idx))
    ##idx = 2
    #camera.set_port_info(port_info_list[idx])
    #gp.check_result(gp.gp_camera_init(camera))

    ##################################
    #testing only
    #print('Capturing image')
    #file_path = gp.check_result(gp.gp_camera_capture(camera, gp.GP_CAPTURE_IMAGE))
    #print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
    #target = os.path.join(path_to_images, file_path.name)
    #print('Copying image to', target)
    #camera_file = gp.check_result(gp.gp_camera_file_get(camera, file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL))
    #gp.check_result(gp.gp_file_save(camera_file, target))
    #gp.check_result(gp.gp_camera_exit(camera))
    #testing only
    ###########################


def main():
    delete_files()
    #capture_image()    
    logging.basicConfig(format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
    gp.check_result(gp.use_python_logging())
    ############################################
    #begin set camera 
    #camera = gp.check_result(gp.gp_camera_new())

    # make a list of all available cameras
    camera_list = []
    #for name, addr in gp.check_result(gp.gp_camera_autodetect()):
            #camera_list.append((name, addr))
    #if not camera_list:
            #print('No camera detected')

    #camera_list.sort(key=lambda x: x[0])
    ## ask user to choose one
    #for index, (name, addr) in enumerate(camera_list):
            #print('{:d}:  {:s}  {:s}'.format(index, addr, name))
            #if name == 'Canon PowerShot A620 (PTP mode)':
                #print(addr)
                #set_camera(addr)    

    # end set camera
    ############################################
    #gp.check_result(gp.gp_camera_init(camera))
    #Day or Night
    # test_capture()

    sunrise = ephem.localtime(o.next_rising(s))
    sunset = ephem.localtime(o.next_setting(s))
    if sunset < sunrise:
        print('Day')    

        print('Capturing image')
        file_path = gp.check_result(gp.gp_camera_capture(camera, gp.GP_CAPTURE_IMAGE))
        print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
        target = os.path.join(path_to_images, file_path.name)
        print('Copying image to', target)
        camera_file = gp.check_result(gp.gp_camera_file_get(camera, file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL))
        gp.check_result(gp.gp_file_save(camera_file, target))
        gp.check_result(gp.gp_camera_exit(camera))   
        #end capture image 

        print(glob.glob("./*.*"))
        file_to_rename = glob.glob("./*.*")
        fix_me = str(file_to_rename)
        fix_me = re.sub('[[/\]\'\"]', '', fix_me)
        fix_me = re.sub('.', '', fix_me, 1)
        #pass_me = '["mv" ' + ', "' + path_to_images + '/' + fix_me + '" , "' + path_to_images + '/' + 'webcam.jpg"]'
        #print pass_me
        #shutil.copy(target, path_for_movie)
        os.rename(fix_me, 'webcam.jpg')

        #add current file to movie source
        file_found = True
        i = 1
        while file_found: 
            ####################
            #fix base_file
            ####################
            if i > 9:
                zeros = '0'
            else: zeros = '00'
            #print(zeros)        
            #the_file = base_file + str(i) + '.jpg'
            the_file = base_file + zeros + str(i) +'.jpg'
            #used to create a bunch of files
            #open(the_file, 'a')
            #print('Looking for :', the_file)
            if os.path.isfile(the_file):
                print('Found :', the_file)
                i += 1
            else:
                print('Creating 1 File')
                file_found = False          
                #break loop and...
        #create one from current image
        #if i > 9:
            #zeros = '0'
        #else: zeros = '00'
        #print(zeros)
        scr = '/Users/Neal/Documents/gphoto2_testing/captured_image/webcam.jpg'
        dst = '/Users/Neal/Documents/gphoto2_testing/ForMovie/IMG_' + zeros + str(i) + '.jpg' 
        print('Copyied Current') 
        shutil.copy(scr, dst)

        #when there are 30 images create a movie and delete files
        path, dirs, files = os.walk("/Users/Neal/Documents/gphoto2_testing/ForMovie").next()
        file_count = len(files)
        if file_count > 29: 
            print('Making New Movie')
            #write something to process a movie hourly(ish)
            #the_file = '/Users/Neal/Documents/gphoto2_testing/TheMovie/test.mp4'
            theFile = '/Users/Neal/Dropbox/WeatherMovie/test.mp4'
            if os.path.isfile(the_file):
                os.remove(the_file)
            #os.system('ffmpeg -f image2 -r 1 -i /Users/Neal/Documents/gphoto2_testing/ForMovie/IMG_%03d.jpg -vcodec mpeg4 -y /Users/Neal/Documents/gphoto2_testing/TheMovie/test.mp')
            os.system('ffmpeg -f image2 -r 1 -s 2027x1520 -i /Users/Neal/Documents/gphoto2_testing/ForMovie/IMG_%03d.jpg -vcodec libx264 -crf 10 -pix_fmt yuv420p -y /Users/Neal/Dropbox/WeatherMovie/test.mp4')
            #write something to delete movie source
            for fl in glob.glob('/Users/Neal/Documents/gphoto2_testing/ForMovie/*.jpg'):
                os.remove(fl)
            subprocess.call(['python', '/Users/Neal/Documents/gphoto2_testing/delete-video.py'])
            subprocess.call(['python', '/Users/Neal/Documents/gphoto2_testing/upload-video.py', '--file', '/Users/Neal/Dropbox/WeatherMovie/test.mp4', '--title', 'Bayshore Weather Timelapse'])
        print('Deleting: {0}/{1}'.format(file_path.folder, file_path.name))
        gp.check_result(gp.gp_camera_file_delete(camera, file_path.folder, file_path.name))     
        #subprocess.call(pass_me)
    else: print('Night')
if __name__ == "__main__":
    sys.exit(main())