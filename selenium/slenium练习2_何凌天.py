from selenium import webdriver

wd = webdriver.Chrome('/Users/lyndon/Documents/Github/chromedriver')
wd.implicitly_wait(10)
wd.get('http://music.taihe.com/top/new')
all_elements = [x.get_attribute('class') for x in wd.find_elements_by_css_selector('li div span:nth-child(2) i')]
target_index = [i for i,e in enumerate(all_elements) if e=='up']
target_divs = wd.find_elements_by_css_selector('li div')
for i in target_index:
    title = target_divs[i].find_element_by_css_selector('span[class*="song-title"]').text
    if '影视原声' not in title:
        singer = target_divs[i].find_element_by_css_selector('span[class*="singer"]').text
        print(f'{title:<8}:{singer:>8}')
wd.quit()