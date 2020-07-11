from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import re

# 作业1
def check_exist(targets,tabs):
    return [target for target in targets if re.search(target, ' '.join([tab.text for tab in tabs]))]


wd = webdriver.Chrome('/Users/lyndon/Documents/Github/chromedriver')
wd.implicitly_wait(10)
wd.get('https://www.vmall.com/')

base_handle = wd.current_window_handle
wd.find_element_by_css_selector('a[href*="huawei.com"]').click()
wd.switch_to_window(wd.window_handles[1])
_=wd.find_element_by_css_selector('ul[class="main-nav__list"]')
tabs = _.find_elements_by_css_selector('li a')
tabs = [tab for tab in tabs if tab.text!='']
targets="""手机
笔记本
平板
智慧屏
穿戴
更多产品
EMUI
服务支持
零售店"""
print(check_exist(targets.splitlines(),tabs))

wd.switch_to_window(base_handle)
# ac = ActionChains(wd)
# 悬停
# ac.move_to_element(
#     wd.find_element_by_css_selector('#zxnav_2 > div.category-item-bg > div')
# ).perform()
# 悬停只能显示大概1秒，然后sub category就不显示了
wd.find_element_by_css_selector('#zxnav_2 > div.category-item-bg > div').click()
#zxnav_2 > div.category-panels.category-panels-1
tabs = wd.find_elements_by_css_selector('#zxnav_2 > div.category-panels.category-panels-1 li a p')
targets = """华为MatePad 系列
华为畅享 系列
荣耀数字系列
荣耀畅玩系列"""
print(check_exist(targets.splitlines(),tabs))
wd.quit()


# 作业2
wd = webdriver.Chrome('/Users/lyndon/Documents/Github/chromedriver')
wd.implicitly_wait(10)
wd.get('https://tinypng.com/')
path = '/Users/lyndon/Desktop/selenium_test.png'
wd.find_element_by_css_selector('#top > section > section > input[type=file]').send_keys(path)
wd.quit()