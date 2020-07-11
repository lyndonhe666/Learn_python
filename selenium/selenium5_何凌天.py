from selenium import webdriver
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

def switch_window(wd, target_handle):
    for handle in wd.window_handles:
        wd.switch_to.window(handle)
        if target_handle in wd.title:
            break

def find_job_detail(wd):
    try:
        res = wd.find_element_by_css_selector('div[class="bmsg job_msg inbox')
        return res.text
    except NoSuchElementException:
        return None

# 在每一页上找到所有的工作
def page_wise():
    # 以df方式储存
    jobs = wd.find_elements_by_css_selector('.dw_table div[class="el"]')
    # 取非前程无忧自己的工作
    jobs = [x for x in jobs if '前程无忧' not in x.find_element_by_css_selector('.t2').text]
    job_names = []
    company_names = []
    positions = []
    salaries = []
    update_times = []
    job_details = []
    for job in jobs:
        job_name = job.find_element_by_css_selector('.t1').text
        job_names.append(job_name)
        company_names.append(job.find_element_by_css_selector('.t2').text)
        positions.append(job.find_element_by_css_selector('.t3').text)
        salaries.append(job.find_element_by_css_selector('.t4').text)
        update_times.append(job.find_element_by_css_selector('.t5').text)
        # 进入工作详情页
        job.find_element_by_tag_name('a').click()
        # 是否需要等待加载
        # time.sleep(2)
        # 遍历进入工作详情页，加入职位信息
        switch_window(wd, job_name)
        job_detail = find_job_detail(wd)
        job_details.append(job_detail)
        if job_detail==None:
            # 没有找到相应信息,把录入的删除
            job_names.pop()
            company_names.pop()
            positions.pop()
            salaries.pop()
            update_times.pop()
            job_details.pop()
        wd.close()
        # 切换回base
        wd.switch_to.window(base_handle)
    data = {
        'job_name':job_names,
        'company_name':company_names,
        'position':positions,
    'salarie':salaries,
    'update_time': update_times,
    'job_detail':job_details
    }
    return pd.DataFrame(data)

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
time.sleep(5)
# 定位到已经选择的地区并点击删除
selected_poss = wd.find_elements_by_css_selector('span[id*="work_position_click_multiple_selected_each"]')
for ele in selected_poss:
    ele.click()
cities = wd.find_elements_by_css_selector('em[id*="work_position_click_center_right"]')
sh = [city for city in cities if city.text=='上海'][0]
sh.click()
wd.find_element_by_id('work_position_click_bottom_save').click()
wd.find_element_by_css_selector('#kwdselectid').send_keys('python')
wd.find_element_by_css_selector('div[class*=fltr] button[onclick*="kwdGoSearch"]').click()
base_handle = wd.current_window_handle
dfs = []

# 找到选择第几页的元素
for i in range(1,11):
    navigator = wd.find_element_by_css_selector('input[id="jump_page"]')
    navigator.clear()
    navigator.send_keys(str(i))
    wd.find_element_by_css_selector('span[class="og_but"]').click()
    # 等待加载
    time.sleep(2)
    dfs.append(page_wise())

# 合并dfs
total_df = pd.concat(dfs)
wd.quit()
total_df.to_csv('51job.csv',index=False)