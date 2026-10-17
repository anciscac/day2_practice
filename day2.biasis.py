#1.整数 int
age = 25
print("年龄:",age)
print("年龄类型：",type(age))

 #2.浮点数 float
price = 19.99
print("价格:",price)
print("价格类型：",type(price))

#3.字符串 str
name = "AI学习"
print("名称：",name)
print("名称类型：",type(name))

#4.布尔值 bool
is_student = True
print("是否是学生：",is_student)
print("布尔类型：",type(is_student))

#5.类型转换 
str_age = str(age)
print("转换后的年龄:",str_age,"类型：",type(str_age))
int_price = int(price)
print("转换后的价格：",int_price,"类型：",type(int_price))

#1.定义列表
scores = [85,92,78,92,88]
print("成绩列表：",scores)

#2.索引
print("第一个成绩:",scores[0])
print("最后一个成绩:",scores[-1])
print("中间几个成绩:",scores[1:3])

#3.修改数据
scores[0] = 95
print("修改后的成绩列表:",scores)

#4.删除和添加成绩
scores.append(100)   #在末尾添加
print("添加后的列表:",scores)
scores.pop()      #删除末尾元素
print("删除后的列表:",scores)

#5.列表的常用统计
print("总人数:",len(scores))
print("最高分:",max(scores))
print("最低分:",min(scores))
print("平均分:",sum(scores) / len(scores))

#1.定义字典
user = {"name": "张三","age": 25,"city":"青岛"}
print("用户信息:",user)

#2.取值
print("用户名:",user["name"])
print("用户年龄:",user.get("age"))

#3.修改和新增
user["age"] = 26
user["hobby"] = "写代码"
print("修改后的字典:",user)

#4.遍历字典
print("---开始遍历---")
for key,value in user.items():
    print(f"键: {key},值:{value}")

print("\n--- 1、条件判断 ---")
scores = 85

if scores >= 90:
    print("成绩优秀!")
elif scores >= 60:
    print("成绩及格。")
else:
    print("成绩不及格，需要补考")

# 结合逻辑运算符
temperature = 95
pressure = 1.2
if temperature > 90 and pressure > 1.0:
    print("报警：温度和压力双高！")

print("\n--- 2、循环 ---")
#1.for 循环
scores = [85,92,55,78,90]
total=0
for s in scores:
    total = total + s
print(f"全班总成绩为:{total}")

#2.range()函数
for i in range(3):
    print(f"这是第{i+1}次学习")

#3. while 循环
count = 3
while count >= 0:
    print(f"倒计时：{count}")
    count = count - 1
print("倒计时结束！")

print("\n---3、函数封装---")
# 定义函数
def check_score(score):
    if score >= 60:
        return "及格"
    else:
        return "不及格"
#调用函数
result1 = check_score(85)
result2 = check_score(55)
print(f"85分是:{result1}")  
print(f"55分是:{result2}")

#定义更复杂的函数
def calculate_average(score_list):
    if len(score_list) == 0:
        return 0
    return sum(score_list) / len(score_list)
my_scores = [85,90,95]
avg = calculate_average(my_scores)
print(f"我的平均分是：{avg}")

