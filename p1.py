from openpyxl import load_workbook
import sys

path ='./' + sys.argv[1]

wb = load_workbook(filename=path, read_only=False, keep_vba=False)

