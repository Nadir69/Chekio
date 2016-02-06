from selenium.webdriver import firefox, ActionChains

__author__ = 'lucie'

from selenium import webdriver



fp = webdriver.FirefoxProfile('/home/merlo/.mozilla/firefox/0id4l4jm.default/')

driver = webdriver.Firefox(firefox_profile=fp)
driver.get('http://vk.com/')
# inputlogin = driver.find_element_by_id('quick_email')
# inputlogin.send_keys('luciefel@yandex.ru')
# inputpass = driver.find_element_by_id('quick_pass')
# inputpass.send_keys('fksqRJHJKM99')
# submitbutton = driver.find_element_by_id('quick_login_button')
# submitbutton.click()
driver.implicitly_wait(5)
audioslink = driver.find_element_by_xpath('//a[@href="/audios6534236"]')
audioslink.click()
driver.implicitly_wait(7)
# driver.execute_script("window.scrollTo(0, 1000);")
downloadbutton = driver.find_elements_by_class_name('vk-downloader-button')
print 'len(downloadbutton) =', len(downloadbutton)
a = 0
while a < len(downloadbutton):
    print 'a =', a
    a = len(downloadbutton)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.implicitly_wait(2)
    downloadbutton = driver.find_elements_by_class_name('vk-downloader-button')
    print len(downloadbutton)


ActionChains(driver).move_to_element(downloadbutton[3]).click(downloadbutton[3]).perform()
#
# for item in downloadbutton[:2]:
#     item.click()
#     driver.implicitly_wait(2)
#