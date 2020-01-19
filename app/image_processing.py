from app.ocr_process import OCR
from app.util  import compress_word_list
import numpy as np
import math
import matplotlib.pyplot as plt

class ImageProcessing:

    def __init__(self):
        super().__init__()

    @staticmethod
    def draw_line(self,point_list,kind = "horizontal",color =(0,0,0),thickness=1):
        if kind == "horizontal":
            for x in point_list:
                cv2.line(self.img,(0,x),(img.shape[0],x),color,thickness)
        elif kind == "vertical":
            for x in point_list:
                cv2.line(self.img,(x,0),(x,img.shape[1]),color,thickness)
        else :
            print("Invalid type")

    @staticmethod
    def get_lines(gray,kind = "horizontal",threshold_value=250,minimum_distance=40):
        if kind == "horizontal":
            hist = np.sum(gray,axis=1)
            hist = hist/gray.shape[1]
        else:
            hist = np.sum(gray,axis=0)
            hist = hist/gray.shape[0]
        filter_value = hist>threshold_value
        filter_list  = np.where(filter_value)[0]
        compress_list = []
        temp_list = []
        for i  in filter_list:
            if len(temp_list)==0:
                temp_list.append(i)
            elif i == temp_list[-1]+1:
                temp_list.append(i)
            else:
                compress_list.append(np.mean(temp_list))
                if len(compress_list)>2 and compress_list[-1]-compress_list[-2]<minimum_distance:
                    del compress_list[-1]
                if kind != "horizontal" and len(temp_list) < 20:
                    del compress_list[-1]
                temp_list = []
        compress_list  = list(map(math.ceil,compress_list))
        return compress_list

    @staticmethod
    def extract_text(img,point_list):
        word_list = []
        #print(len(point_list))
        if len(point_list)==0:
            return []
        i = 0
        if (len(point_list)==1):
            words = OCR.image_to_string(img[:,point_list[i]:img.shape[1],:])
            words = words.replace("\n\n"," ")
            # print(words)
            # plt.imshow(img[:,point_list[i]:img.shape[1],:])
            # plt.show()
            if len(words):
                temp_word_list = words.split(" ")
                word_list.extend(compress_word_list(temp_word_list))
        else:
            for i in range(0,len(point_list)-1):
                words = OCR.image_to_string(img[:,point_list[i]:point_list[i+1],:])
                words = words.replace("\n"," ")
                # print(words)
                # plt.imshow(img[:,point_list[i]:point_list[i+1],:])
                # plt.show()
                if len(words):
                    temp_word_list = words.split(" ")
                    word_list.extend(compress_word_list(temp_word_list))
            else:
                words = OCR.image_to_string(img[:,point_list[i+1]:img.shape[1],:])
                words = words.replace("\n"," ")
                # print(words)
                # plt.imshow(img[:,point_list[i+1]:img.shape[1],:])
                # plt.show()
                if len(words):
                    temp_word_list = words.split(" ")
                    word_list.extend(compress_word_list(temp_word_list))
        return word_list
    
    # @staticmethod
    # def get_vertical_inside_horizontal(,point_x_list):
    #     for i in range(len(point_x_list)-1):
    #         point_y_list = get_lines(self.gray_img[point_x_list[i]:point_x_list[i+1],:],kind="vertical")
    #         #if len(point_y_list) >=2:
    #         #draw_line(img[point_x_list[i]:point_x_list[i+1],:,:],point_y_list,kind="vertical")
    #         text_list = self.extract_text(img[point_x_list[i]:point_x_list[i+1],:,:],point_y_list)
    #         list_seperation_logic(text_list,len(point_y_list),alteration_list,rearrangement_list)
