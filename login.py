from selenium import webdriver
from time import sleep
from info import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
def google_login(url,browser):
    wait = WebDriverWait(browser, 100)
    browser.get(url)
    wait.until(EC.presence_of_element_located((By.ID, 'identifierId'))).send_keys(youtube_id)
    browser.find_element_by_id('identifierNext').click()
    wait.until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys(youtube_password)
    browser.find_element_by_id('passwordNext').click()
    print('登录youtube成功！')
def twitter_login(url,browser):
    browser.get(url)
    sleep(5)
    browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input').send_keys(teweet_id)
    browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input').send_keys(teweet_password)
    browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button').click()
    sleep(5)
    print('登录twitter成功')
def main_login(url):
    # 设置浏览器
    chromeOptions = webdriver.ChromeOptions()
    # chromeOptions.add_argument('headless')
    chromeOptions.add_argument("--proxy-server=http://127.0.0.1:8087")
    chromeOptions.add_argument('disable-infobars')
    browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser.maximize_window()
    browser.get(url)
    browser.find_element_by_id('username').send_keys(youlike_id)
    browser.find_element_by_id('password').send_keys(youlike_password)
    sleep(1)
    browser.find_element_by_xpath('//input[@type="submit"]').click()
    sleep(5)
    print('登录youlike成功')
    google_login(google,browser)
    sleep(3)
    twitter_login(twitter,browser)
    return browser