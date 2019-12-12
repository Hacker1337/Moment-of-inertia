import xlrd


data = xlrd.open_workbook('данные.xlsx').sheets()[0]


path = 'decr.txt'
out = open(path, 'w')
maxA = 0
minA = 10
t = data.col_values(0, 1)
a = []
for j in data.col_values(1, 1):
    if j == '':
        break
    a.append(j)



upper = True
counter = 0
goodt = []
size = 5
for k in range(1, len(a)):
    maxA = max(maxA, a[k])
    minA = min(minA, a[k])
    if upper and a[k] <= 0:
        upper = False
        counter += 1
        inter = t[k-1] + (t[k]-t[k-1])*a[k]/(a[k-1] - a[k])
        goodt.append(inter)
        if len(goodt) > size:
            out.write(str((maxA-minA)/2) + '\t' + str((float(goodt[-1]) - float(goodt[-size]))/(size-1)) + '\n')
        maxA = 0
        minA = 10

    elif (not upper) and a[k] > 0:
        upper = True


out.close()

