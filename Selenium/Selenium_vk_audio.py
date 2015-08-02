__author__ = 'lucie'

from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://vk.com/')
inputlogin = driver.find_element_by_id('quick_email')
inputlogin.send_keys('luciefel@yandex.ru')
inputpass = driver.find_element_by_id('quick_pass')
inputpass.send_keys('fksqRJHJKM99')
submitbutton = driver.find_element_by_id('quick_login_button')
submitbutton.click()
audioslink = driver.find_element_by_xpath('//a[@href="/audios6534236"]')
audioslink.click()