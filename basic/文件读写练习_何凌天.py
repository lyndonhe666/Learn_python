# 课后练习1
# 读取
f=open('0013_a1.txt','r')
content=f.read()
f.close()

l1=[x for x in content.splitlines() if ':' in x]
# 高于50岁的人列表
gt50=[x.split(':')[0].strip() for x in l1 if int(x.split(':')[1].strip())>50]

# 写入
with open('0013_a1.txt','a') as f:
	f.write('\n高于50岁的人有:'+', '.join(gt50))

# 课后练习2
def if_png(src):
    with open(src,'rb') as f:
        content=f.read(8)
    if content==b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a':
        print('png')
    else:
        print('jpg')


# 补充练习1
import re
def create_new_url(old_url,number_to_add):
	"""
	替换链接末尾的数字
	Args:
		old_url:原来的url
		number_to_add:需要加上的数字

	Return:
		new_url:已经加上了数字的新的url
	"""
    number_pattern = re.compile('.*?p=(\d+).*',re.S)
    old_number = re.search(number_pattern, old_url).group(1)
    new_number = str(int(old_number) + number_to_add)
    new_url = re.search(number_pattern, old_url).group().replace(old_number,new_number)
    return new_url

with open('prac_filerw.txt','r',encoding='utf-8') as f:
    log = f.read()
# 找出所有的url以及在原文本中的起止位置
pattern = re.compile('https://.*?\n',re.S)
index_pair = [match.span() for match in re.finditer(pattern, log)]
urls = re.findall(pattern, log)

number_to_add = int(input('请输入一个数字：'))

# 更新url
new_urls = [create_new_url(old_url, number_to_add) for old_url in urls]
# 找到对应位置
url_location_map = dict(zip(new_urls,index_pair))
# 修改
new_log=''
execute_urls=list(url_location_map.keys())
initial_index=0
# 从index为0处开始，拷贝url对应的起点之前的字符，然后拼接上新的url。当所有url都拼接完之后，再拼接上最后一个url后的所有字符
while len(execute_urls)!=0:
    start_index = url_location_map[execute_urls[0]][0]
    end_index = url_location_map[execute_urls[0]][1]
    new_log += log[initial_index:start_index]+execute_urls[0]
    initial_index = end_index
    execute_urls.pop(0)
new_log+=log[initial_index:]
with open('new_log.txt','w',encoding='utf-8') as f:
	f.write(new_log)

# 补充练习2
def write_file():
    file_name = input('请输入 新文件的名称：')
    assert type(file_name)==str
    with open(r'cfiles/gbk编码.txt','r', encoding='gbk') as f:
        f1 = f.read()
    with open(r'cfiles/utf8编码.txt','r', encoding='utf-8') as f:
        f2 = f.read()    
    new_content = '\n'.join([f1,f2])
    with open(r'cfiles/{}'.format(file_name),'w',encoding='utf-8') as f:
        f.write(new_content)
    print(new_content)