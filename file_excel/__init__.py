import openpyxl

f = openpyxl.load_workbook('excel_file.xlsx')
my_sheet1 = f['sheet1']
# print(my_sheet1['B1'].value) #xem dữ liệu ở ô/cell thứ B1
for i in range(1,6): #nghiên cứu nên lặp tới n = ?
    print(my_sheet1['B'+str(i)].value)

#ghi dữ liệu vào file excel
my_sheet1['E10'].value = 'LOP HOC PYTHON'
f.save('excel_file.xlsx')
f.close()

#The new code
#follow new requirement at 10:42 am 02.07.2022
#nhan new code 11:34h

#Hieu chen doan code
