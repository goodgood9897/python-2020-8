import os.path

d = {}

def buildMenu():
    print('=>')
    print('1. 建立辭彙')
    print('2. 列出所有單字')
    print('3. 英翻中')
    print('4. 中翻英')
    print('5. 測驗學習成果')
    print('6. 離開系統')

print('############################')
print('#歡迎進入阿茂的英文高手系統#')
print('############################')
print('*** 使用本系統，你將成為英文高手!!! ***')

if not os.path.isfile('mydictionary.txt'):
    fo = open('mydictionary.txt', 'w')
    print('new file')
else:
    fo = open('mydictionary.txt', 'r')
    print('old file')

for row in fo.readlines():
    data = row.split(':')
    
    key = data[0]
    value = data[1]
    value = value.strip()
    
    d[key]=value
print(d)    

fo.close()


while True:
    buildMenu()
    
    sel = input('請輸入欲執行選項: ')

    if sel=='1':
        while True:
            voc = input('輸入新單字(按0停止輸入): ')
            if voc == '0':
                break
            if voc not in d:
                m = input('輸入中文解釋: ')
                d[voc] = m
            else:
                print('單字已經存在')

        print(d)
        #if not os.path.isfile('mydictionary.txt'):
        fo = open('mydictionary.txt', 'w')
        #        else:
        #            fo = open('mydictionary.txt', 'a')
        for k,v in d.items():
            fo.write(k)
            fo.write(':')
            fo.write(v)
            fo.write('\n')
        fo.close()
    elif sel=='2':
        if not os.path.isfile('mydictionary.txt'):
            print('目前字典是空的!!!')
        else:
            fo = open('mydictionary.txt', 'r')
            foc = fo.read()

            print(foc)
            #for row in fo.readlines():
            #    data = row.split(':')
                    
            
        
        
    elif sel=='3': # 英翻中
        voc = input('輸入要查詢的英文單字: ')
        if voc in d: 
            print(d[voc])
        else:
            print('我的字典沒有這個單字')
    elif sel=='4': # 中翻英
        got=False
        ch = input('輸入要查詢的中文: ')
        for k,v in d.items():
            if ch==v:
                print(ch,'的英文是',k)
                got=True
        if not got:
            print('抱歉，查不到!')                                      
    elif sel=='5': # 測驗
        score=0
        print('The total score is', len(d), 'points')
        for k, v in d.items():
            print(v, ':')
            ans = input()
            if ans == k:
                score += 1
                print('correct! you got', score, 'points now')
            else:
                print('wrong! you got', score, 'points now')
    elif sel=='6':
        break
    else:
        print('輸入錯誤，請重新輸入!')

