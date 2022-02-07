from openpyxl import load_workbook
import sys

# the Excel file must be in the same folder of this python file


path = './' + sys.argv[1]

wb = load_workbook(filename=path, read_only=False, keep_vba=False)
