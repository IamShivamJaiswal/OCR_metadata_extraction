from PIL import Image
from os.path import exists
import numpy as np
import sys
import cv2

class PreProcess:

    def __init__(self):
        super().__init__()

    def read(self,path):
        if not exists(path):
            print("Invalid path..")
            sys.exit(0)
        else:
            self.img = cv2.imread(path,-1)
            if self.img.shape[2]==4:
                self.handle_rgba()
            self.gray_img =  cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        
    def handle_rgba(self):
        rgba = Image.fromarray(self.img).convert('RGBA')
        background = Image.new('RGBA', rgba.size, (255,255,255))
        alpha_composite = Image.alpha_composite(background, rgba)
        self.img = np.array(alpha_composite,dtype=np.uint8)[:,:,:3].copy()
    
    def get_img(self):
        return self.img
    

    def get_gray_img(self):
        return self.gray_img
    

    def smoothening(self,kernel):
        return cv2.medianBlur(self.gray_img,kernel)