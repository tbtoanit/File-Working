f = open(file = 'bt.txt', encoding='utf-8', mode='r')
final_list = []
data = f.read()
# print(data)
data1 = data.split('---')
# print(data1)
for i in range(0, len(data1)):
    object_lop_hoc = data1[i]
    ds = object_lop_hoc.split('\n')
    #remove những phần tử '' trong ds
    ds.remove('')
    if i != 0:
        ds.remove('')
    #Cắt ra dữ liệu từ ds
    x = ds[0].split(':')[1]
    y = ds[1].split(':')[1]
    z = ds[2].split(':')[1]
    t = (x,y,z) #chuyển đổi dữ liệu thành tuple
    final_list.append(t) #add dữ liệu vào trong final_list

print(final_list)

# hoa comment
