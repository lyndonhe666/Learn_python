import os

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


pwd = os.getcwd()
for (dir_path, dir_names, file_names) in os.walk(pwd+'/prac_re'):
    for file_name in file_names:
        fpath = os.path.join(dir_path, file_name)
        with open(fpath) as f:
            data = f.read().splitlines()
            new_data = '\n'.join([modify_line(line, 3) if 'https://www.bilibili.com/video/av74106411' in line else line for line in data])
        with open(fpath,'w') as f:    
            f.write(new_data)