# 我与小明共同喜欢的菜普有 "大白菜","茄子","猪排" ,小明还喜欢 西红柿 利用切片 将我的菜谱复制给小明 并添加小明喜欢的西红柿。
my_foods= ["大白菜","茄子","猪排"]
friend_foods=my_foods[:] #利用切片复制整个列表
# friend_foods=my_foods  #利用恒等复制整个列表
friend_foods.append("西红柿")
print("******我的是食谱*****")
print(my_foods)
print("******朋友的是食谱*****")
print(friend_foods)

