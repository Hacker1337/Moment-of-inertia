import xlrd


data = xlrd.open_workbook('данные.xlsx').sheets()[0]


path = 'decr.txt'
out = open(path, 'w')
maxA = 0
t = data.col_values(0, 1)
a = []
for j in data.col_values(1, 1):
    if j == '':
        break
    a.append(j)



upper = True
counter = 0
goodt = []
size = 3
for k in range(len(a)):
    maxA = max(maxA, a[k])
    if upper and a[k] <= 0:
        upper = False
        counter += 1
        goodt.append(t[k])
        if len(goodt) > size:
            out.write(str(maxA) + '\t' + str((float(goodt[-1]) - float(goodt[-size]))/(size-1)) + '\n')

    elif (not upper) and a[k] > 0:
        upper = True
        maxA = 0

out.close()

