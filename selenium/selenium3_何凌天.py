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
# 每一个job
# 这样选择会把class=el title的也选进来，怎么样是exact select而不是wildcard select???
jobs = wd.find_elements_by_css_selector('.dw_table .el')
job_names = []
company_names = []
positions = []
salaries = []
update_times = []
# 去掉第一行title
for job in jobs[1:]:
    # 这里为什么 css_selector('p span').text不行？
    job_names.append(job.find_element_by_css_selector('.t1').text)
    company_names.append(job.find_element_by_css_selector('.t2').text)
    positions.append(job.find_element_by_css_selector('.t3').text)
    salaries.append(job.find_element_by_css_selector('.t4').text)
    update_times.append(job.find_element_by_css_selector('.t5').text)
for record in zip(job_names, company_names, positions, salaries, update_times):
    print(f'{record[0]} | {record[1]} | {record[2]} | {record[3]} | {record[4]}')
wd.quit()