a=1
b=2.0
c="3"
d=complex(1,2)
# 浮点型转换int
# print(int(b))
# print(type(int(b)))
# 字符串转int
# print(int(c))
# print(type(int(c)))
# 复数不能转换成int
# print(int(d))
# print(type(int(d)))
# int转浮点类型
# print(float(a))
# print(type(float(a)))
# print(float(c))
# print(type(float(c)))
# 复数转浮点型--复数不能转换成float
# print(float(d))
# print(type(float(d)))
# int转换字符串
# print(str(a))
# print(type(str(a)))
# float转字符串
# print(str(b))
# print(type(str(b)))
# complex转换字符串
# print(str(d))
# print(type(str(d)))
# int转换复数
# print(complex(a))
# print(type(complex(a)))
# float转复数
# print(complex(b))
# print(type(complex(b)))
# print(complex(c))
# print(type(complex(c)))
# 只有数字类型的字符串才能够成功的转换成int,同理转换float,complex也是一样的
c="1+2j"
print(type(complex(c)))