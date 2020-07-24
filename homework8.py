pw_str = input('支付宝支付密码：')
pw_num = int(pw_str)
while True:
    print("num=",pw_num,"str=", pw_str)
    if pw_num >= 0 and pw_num <= 999999 and len(pw_str) == 6:
        print('支付数字合法')
    else:
        print('支付数字不合法，请重新输入')
    pw_str = input('支付宝支付密码：')
