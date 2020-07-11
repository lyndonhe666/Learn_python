# 文件读写 补充练习1修改
# 如果有链接，修改
#    如果有修改，拼接3部分
def modify_line(line, number):
    start_index = line.find('av74106411')+len('av74106411')
    # 找到数字起始位置
    while line[start_index].isdigit()==False:
        start_index+=1
    # 找数字结束位置
    end_index=start_index
    while line[end_index].isdigit():
        end_index+=1
    new_number=str(int(line[start_index:end_index])+number)
    return line[:start_index] + new_number + line[end_index:]
# 对每一行处理
with open('prac_filerw.txt','r',encoding='utf-8') as f:
    log = f.read()
lines=log.splitlines()
number = int(input('请输入：'))
new_log=''.join([modify_line(line, number) if 'https' in line else line for line in lines])

# 字典课后练习1
with open('0016_1.txt','r') as f:
    content=f.read()
records = content.splitlines()
names=[]
credits=[]
for record in records:
    elements=record.split(' ')
    name, credit, age = [x for x in elements if len(x)>0]
    names.append(name)
    credits.append(credit)
dict1=dict(zip(names,credits))
dict2 = {}
for key, value in dict1.items():
    if key[0] in dict2:
        dict2[key[0]]+=int(value)
    else:
        dict2[key[0]]=int(value)


# 课后练习2
members = {
    1 :{'name':'白月黑羽', 'level':3, 'coins':300},
    2 :{'name':'短笛魔王', 'level':5, 'coins':330},
    3 :{'name':'紫气一元', 'level':6, 'coins':340},
    4 :{'name':'拜月主',   'level':3, 'coins':32200},
    5 :{'name':'诸法空',   'level':4, 'coins':330},
    6 :{'name':'暗光城主', 'level':3, 'coins':320},
    7 :{'name':'心魔尊',   'level':3, 'coins':2300},
    8 :{'name':'日月童子', 'level':8, 'coins':3450},
    9 :{'name':'不死尸王', 'level':3, 'coins':324},
    10:{'name':'天池剑尊', 'level':9, 'coins':13100},
}
def check_account():
    account_name = input("请输入账号名: ")
    print(f'用户ID:{[uid for uid in members.keys() if members[uid]["name"]==account_name][0]}')
    print(f'用户等级:{[members[uid]["level"] for uid in members.keys() if members[uid]["name"]==account_name][0]}')
    print(f'用户金币:{[members[uid]["coins"] for uid in members.keys() if members[uid]["name"]==account_name][0]}')
    print("用户查询完成")

def add_user():
    user_name = input("请输入用户名: ")             
    # check
    user_names = [members[uid]['name'] for uid in members.keys()]
    if user_name in user_names:
        print('用户已存在，请重新输入: ')
        add_user()
    else:
        user_level = input("请输入等级: ")
        user_coins = input("请输入金币: ")  
        largest_id = max(members.keys())
        members[largest_id+1]={
            'name':user_name,
            'level':user_level,
            'coins':user_coins
        }
        print('添加用户完成')
def del_user():
    user_name = input("请输入用户名: ")             
    # check
    user_names = [members[uid]['name'] for uid in members.keys()]
    if user_name not in user_names:
        print('用户不存在，请重新输入: ')
        del_user()
    else:
        uid=[uid for uid in members.keys() if members[uid]["name"]==user_name][0]
        del members[uid]
        print('删除用户完成')

def options():
    print("""
    操作选项：
   1 查看用户账号信息
   2 添加用户
   3 删除用户
   4 列出所有用户信息
   0 退出
   """)
    option = input('请选择操作选项: ')
    while option!='0':
        if option=='1':
            check_account()
        elif option == '2':
            add_user()
        elif option == '3':
            del_user()
        elif option == '4':
            print(members)
        option = input('请选择操作选项: ')
options()


# 补充练习1
with open('2019-10-22_11.05.40.log','r') as f:
    log = f.read()
lines = log.splitlines()
res = {}
for line in lines:
    print(line)
    t, API, user = line.split('|')
    if API in res:
        res[API] += 1
    else:
        res[API] = 0

# 补充练习2
with open('stock.txt','r') as f:
    data=f.read()
records = data.splitlines()
names = [record.split('|')[0].strip() for record in records]
codes = [record.split('|')[1].strip() for record in records]
stock_dict=dict(zip(names,codes))
def stock_query():
    a = input("请输入要查询的代码或名称: ")
    # 不全是数字
    if sum([letter.isdigit() for letter in a])!=len(a):
        print(f'股票名称:{stock_dict[a]}')
        print(f'股票代码:{a}')   
    else:
        print(f'股票代码:{a}')
        print(f'股票名称:{[key for key in stock_dict.keys() if stock_dict[key]==a][0]}')
stock_query()

# 补充练习3 github上的题
with open('0005_1.txt', 'r') as f:
    data = f.read()
data = data.splitlines()
# structure:
# {user_id: 
#    [{lessionid:xxx,checktime:xxx},
#     {lessionid:xxx,checktime:xxx}]
sign_dict = {}
for line in data:
    t=(line.strip("\t(),").split(',')[0]).strip("'")
    lessonid=(line.strip("\t(),").split(',')[1]).strip("'")
    userid=(line.strip("\t(),").split(',')[2]).strip("'")
    if userid in sign_dict:
        sign_dict[userid].append({'lessonid':lessonid,'checkintime':t})
    else:
        sign_dict[userid]=[]

# 练习4
with open('/Users/lyndon/Documents/白月黑羽python/data/prac_dict3/teacher.txt','r') as f:
    teacher=f.read().splitlines()
with open('/Users/lyndon/Documents/白月黑羽python/data/prac_dict3/teacher_course.txt','r') as f:
    teacher_course=f.read().splitlines()
with open('/Users/lyndon/Documents/白月黑羽python/data/prac_dict3/course.txt','r') as f:
    course=f.read().splitlines()
teacher_dict = dict(zip([line.split(';')[0] for line in teacher],[line.split(';')[-1] for line in teacher]))
course_dict=dict(zip([line.split(';')[0] for line in course],[line.split(';')[1] for line in course]))
for line in teacher_course[1:]:
    print(f'{teacher_dict[line.split(";")[0]]:<8}'+':'+f'{(course_dict[line.split(";")[1]])}')