pw = int(input('支付宝支付密码：'))
if pw >= 0 and pw <= 999999:
    print('支付数字合法')
else:
    print('支付数字不合法，请重新输入')
