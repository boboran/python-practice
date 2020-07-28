
####### Q1
# pw_str = input('支付宝支付密码：')
# pw_num = int(pw_str)
# while True:
#     if pw_num >= 0 and pw_num <= 999999 and len(pw_str) == 6:
#         print('支付数字合法')
#     else:
#         print('支付数字不合法，请重新输入')
#     pw_str = input('支付宝支付密码：')
#     pw_num = int(pw_str)



#######  Q2

# import random
# p1 = 'SanDisk 闪迪u盘128g'
# p2 = '苹果鼠标 Magic Mouse2'
# p3 = '罗技MK235无线键盘鼠标套装'
# p4 = '小米米家扫地机器人'
# random_product = random.choice((p1,p2,p3,p4))
# sales = int(input("竞猜商品为：" + str(random_product) + '，请输入您的竞猜价格：'))
# i = 1
# while i <= 20:
#
#     # print("p=",random_product,"sales=",sales)
#     if random_product == p1:
#         if sales < 149:
#             print('价格低了，请继续竞猜：',end = str())
#         elif sales > 149:
#             print('价格高了，请继续竞猜：',end = str())
#         else:
#             print('恭喜你，你猜对了该商品的价格，你是大赢家！')
#             break
#
#     if random_product == p2:
#         if sales < 550:
#             print('价格低了，请继续竞猜：',end = str())
#         elif  sales > 550:
#             print('价格高了，请继续竞猜：',end = str())
#         else:
#             print('恭喜你，你猜对了该商品的价格，你是大赢家！')
#             break
#     if random_product == p3:
#         if sales < 120:
#             print('价格低了，请继续竞猜：',end = str())
#         elif sales > 120:
#             print('价格高了，请继续竞猜：',end = str())
#         else:
#             print('恭喜你，你猜对了该商品的价格，你是大赢家！')
#             break
#     if random_product == p4:
#         if sales < 1400:
#             print('价格低了，请继续竞猜：',end = str())
#         elif sales > 1400:
#             print('价格高了，请继续竞猜：',end = str())
#         else:
#             print('恭喜你，你猜对了该商品的价格，你是大赢家！')
#             break
#     i +=1
#     sales = int(input())
# if i > 20:
#     print("竞猜失败，下次再战！")
#
#
#
#
#
#
