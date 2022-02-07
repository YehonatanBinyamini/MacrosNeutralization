from openpyxl import load_workbook
import sys

#the Excel file mast be in the same folder for get the path


path ='./' + sys.argv[1]

wb = load_workbook(filename=path, read_only=False, keep_vba=False)

