def my_seek_line(f, line):
    data = f.readlines()
    x = 0
    for i in range(0, line - 1):
        x += len(data[i])
    f.seek(x)

f = open(file='my_text_file.txt', encoding='UTF-8', mode='r')
# x = f.read()
# print(x)
#
# y = f.read(10)
# print(y)
#
# f.seek(0) #seek con trỏ/cursor về vị trí thứ n với n là tham số bên trong seek
# z = f.read()
# print(z)
# f.write("Tôi là NVVP")
# f.seek(2)
# l1 = f.readline() #trả về dòng kể từ vị trí con trỏ
# print(l1)

# l2 = f.readline()
# print(l2)
# ls1 = f.readlines(20)  # trả về dòng kể từ vị trí con trỏ
# print(ls1)
f.close()



