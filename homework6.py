timelist = [89,98,00,75,68,37,58,90]
print("原列表：",timelist)
for i in range(len(timelist)):
    timelist[i] = timelist[i] + 1900
    if timelist[i] == 1900:
        timelist[i] = 2000
timelist.sort()
print('参考输出序列：',timelist)