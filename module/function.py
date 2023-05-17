import os
import xlwings as xw


def get_sheet(now,sheetname):
    if not os.path.isfile( ".\\output\\" + now + "\\result.xlsx" ):
        app=xw.App(visible=False,add_book=False)
        wb=app.books.add()
        wb.save( ".\\output\\" + now + "\\result.xlsx" )
        wb.close()
        #结束进程

    app=xw.App(visible=True,add_book=False)
    wb=app.books.open(".\\output\\" + now + "\\result.xlsx")
    #查看工作表是否建立
    if sheetname not in [s.name for s in wb.sheets]:
        wb.sheets.add(name=sheetname)

    sheet = wb.sheets[sheetname]
    
    init_sheet(sheet )

    return sheet 

def init_sheet(sheet):
    sheet.range('A1').value = "場館名稱"
    sheet.range('B1').value = "測試狀態"
    sheet.range('C1').value = "測試語系"
    sheet.range('D1').value = "測試語系"
    sheet.range('E1').value = "測試語系"

