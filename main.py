import xlrd

loc = ("absolutely_essential_words_504.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

print("---* welcome wordmaster *---")
print()

for i in range(1, 5):
    meaning = sheet.cell_value(i,1)
    print('{}'.format(i))
    print('meaning> '+meaning)
    word = ""
    while word != sheet.cell_value(i, 0):
        word = input("word> ")

