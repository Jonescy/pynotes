
a = "print('asadasd')"
eval(a)

a = 10
b = 20
c = eval("a+b")
print(c)

dict1 = dict(a=100, b=200)
d = eval("a+b", dict1)
print(d)
