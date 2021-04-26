import xlrd
import pandas as pd
import numpy as np
def read_excel():
    workbook = xlrd.open_workbook('retail.xls')
    # print(workbook.sheet_names())
    sheet = workbook.sheet_by_name(workbook.sheet_names()[1])
    tmp = []
    # print(sheet.cell(98,3).ctype)
    for i in range(72,110):
        t = []
        for j in range(2,14):
            if sheet.cell(i,j).ctype != 1:
                t.append(sheet.cell(i,j).value)
            else:
                t.append(0)
        tmp.append(np.array(t))
    column = [str(i) for i in range(1,13)]
    index = []
    for i in range(72,110):
        index.append(sheet.cell(i,1).value)
    # print(len(tmp))
    data = pd.DataFrame(tmp,columns = column,index = index)
    data = data
    data['avg'] = data.apply(lambda x: x.mean(), axis=1)
    data['std'] = data.apply(lambda x: x.std(), axis=1)
    data['var'] = data.apply(lambda x: x.var(), axis=1)
    data.to_csv('2020_retailer.csv')


    return data

# if __name__ == "__main__":
#     read_excel()
