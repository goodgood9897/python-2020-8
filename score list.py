a = int(input('全班有幾人?'))
list_score = []
for i in range(a):
    i = int(input('請輸入成績:'))
    if i not in list_score:
        list_score.append(i)

print(list_score)
sum_score = sum(list_score)
print('全班平均:',int(sum_score/a))

#最大值
highest = 0
for i in list_score:
    if i > highest:
        highest = i
print('最高分:',highest)

#最小值
lowest = 100
for i in list_score:
    if i < lowest:
        lowest = i
print('最低分:',lowest)