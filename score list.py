a = int(input('全班有幾人?'))
list_score = []
for i in range(a):
    score = int(input('請輸入成績:'))
    if score not in list_score:
        list_score.append(score)

print(list_score)
sum_score = sum(list_score)
print('全班平均:',int(sum_score/a))