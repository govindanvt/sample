import xlsxwriter
workbk = xlsxwriter.Workbook('d:\\text.xlsx')
wrksht = workbk.add_worksheet()
wrksht.write('A1','text data')
workbk.close()