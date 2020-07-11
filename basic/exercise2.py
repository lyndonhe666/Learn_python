# salary
valid_lines = [x for x in data.splitlines() if ";" in x ]
for line in valid_lines:
    name = line.split(";")[0].split(':')[1].strip()
    salary = line.split(";")[1].split(':')[1].strip()
    tax = int(int(salary)*0.1)
    income = int(int(salary)*0.9)
    print(f'name:{name:>8}; salary:{salary:>8}; tax:{tax:>8}; income:{income:>8}')


# 99乘法表
for upper in range(1,10):
    for lower in range(1,upper+1):
        print(f'{lower:<}*{upper:<}={lower*upper}',end=' ')
    print('\n')


# 文件大小统计
lines=[x for x in log.splitlines() if '.' in x]
log_dict = {}
for line in lines:
    file_type = line.split('\t')[0].split('.')[1]
    file_size = int(line.split('\t')[1])
    if file_type not in log_dict.keys():
        log_dict[file_type] = file_size
    else:
        log_dict[file_type] += file_size