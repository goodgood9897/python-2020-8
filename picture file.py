file = open('imagine.png','rb')
img = file.read()

file.close()

copy = open('copy.png','wb')
copy.write(img)
copy.close()
