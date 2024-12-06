from datetime import datetime
import sys
import calendar 
import xlsxwriter
import locale

def generate_excel(transport, name, number, fromAddress, toAddress, distance):
    today = datetime.today()
    locale.setlocale(locale.LC_ALL, 'en_EN')

    workbook = xlsxwriter.Workbook(f'{today.strftime("%B").title()} {today.year} - Kilometer Form.xlsx')
    bold = workbook.add_format({'bold': True})
    underline_and_italic = workbook.add_format({'underline': True, 'italic': True})
    money_format = workbook.add_format({'num_format': '€ 0.00'})
    worksheet = workbook.add_worksheet()

    worksheet.set_column('A:B', 10)
    worksheet.set_column('B:C', 10)
    worksheet.set_column('C:D', 10)
    worksheet.set_column('D:E', 10)

    # Standard info
    worksheet.write('B1', 'Name', bold)
    worksheet.write('C1', name)
    
    worksheet.write('D1', 'Employee Number', bold)
    worksheet.write('F1', number)
    
    worksheet.write('B3', 'FROM-TO')
    worksheet.write('C3', f'{fromAddress} - {toAddress}')

    worksheet.write('B4', 'TO-FROM')
    worksheet.write('C4', f'{toAddress} - {fromAddress}')
    
    worksheet.write('B6', 'Number of kilometers according to Google Maps shortest route:')
    worksheet.write('G6', f'{distance} to and {distance} back')
    
    # Headers
    worksheet.write('B9', 'Day', underline_and_italic)
    worksheet.write('C9', 'Date', underline_and_italic)
    worksheet.write('D9', 'Transport', underline_and_italic)
    worksheet.write('E9', 'Kilometers', underline_and_italic)

    row = 8 
    weekends = 0
    final_row = 8

    weekend = ['Saturday', 'Sunday']

    month = calendar.monthrange(today.year, today.month)

    for i in range(1, month[1] + 1):
        current_day = datetime.today().replace(day=i)
        current_weekday = current_day.strftime('%A').title()

        if current_weekday in weekend:
            weekends += 1
            continue

        worksheet.write_string(row + i - (int)(weekends / 2.0), 1, current_weekday)
        worksheet.write_string(row + i - (int)(weekends / 2.0), 2, current_day.strftime('%d-%m-%Y'))
        worksheet.write_string(row + i - (int)(weekends / 2.0), 3, transport)
        worksheet.write_number(row + i - (int)(weekends / 2.0), 4, float(distance) * 2)

        final_row = row + i - (int)(weekends / 2.0)

    worksheet.write_string(final_row + 2, 2, 'Total (km): ')
    worksheet.write_formula(final_row + 2, 4, f'=SUM(E{row + 1}:E{final_row + 1})')
    
    worksheet.write_formula(final_row + 2, 6, f'=(E{final_row + 3} * 0.23)', money_format)

    workbook.close()

if __name__ == '__main__':
    transport, name, number, fromAddress, toAddress, distance = [line.strip() for line in open('info.txt')]
    generate_excel(transport, name, number, fromAddress, toAddress, distance)
