a = int(input('How many people in the whole class?'))
list_score = []
name = []
nameandscore = []
for i in range(a):
    name_input = (input('Please enter your name:'))
    score = int(input('Please enter your score:'))
    list_score.append(score)
    name.append(name_input)

nameandscore.append(list_score)
nameandscore.append(name)
print(nameandscore)
sum_score = sum(list_score)
print('whole class average:',int(sum_score/a))

highest = 0
for n in range(a):
    if list_score[n] > highest:
        highest = list_score[n]
        highest_name = name[n]
print(highest_name,'the highest score:',highest)

lowest = 100
for n in range(a):
    if list_score[n] < lowest:
        lowest = list_score[n]
        lowest_name = name[n]
print(lowest_name,'the lowest score:',lowest)
