str=input("请输入：")
x= eval(str)

if 0!=x :
    a0 = x/x
a = x*x
b = x*x*x
c = x*x*x*x
d = x*x*x*x*x
if 0==x :
    print("1",str,"0","0","0","0")
elif '.' in str:
    print("{:f}".format(a0),str,"{:f}".format(a),"{:f}".format(b),"{:f}".format(c),"{:f}".format(d))
else :
    print("{:.0f}".format(a0),str,"{:.0f}".format(a),"{:.0f}".format(b),"{:.0f}".format(c),"{:.0f}".format(d))
 
