# A program that using selenium, logs in to your email account and sends an emails of the strings to the provided addresses
# Going to add sys.argv input mail instead of this version...
from selenium import webdriver
import time


# login with selenium
browser = webdriver.Firefox()
browser.get('https://mail.protonmail.com/login')
time.sleep(2)

nameElem = browser.find_element_by_id('username')
nameElem.send_keys('your user id')

passElem = browser.find_element_by_id('password')
passElem.send_keys('your password')
passElem.submit()
time.sleep(2)
titles = ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7'] #these are for example and needs to be filled
subjects = ['test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7'] #these are for example and needs to be filled
mailadress = [1, 2, 3, 4, 5, 6, 7] #these are for example and needs to be filled
# locate create mail button, to, title, and text.
for i in range(len(titles)):
    time.sleep(5)
    create = browser.find_element_by_id('ptSidebar')
    x = create.find_element_by_tag_name('button')
    x.click()
    time.sleep(2)
    receiver = browser.find_element_by_xpath('//input[@name="autocomplete"]')

    receiver.send_keys(mailadress[i])
    subject = browser.find_element_by_xpath(
        '//input[@ng-model="message.Subject"]')
    subject.send_keys(titles[i])
    browser.switch_to.frame(0)

    body = browser.find_element_by_xpath('/html/body')
    body.send_keys(f'This is a test message {subjects[i]}, thanks!')

    browser.switch_to.default_content()

    y = browser.find_element_by_xpath(
        '/html/body/div[2]/form[1]/div/footer/div/button[3]')
    y.click()
browser.quit()
