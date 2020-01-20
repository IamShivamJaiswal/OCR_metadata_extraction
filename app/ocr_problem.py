from app.prepocess import PreProcess   
from app.image_processing import ImageProcessing
from app.util import *
from tqdm import tqdm

class OCRProblem():

    def __init__(self,conf,args):
        super().__init__()
        self.conf = conf
        self.args = args

    def run(self):
        preprocess = PreProcess()
        preprocess.read(self.args.input_image)

        if self.args.problem == "list":

            point_x_list = ImageProcessing.get_lines(preprocess.get_gray_img())
            #print(len(point_x_list))
            alteration_list,rearrangement_list = [],[]
            for i in tqdm(range(len(point_x_list)-1)):
                point_y_list = ImageProcessing.get_lines(preprocess.get_gray_img()[point_x_list[i]:point_x_list[i+1],:],kind="vertical")
                #if len(point_y_list) >=2:
                #draw_line(preprocess.get_img()[point_x_list[i]:point_x_list[i+1],:,:],point_y_list,kind="vertical")
                text_list = ImageProcessing.extract_text(preprocess.get_img()[point_x_list[i]:point_x_list[i+1],:,:],point_y_list)
                list_seperation_logic(text_list,len(point_y_list),alteration_list,rearrangement_list,self.conf)
            get_csv_report(alteration_list,rearrangement_list,self.args.output_file)
        elif self.args.problem.upper() == "REPORT DATE":
            ImageProcessing.get_report_date(preprocess.get_img())
