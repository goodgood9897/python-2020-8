menu_list =[
		{"id": 1, "name":"1.漢堡","price":70,"$":"元"},
		{"id": 2, "name":"2.薯條", "price": 45,"$":"元"},
       	{"id": 3, "name":"3.雪碧", "price": 30,"$":"元"},
       	{"id": 4, "name":"4.薯餅", "price": 45,"$":"元"},
       	{"id": 5, "name":"5.熱狗","price":35,"$":"元"},
        {"id": 6, "name":"6.洋蔥圈", "price": 45,"$":"元"},
        {"id": 7, "name":"7.可樂", "price": 30,"$":"元"}]
Order_list = []
print('==========================歡迎光臨本餐廳,祝您用餐愉快====================================')
print('今日菜單:')
for menu in menu_list:
    print(menu.get('name'),menu.get('price'),menu.get('$'))
while True:
    print('='*50)
    print("1.點餐\n2.取消點餐\n3.確認菜單\n4.結帳")
    server = int(input("請選擇服務:"))
    if server == 1:
        while True:
            menu_add = input("請輸入菜名編號或輸入Y结束點菜:")
            if menu_add != 'Y':
                for m in menu_list:
                    if m.get('id')== int(menu_add):
                        Order_list.append(m)
                        break
            else:
                print('==================已點菜=====================')
                total_price = 0
                for order in Order_list:
                    print(order.get('name'),order.get('price'),order.get('$'))
                    total_price += int(order.get('price'))
                print('                           小計:{}元'.format(total_price))
                break
    elif server == 2:       
        menu_del = input("請輸入要取消的菜名:")
        Order_list.remove(order)
        print('==================已點菜=====================')
        total_price = 0
        for order in Order_list:
            print(order.get('name'),order.get('price'),order.get('$'))
            total_price += int(order.get('price'))
        print('                                   小計:{}元'.format(total_price))
    elif server == 3:
        print('==================已點菜=====================')
        total_price = 0
        for order in Order_list:
            print(order.get('name'),order.get('price'),order.get('$'))
            total_price += int(order.get('price'))
        print('                           小計:{}元'.format(total_price))
    elif server == 4:
        print('=================您的消費菜單=======================')
        total_price = 0
        for order in Order_list:
            print(order.get('name'),order.get('price'),order.get('$'))
            total_price += int(order.get('price'))
        print('          總計:{}元'.format(total_price))
        print('==================謝謝光臨，歡迎您再次光臨本店!=====================')
        break