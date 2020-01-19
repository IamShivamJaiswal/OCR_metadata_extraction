import argparse
from app.prepocess import PreProcess
from app.config import Config
from app.ocr_problem import OCRProblem

parser = argparse.ArgumentParser(prog="")#prog='PDFCrop'

parser.add_argument('--input_image', help='Specify input image path.')
parser.add_argument("--problem", help="'list' for genes assayed and genes tested.\n'Report Date' for Report Date.")

parser.add_argument('--output_file', default="output.csv",help='Specify output .csv file path')

args = parser.parse_args()


def main():
    conf = Config()
    ocr_problem = OCRProblem(conf,args)
    ocr_problem.run()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)