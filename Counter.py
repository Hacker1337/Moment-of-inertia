out = open('time11.txt', 'w')

t, a = (float(i) for i in input().split())
upper = True
counter = 0
while(t != -1):
    if (upper and a <= 0):
        upper = False
        counter+=1
        out.write(str(counter)+str(t)+'\t'+'\n')

    elif (not upper) and a > 0:
        upper = True
    t, a = (float(i) for i in input().split())

out.close()

