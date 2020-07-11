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