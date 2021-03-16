from selenium import webdriver
browser=webdriver.Chrome('c:/chromedriver/chromedriver.exe')
browser.get("link")
textfield=browser.find_element_by_css_selector('.fdfh')

############

textfield.send_keys(u'\ue007')

#############

