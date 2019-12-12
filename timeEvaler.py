import xlrd


data = xlrd.open_workbook('данные.xlsx').sheets()[0]
for i in range(11):
    path = 'time' + str(i + 1) + '.txt'
    out = open(path, 'w')
    maxA = 0
    t = data.col_values(2 * i, 1)
    print(data.col_values(2 * i + 1, 1))
    a = []
    for j in data.col_values(2 * i + 1, 1):
        if j == '':
            break
        a.append(j)



    upper = True
    counter = 0
    for k in range(len(a)):
        maxA = max(maxA, a[k])
        if upper and a[k] <= 0:
            upper = False
            counter += 1
            out.write(str(counter) + '\t' + str(t[k]) + '\n')
        elif (not upper) and a[k] > 0:
            upper = True
            maxA = 0

    out.close()

