from selenium import webdriver
import time
wd = webdriver.Chrome('/Users/lyndon/Documents/Github/chromedriver')
wd.implicitly_wait(10)
wd.get('http://www.51job.com')
pos_input = wd.find_element_by_id('work_position_input')
pos_input.click()
# # 等到layer弹出之后再操作
# layer = wd.find_element_by_id('work_position_layer')
# while layer.get_attribute('style').split('display: ')[-1].strip(';')!='block':
#     time.sleep(0.05)
#     layer = wd.find_element_by_id('work_position_layer')
#     print(layer.get_attribute('style').split('display: ')[-1].strip(';'))
time.sleep(2)
# 定位到已经选择的地区并点击删除
selected_poss = wd.find_elements_by_css_selector('span[id*="work_position_click_multiple_selected_each"]')
for ele in selected_poss:
    ele.click()
cities = wd.find_elements_by_css_selector('em[id*="work_position_click_center_right"]')
hangzhou = [city for city in cities if city.text=='杭州'][0]
hangzhou.click()
wd.find_element_by_id('work_position_click_bottom_save').click()
wd.find_element_by_css_selector('#kwdselectid').send_keys('python')
wd.find_element_by_css_selector('div[class*=fltr] button[onclick*="kwdGoSearch"]').click()

wd.find_element_by_css_selector('em[class="dicon Dm"]').click()
time.sleep(2)
comp_types = wd.find_elements_by_css_selector('div[id="filter_cotype"] ul li')
[comp_type for comp_type in comp_types if comp_type.text=='外资(欧美)'][0].click()
# ---断点1
years = wd.find_elements_by_css_selector('div[id="filter_workyear"] ul li')
[year for year in years if year.text=='1-3年'][0].click()
time.sleep(2)
wd.find_element_by_id('funtype_input').click()
time.sleep(2)

func_list = wd.find_elements_by_css_selector('em[id*="funtype_click_center_right_list"]')
# 选取后端开发
# 这里顺序不能换，职能选择只能在最后，否则前面的选项会被清除
[func for func in func_list if func.text=='后端开发'][0].click()

sub_list = wd.find_elements_by_css_selector('em[id*="funtype_click_center_right_list_sub_category"]')
[sub for sub in sub_list if sub.text=='高级软件工程师'][0].click()
wd.find_element_by_id('funtype_click_bottom_save').click()
wd.find_element_by_css_selector('button[class="p_but"]').click()
jobs = wd.find_elements_by_css_selector('.dw_table div[class="el"]')
job_names = []
company_names = []
positions = []
salaries = []
update_times = []
# 去掉第一行title
for job in jobs:
    # 这里为什么 css_selector('p span').text不行？
    job_names.append(job.find_element_by_css_selector('.t1').text)
    company_names.append(job.find_element_by_css_selector('.t2').text)
    positions.append(job.find_element_by_css_selector('.t3').text)
    salaries.append(job.find_element_by_css_selector('.t4').text)
    update_times.append(job.find_element_by_css_selector('.t5').text)
for record in zip(job_names, company_names, positions, salaries, update_times):
    print(f'{record[0]} | {record[1]} | {record[2]} | {record[3]} | {record[4]}')
wd.quit()


# 股票
from selenium import webdriver
import time
wd = webdriver.Chrome('/Users/lyndon/Documents/Github/chromedriver')
wd.implicitly_wait(10)
wd.get('http://quote.eastmoney.com/stock_list.html')
stocks = wd.find_elements_by_css_selector('div[id="quotesearch"] ul li')
file_str = ''
for stock in stocks:
    stock_text = stock.find_element_by_css_selector('a[target="_blank"]').text
    name = stock_text.split('(')[0]
    code = stock_text.split('(')[1].strip(')')
    str_ap = name+':'+code+'\n'
    file_str+=str_ap
wd.quit()
with open('stock.txt','w') as f:
    f.write(file_str)