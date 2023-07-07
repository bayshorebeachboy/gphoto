import gphoto2 as gp
import os

camera = gp.Camera()
camera.init()
file_path = gp.check_result(gp.gp_camera_capture(
    camera, gp.GP_CAPTURE_IMAGE))
print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
# target = os.path.join('/Users/Neal/Documents/gphoto2_testing', file_path.name)
# print('File Path Name', file_path.name)
camera_file = gp.check_result(gp.gp_camera_file_get(
        camera, file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL))
gp.check_result(gp.gp_file_save(camera_file, '/Users/Neal/Documents/gphoto2_testing/webcam.jpg'))
print('Copied image to /Users/Neal/Documents/gphoto2_testing/webcam.jpg')
gp.check_result(gp.gp_camera_exit(camera))