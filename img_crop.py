import cv2
import glob
import os
from PIL import Image

def crop_imgs(imgs, modified_path, x, y):
    from PIL import Image


    for i, img_path in enumerate(imgs):
        img = Image.open(img_path)
	# BEWARE THIS IS HARDCODED, PLEASE ADJUST ACCORDING TO YOUR NEEDS
        file_name = img.filename.split('/')[-1].split('/')[0][12:].split('.')[0]
        img = cv2.imread(img_path)
        cropped = img[1:x, :]
	# THE FOLLOWING LINE CAN BE UNCOMMENTED TO RESIZE and INSPECT IMAGE AS WELL.
        #newimg = cv2.resize(img, (1920, 1080))
        #cv2.namedWindow("cropped", cv2.WINDOW_NORMAL)
        #cv2.resizeWindow("cropped", 800, 600)
        #cv2.imshow("cropped", cropped)
        #cv2.waitKey(0)
        cv2.imwrite(modified_path+file_name + ".png", cropped)
        print("Wrote image: {0}".format(i))

input_dir=r"add_your_path_here/"
TEST_IMAGE_PATHS = glob.glob(os.path.join(input_dir, "*.png*"))
output_path = r"Add_your_output_path_here/"
x = 785 # Adjust according to your needs
y = 1920 # Adjust according to your needs
crop_imgs(TEST_IMAGE_PATHS, output_path, x, y)

