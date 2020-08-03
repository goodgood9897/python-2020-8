r = int(input("輸入半徑長度:"))
c = r*2*3.14
print("周長:%.2f"%c)
if (c<30):
    print("This circle is too small.")
elif (c>31 and c<60):
    print("This circle is small.")
elif (c>61 and c<90):
    print("This circle is normal one.")
elif (c>91 and c<120):
    print("This circle is big.")
else:  
    print("This circle is too big.")