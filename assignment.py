import numpy as np
import cv2
import glob
class bacterialcrop:
    #this method is used to read the image
    def readimage(self,img):
        #read image as grayscale image
        img=cv2.imread(img)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        return img

    #apply binary thresholding to the image
    def threshold_img(Self,img):
        _,thresh=cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
        return thresh

   #find all the contours of the thresholded image
    def find_contours(self,thresh):
        _,contours,_=cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        return contours

if __name__ == "__main__":
    bc=bacterialcrop()
      
    count=0
    for im in glob.glob('Input/*.JPG'):
        count+=1
        img=bc.readimage(im)
        org_img=cv2.imread(im)
        thresh=bc.threshold_img(img)
        contours=bc.find_contours(thresh)

        for contour in contours:
            #draw a bounding rectangle around the contours
            x,y,w,h=cv2.boundingRect(contour)
            
            if w>200 and h>200:
                crop=org_img[y:y+h,x:x+w]
                cv2.imwrite('crop_img'+str(count)+'.png',crop)
