#
#
#
# # timelist = [89,98,00,75,68,37,58,90]
# # print("原列表：",timelist)
# # for i in range(len(timelist)):
# #     timelist[i] = timelist[i] + 1900
# #     if timelist[i] == 1900:
# #         timelist[i] = 2000
# # timelist.sort()
# # print('参考输出序列：',timelist)
#
# thisweek = [4235,10111,8447,9566,9788,8951,9808]
# print('本周运动步数列表：',thisweek)
# lastweek = [4235,5612,8447,11250,9211,9985,3783]
# print('上周运动步数列表：',lastweek)
# sumweek = []
# for i in range(len(thisweek)):
#      sumweek.append(thisweek[i] + lastweek[i])
# print('上周和本周运动步数汇总：',sumweek)
# sumweek.sort()
# print('升序：',sumweek)
# sumweek.sort(reverse=True)
# print('降序：',sumweek)
# weekday = ['周日','周一','周二','周三','周四','周五','周六']
#
# # #### 1 get max and min from this week
# # max_thisweek = max(thisweek)
# # min_thisweek = min(thisweek)
# # # print(min_thisweek)
# # # print(max_thisweek)
# # #### 2 get the index of max and min in thisweek
# # for index,ma in enumerate(thisweek):
# #     if ma == max_thisweek:
# #         maxindex = index
# #     if ma == min_thisweek:
# #         minindex = index
# # # print(maxindex,minindex)
# # #### 3 insert min and max into weekday
# # if maxindex > minindex:
# #     weekday.insert(maxindex+1,max_thisweek)
# #     weekday.insert(minindex+1,min_thisweek)
# # else:
# #     weekday.insert(minindex + 1, min_thisweek)
# #     weekday.insert(maxindex + 1, max_thisweek)
# # print(weekday)
#
# #### compare the item to 8000
# meetlist = []
# for index,steps in enumerate(lastweek):
#     if steps > 8000:
#         meetlist.append(index)
# for index in meetlist:
#     print(weekday[index],lastweek[index])
# meetlistnow = []
# for index,steps in enumerate(thisweek):
#     if steps > 8000:
#         meetlistnow.append(index)
# for index in meetlistnow:
#     print(weekday[index],thisweek[index])
# total = sum(thisweek)+sum(lastweek)
# print('上周和本周运动总步数：',total)


########### 商品入库
item_num = []
item_name = []
for i in range(5):
    num_item = input('请输入商品编号和商品名称进行商品入库，每次只能输入一件商品：')
    stock_in = num_item.split()
    item_num.append(stock_in[0])
    item_name.append(stock_in[1])
print("商品清单：")
for index in range(len(item_name)):
    print(item_num[index],item_name[index])
cart = []
num = input('请输入要购买的商品的商品编号：')
while True:
    num = input('商品已添加到购物车，请继续添加要购买商品的商品编号：')
    if num == 'q':
        break
    else:
        index = item_num.index(num)
        name = item_name[index]
print("您购物车里已经选择的商品为：")
