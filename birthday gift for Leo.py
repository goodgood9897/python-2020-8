import turtle

birthday = 10187
birthday1 = 1010807
birthday2 = 20120807
Chinesse_name = '鄧凱中'
English_name = 'Leo'
English_name1 = 'leo'
Birthday_gift = '紙片馬力歐'
Birthday_gift1 = '紙片馬力歐:摺紙國王'
Birthday_gift2 = 'Paper Mario'
Birthday_gift3 = 'The origami king'
Birthday_gift4 = 'Paper Mario: The origami king'
Birthday_gift5 = '紙片馬力歐'

while True:
    a = int(input("What's your birthday?"))
    if a == birthday or a == birthday1 or a == birthday2:
        a = input("What's your Chinesse name?")
        if a == Chinesse_name:
            a = input("What's your English name?")
            if a == English_name or a == English_name1:
                a = input("Your birthday gift is _________.")
                if a == Birthday_gift or a == Birthday_gift1 or a == Birthday_gift2 or a == Birthday_gift3 or a == Birthday_gift4 or a == Birthday_gift5:
                    print('Happy Birthday~~~')
                    print('Here is your dictionary and gift:')
                    
                    d = {}

                    while True:
                        print('=>')
                        print('1.建立字彙')
                        print('2.列印全部資料')
                        print('3.英翻中')
                        print('4.中翻英')
                        print('5.學習測驗')
                        print('6.離開系統')
    
                        sel = input('請輸入功能選項:')
    
                        if sel == '1':
                            en = input('輸入英文單字: ')
                            ch = input('輸入中文解釋: ')
                            d[en] = ch
        
                            fo = open('mydictionary.txt','w')
                            for k,v in d.items():
                                fo.write(k)
                                fo.write(':')
                                fo.write(v)
                                fo.write('\n')
                            fo.close()
                        elif sel == '2':
                            for k,v in d.items():
                                print(k,':',v)
                        elif sel == '3':
                            search = input('搜尋英文:')
                            print(d[search])
                        elif sel == '4':
                            search1 = input('搜尋中文:')
                            for k,v in d.items():
                                if search1 == v:
                                    print(k)
                        elif sel == '5':
                            score = 0
                            for k,v in d.items():
                                print(v,':')
                                ans = input('請輸入你的答案:')
                                if ans == k:
                                    print('恭喜答對')
                                    score = score + 1
                                    print('你的分數:',score)
                                else:
                                    print('答錯了')
                        elif sel == '6':
                            print('Bye~!')
                            print('打開底下的新分頁')
                            break
                    j = turtle.Turtle()
                    j.color('blue')
                    j.shape('turtle')

                    d = turtle.Turtle()
                    d.color('yellow')
                    d.shape('turtle')

                    f = turtle.Turtle()
                    f.color('red')
                    f.shape('turtle')

                    for i in range(360):
                        j.forward(1)
                        j.left(1)

                    for i in range(4):
                        d.forward(100)
                        d.left(90)

                    for i in range(3):
                        f.left(120)
                        f.forward(100)

                    turtle.done()
                    break
                else:
                    print('Enter errow, you are not Leo')
                    print('Please enter again.')
            else:
                print('Enter errow, you are not Leo')
                print('Please enter again.')
        else:
             print('Enter errow, you are not Leo')
             print('Please enter again.')
    else:
        print('Enter errow, you are not Leo')
        print('Please enter again.')