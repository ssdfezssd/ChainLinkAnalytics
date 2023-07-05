import streamlit as st
import pandas as pd
import openpyxl





# Reformat Excel spreadsheet for SAFEWAY
#====================================================================================================================
def format_SAFEWAY_DistroGrid(workbook):

    st.write("YAY YOU CALLED ME safeway dg CODE")


    # Select the Reset Dates sheet
    ws = workbook['SAFEWAY_dg']

    # Insert a new column "Chain_Name" at the beginning and fill it with "WALMART"
    ws.insert_cols(1)
    ws.cell(row=1, column=1, value="STORE_NAME")
    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=1):
        for cell in row:
            cell.value = "SAFEWAY"

    # Delete columns 3(C)
    ws.delete_cols(3)

    # Delete columns 3(C)
    ws.delete_cols(3)

    # Delete columns 3(C)
    ws.delete_cols(3)

        # Iterate over the rows starting from row 2 and remove all values 
    for row in ws.iter_rows(min_row=2, min_col=4, max_col=4):
        for cell in row:
            cell.value = None

       # Iterate over the rows starting from row 2 and remove all values 
    for row in ws.iter_rows(min_row=2, min_col=7, max_col=7):
        for cell in row:
            cell.value = None

       # Iterate over the rows starting from row 2 and remove all values 
    for row in ws.iter_rows(min_row=2, min_col=6, max_col=6):
        for cell in row:
            cell.value = None

       # Iterate over the rows starting from row 2 and remove all values 
    for row in ws.iter_rows(min_row=2, min_col=9, max_col=9):
        for cell in row:
            cell.value = None


    # Remove the filter from the sheet
    ws.auto_filter.ref = None

    ## Change ADDED and MAINTAIN to 1 IN Column H
    for cell in ws['H']:
        if cell.value is not None:
            cell.value = str(cell.value).replace('ADDED', '1').replace('MAINTAIN', '1')



    # Rename Columns as required to meet objective for uploading to Snowflake
    ws.cell(row=1, column=1, value='STORE_Name')
    ws.cell(row=1, column=2, value='STORE_Number')
    ws.cell(row=1, column=3, value='UPC')
    ws.cell(row=1, column=4, value='SKU')
    ws.cell(row=1, column=5, value='PRODUCT_NAME')
    ws.cell(row=1, column=6, value='MANUFACTURER')
    ws.cell(row=1, column=7, value='SEGMENT')
    ws.cell(row=1, column=8, value='YES_NO')
    ws.cell(row=1, column=9, value='ACTIVATION_STATUS')
    ws.cell(row=1, column=10, value='COUNTY')
    ws.cell(row=1, column=11, value='CHAIN_NAME')


    return workbook