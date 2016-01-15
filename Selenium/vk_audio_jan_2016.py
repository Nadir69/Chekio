__author__ = 'lucie'

from selenium import webdriver

fp = webdriver.FirefoxProfile('/home/merlo/.mozilla/firefox/0id4l4jm.default/')
# fp.set_preference("extensions.vk@sergeykolosov.mp.install-event-fired", True)



driver = webdriver.Firefox(firefox_profile=fp)
driver.get('http://vk.com/')
inputlogin = driver.find_element_by_id('quick_email')
inputlogin.send_keys('luciefel@yandex.ru')
inputpass = driver.find_element_by_id('quick_pass')
inputpass.send_keys('fksqRJHJKM99')
submitbutton = driver.find_element_by_id('quick_login_button')
submitbutton.click()
driver.implicitly_wait(5)
audioslink = driver.find_element_by_xpath('/html/body/div[11]/div/div/div/div[2]/ol/li[5]')
audioslink.click()