str = input("请输入钱数：")
if "RMB" in str:
    a = eval(str[3:])/6.78
    print("USD{:.2f}".format(a))
elif "USD" in str:
    a = eval(str[3:])*6.78  
    print("RMB{:.2f}".format(a))
