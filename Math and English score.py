Math = int(input("What's your"+'"Math" score?'))
English = int(input("What's your"+'"English" score?'))
if Math>90 and English>90:
    print("有獎品")
elif Math==100 or English==100:
    print("有獎品")
elif Math>90 or English>90:
    print("再加油")
else:
    print("要處罰")