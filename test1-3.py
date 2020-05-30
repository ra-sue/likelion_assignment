break_check = False

for first in range(2, 101):
    for second in range(2, first+1):
        if (first != second) and (first % second == 0):
            break_check = True
            break
    if break_check == True:
        break_check = False
        continue
    else:
        print(first)



for i in range(2, 101):
    check = True
    for j in range(2, i):
        if i % j == 0:
            check = False
            break
    if check:
        print(i, end=", ")
        # print(i)
