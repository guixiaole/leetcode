import xlrd
from xlutils.copy import copy

excel1 = xlrd.open_workbook('1.xlsx')
wb = copy(excel1)
ws = wb.get_sheet(0)
# ws.write(0,0,'guile')
# wb.save('guile.xlsx')
# print(table1.col_values(0))
excel2 = xlrd.open_workbook('2.xlsx')
table2 = excel2.sheets()[0]
table1 = excel1.sheets()[0]
for i in range(3, table1.nrows):
    # print(table1.row_values(i)[3])
    if table1.row_values(i)[3] == '':
        names = table1.row_values(i)[2]
        # print(names)
        for j in range(1, table2.nrows):
            names2 = table2.row_values(j)[2]
            if names == names2:
                sid = table2.row_values(j)[3]
                ws.write(i, 3, sid)
                break
                # print(sid)
for i in range(3, table1.nrows):
    if table1.row_values(i)[7] == '':

        teacher_name1 = table1.row_values(i)[6]
        # print(teacher_name1)
        for j in range(1, table2.nrows):
            teacher_names2 = table2.row_values(j)[8]
            # print('teach=',teacher_names2)
            if teacher_name1 == teacher_names2:
                teacher_phone = table2.row_values(j)[9]
                # print(teacher_name1)
                print(teacher_phone)
                ws.write(i, 7, teacher_phone)
                break
for i in range(3, table1.nrows):
    if table1.row_values(i)[6] == '':

        names = table1.row_values(i)[2]
        # print(teacher_name1)
        for j in range(1, table2.nrows):
            names2 = table2.row_values(j)[2]
            # print('teach=',teacher_names2)
            if names == names2:
                teacher_phone = table2.row_values(j)[9]
                teacher_names2 = table2.row_values(j)[8]
                # print(teacher_name1)
                print(teacher_phone)
                ws.write(i, 7, teacher_phone)
                ws.write(i, 6, teacher_names2)
                break
        # print(table1.row_values(i)[6])
        # print('names2=',names2)
    # print(table1.row_values(i)[3])
wb.save('guile.xlsx')
