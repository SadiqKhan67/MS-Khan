
def main():
    import cv2, glob #cv2 library for image process, glob library for finding the path and name of file available in folder/route 

    images=glob.glob("*.jpg") #list the image files of jpg file extension.

    for image in images:
    
        img=cv2.imread(image,0) #read each image in loop, 1 is for color, 0 for gray
        re=cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/4))) #resize to 25% of actual size, index 0 for row, index 1 for column
        cv2.imwrite("resized_"+image,re) #save resized image in same folder/route

    
if __name__ == __main__:
    main()
