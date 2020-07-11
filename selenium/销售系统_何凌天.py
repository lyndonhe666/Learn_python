from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

def fill_blank(paras):
    # paras is a list containing variables
    input_boxes = list(wd.find_elements_by_css_selector('#root > div > section.content.container-fluid > div.col-lg-12.col-md-12.col-sm-12.add-one-area > div.col-lg-8.col-md-8.col-sm-8 > div'))
    for para in paras:
        for input_box in input_boxes:
            input_box.find_element_by_css_selector(':nth-child(1)').send_keys(para[input_box.text])
        # 点击添加
        wd.find_elements_by_css_selector("button[type='button']")[1].click()
        time.sleep(2)

wd = webdriver.Chrome('/Users/lyndon/Documents/Github/chromedriver')
wd.implicitly_wait(10)
wd.get('http://127.0.0.1/mgr/sign.html')

wd.find_element_by_id('username').send_keys('byhy')
wd.find_element_by_id('password').send_keys('88888888')
wd.find_element_by_css_selector("button[type='submit']").click()

# 添加药品
wd.find_element_by_css_selector("a[href='#/medicines']").click()
meds = """'青霉素盒装1','YP-32342341','青霉素注射液，每支15ml，20支装'
'青霉素盒装2','YP-32342342','青霉素注射液，每支15ml，30支装'
'青霉素盒装3','YP-32342343','青霉素注射液，每支15ml，40支装'
"""
med_paras=[dict(zip(['药品名称','编号','描述'],[x.strip("''") for x in med.split(',')])) for med in meds.splitlines()]
wd.find_element_by_css_selector("button[type='button']").click()
fill_blank(med_paras)

# 添加客户
wd.find_element_by_css_selector("a[href='#/customers']").click()
time.sleep(2)
clients = """'南京中医院1','2551867851','江苏省-南京市-秦淮区-汉中路-501'
'南京中医院2','2551867852','江苏省-南京市-秦淮区-汉中路-502'
'南京中医院3','2551867853','江苏省-南京市-秦淮区-汉中路-503'"""
client_paras = [dict(zip(['客户名','联系电话','地址'],[x.strip("''") for x in client.split(',')])) for client in clients.splitlines()]
wd.find_element_by_css_selector("button[type='button']").click()
fill_blank(client_paras)

# 添加订单
wd.find_element_by_css_selector("a[href='#/orders']").click()
time.sleep(2)
wd.find_element_by_css_selector("button[type='button']").click()
_ = wd.find_element_by_css_selector('#root > div > section.content.container-fluid > div.col-lg-12.col-md-12.col-sm-12.add-one-area > div.col-lg-8.col-md-8.col-sm-8')
input_boxes = _.find_elements_by_tag_name('div')
input_boxes[0].find_element_by_tag_name('input').send_keys('订单1')
client_selections = Select(input_boxes[1].find_element_by_tag_name('select'))
client_selections.select_by_visible_text("南京中医院2")
med_selections = Select(input_boxes[2].find_element_by_tag_name('select'))
med_selections.select_by_visible_text("青霉素盒装1")
wd.find_element_by_css_selector('input[type="number"]').send_keys('100')
wd.find_elements_by_css_selector("button[type='button']")[1].click()
time.sleep(5)
wd.quit()