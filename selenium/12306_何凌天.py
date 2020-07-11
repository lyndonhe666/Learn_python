from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

wd = webdriver.Chrome('/Users/lyndon/Documents/Github/chromedriver')
wd.implicitly_wait(10)
wd.get('https://kyfw.12306.cn/otn/leftTicket/init')

wd.find_element_by_css_selector('#fromStationText').click()
wd.find_element_by_css_selector('#fromStationText').send_keys('南京南\n')

wd.find_element_by_css_selector('#toStationText').click()
wd.find_element_by_css_selector('#toStationText').send_keys('杭州东\n')

wd.find_element_by_css_selector('#date_range > ul > li:nth-child(2)').click()

time_spans = Select(wd.find_element_by_css_selector('#cc_start_time'))
time_spans.select_by_visible_text('06:00--12:00')

elements = wd.find_elements_by_xpath('//*[@id="queryLeftTable"]//tr[contains(@id,"ticket")]/td[4][@class]/../td/div//a')
for e in elements:
    print(e.text)
wd.quit()