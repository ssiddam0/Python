
# program - lab7-99_sowjanya.py  30 April 2019

'''
This program read the excel file '' into a numpy two-dimensional array. It also
generate 2 one-dimensional lists of row and column headers and prints the data.

'''
import numpy as np    # Needed to create numpy arrays
import pandas as pd   # Needed to read excel file into dataframe
import xlrd           # Needed to work on excel files


def main():
    
    colheader_list = create_colheader_list()
    rowheader_list = create_rowheader_list()
    revenue_array = generate_numpy_array()
    
        
    for i in range(len(rowheader_list)):
        print(rowheader_list[i],end='\t')  # prints column headers
    print('\n')    
    for i in range(15):
        print(colheader_list[i+1],end='\t') # prints row headers
        for j in range(6):
            
            print(revenue_array[i][j],end='\t') # prints data in 2d numpy array
        print('\n')
    
    
def create_colheader_list():
    
    # Extracting Column headers into one dimensional list
    colheader_list = []
    rowheader_list = []
    wb = xlrd.open_workbook('lab7-99_excelFile.xlsx') 
    sheet = wb.sheet_by_index(0) 
    sheet.cell_value(0, 0) 
      
    for i in range(sheet.nrows): 
        #print(sheet.cell_value(i, 0))
        colheader_list.append(sheet.cell_value(i, 0))
        
    return colheader_list

def create_rowheader_list():
    
    # Extracting row headers into one dimensional list
    rowheader_list = []
    wb = xlrd.open_workbook('lab7-99_excelFile.xlsx') 
    sheet = wb.sheet_by_index(0) 
    sheet.cell_value(0, 0) 
      
    for i in range(sheet.ncols):
        rowheader_list.append(sheet.cell_value(0,i))
    
    return rowheader_list
    
def generate_numpy_array():
       
    #Skip the first column since it contains the row headers
    cols = [1,2,3,4,5,6]
    
    #skiprows = 1, skip the first row since it contains column headers
    data_frame = pd.read_excel('lab7-99_excelFile.xlsx',skiprows = 1, usecols = cols, header=None)
    
    # Converts dataframe to numpy two-dimensional array
    revenue_array = data_frame.to_numpy()
    
    return revenue_array
   
    
main()

input('\n press any key to continue')