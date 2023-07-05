import streamlit as st
import pandas as pd
import openpyxl
from openpyxl.styles import Border, Side, PatternFill, Font, NamedStyle





def format_FOODMAXX_schedule(workbook):
    st.write("Woo Hoo you called FOODMAXX FUNCTION")
    ws = workbook['Food Maxx']

    # Remove filter from the worksheet
    ws.auto_filter.ref = None

    # Create a list to store merged cell ranges
    merged_cell_ranges = []

    # Collect merged cell ranges
    for merged_cell_range in ws.merged_cells.ranges:
        merged_cell_ranges.append(merged_cell_range)

    # Unmerge cells
    for merged_cell_range in merged_cell_ranges:
        ws.unmerge_cells(str(merged_cell_range))

    


    # Expand all rows in the worksheet
    for row in ws.iter_rows():
        for cell in row:
            ws.row_dimensions[cell.row].hidden = False

    # Unfreeze rows in the worksheet
    ws.freeze_panes = None

    # Determine the number of rows with data
    max_row = ws.max_row
    for row in reversed(range(1, max_row + 1)):
        if ws.cell(row=row, column=3).value:
            max_row = row
            break

    # Delete extra rows beyond the data range
    if ws.max_row > max_row:
        ws.delete_rows(max_row + 1, ws.max_row - max_row)

    # Delete Rows 1 and 2
    rows_to_delete = [1, 2]
    for row_index in sorted(rows_to_delete, reverse=True):
        ws.delete_rows(row_index)

    # delete column I "Inventory Blackout Dates"
    ws.delete_cols(9)

    # Delete Rows 1 and 2
    rows_to_delete = [2]
    for row_index in sorted(rows_to_delete, reverse=True):
        ws.delete_rows(row_index)

    # Create new column I to hold Team Lead
    ws.insert_cols(9)

    # Cut data from column C and paste it to column I
    ws.move_range("C1:C{}".format(ws.max_row), cols=6)

    # delete column I "Inventory Blackout Dates"
    ws.delete_cols(3)

    # Fill column A with "Save Mart" starting from row 2
    for row in ws.iter_rows(min_row=2, min_col=1, max_col=1):
        for cell in row:
            cell.value = "Save Mart"

    # Fill column A with "Save Mart" starting from row 2
    for row in ws.iter_rows(min_row=2, min_col=7, max_col=7):
        for cell in row:
            cell.value = "CA"

    # Create new column H to hold "County"
    ws.insert_cols(8)

    # delete column I "Inventory Blackout Dates"
    ws.delete_cols(14, 15)

    # Format column J as date "mm/dd/yyyy"
    date_format = NamedStyle(name='date_format')
    date_format.number_format = 'mm/dd/yyyy'
    column_letter = 'J'
    for cell in ws[column_letter]:
        cell.style = date_format

    # Find the last row with data in column A
    last_row = ws.max_row
    for row in reversed(range(1, last_row + 1)):
        if ws.cell(row=row, column=1).value:
            last_row = row
            break

    # Fill in empty cells in column J with '01/01/1900'
    for row in range(1, last_row + 1):
        if not ws.cell(row=row, column=10).value:
            ws.cell(row=row, column=10).value = '01/01/1900'

    # Fill in empty cells in column J with '6:00 AM'
    for row in range(2, last_row + 1):
        if not ws.cell(row=row, column=11).value:
            ws.cell(row=row, column=11).value = '6:00 AM'

    # Delete rows past the last row with data in column A
    if last_row < ws.max_row:
        ws.delete_rows(last_row + 1, ws.max_row - last_row)

    # Apply gridlines to all cells
    thin_border = Border(left=Side(style='thin'), right=Side(style='thin'), top=Side(style='thin'),
                         bottom=Side(style='thin'))
    for row in ws.iter_rows():
        for cell in row:
            cell.border = thin_border

            # Remove cell colors
            cell.fill = PatternFill(start_color="FFFFFFFF", end_color="FFFFFFFF", fill_type="solid")

    # Make the entire sheet have black-colored text with font size 11
    for row in ws.iter_rows():
        for cell in row:
            cell.font = Font(color="00000000", size=11)


# Rename Columns as required to meet objective for uploading to Snowflake
    ws.cell(row=1, column=1, value='CHAIN_NAME')
    ws.cell(row=1, column=2, value='STORE_NUMBER')
    ws.cell(row=1, column=3, value='STORE_NAME')
    ws.cell(row=1, column=4, value='PHONE')
    ws.cell(row=1, column=5, value='CITY')
    ws.cell(row=1, column=6, value='ADDRESS')
    ws.cell(row=1, column=7, value='STATE')
    ws.cell(row=1, column=8, value='COUNTY')
    ws.cell(row=1, column=9, value='TEAM_LEAD')
    ws.cell(row=1, column=10, value='RESET_DATE')
    ws.cell(row=1, column=11, value='RESET_TIME')
    ws.cell(row=1, column=12, value='STATUS')
    ws.cell(row=1, column=13, value='NOTES')

    # Return the path to the saved file
    return workbook








