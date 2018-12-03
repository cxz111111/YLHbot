# -*-coding:utf-8 -*-
from time import sleep
from info import *
from login import main_login
from PIL import Image
from get_captch import get_result

def youtube_subscribers(url,browser):#一分钟订阅5个
    browser.get(url)
    sleep(5)
    browser.find_element_by_xpath('//*[@id]/center/a').click()
    for j in range(24):
        sleep(5)
        browser.find_element_by_xpath('//*[@id="FBBox"]/a').click()
        sleep(3)
        windows = browser.window_handles
        browser.switch_to.window(windows[-1])
        try:
            key = browser.find_element_by_xpath(
                '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button').get_attribute("aria-label")
            if(key =='订阅此频道。'):
                browser.find_element_by_xpath('//*[@id="subscribe-button"]').click()
                sleep(5)
                browser.close()
                browser.switch_to.window(windows[0])
            else:
                browser.close()
                browser.switch_to.window(windows[0])
                browser.find_element_by_xpath('//*[@id="DoesLike"]/a').click()
        except:
            browser.close()
            browser.switch_to.window(windows[0])
            browser.find_element_by_xpath('//*[@id="DoesLike"]/a').click()
        print('第' + str(j) + '次')
    sleep(46)
def youtube_likes(url,browser):#一分钟订阅5个
    for i in range(2):
        browser.get(url)
        browser.find_element_by_xpath('//*[@id]/center/a').click()
        sleep(5)
        for j in range(20):
            sleep(15)
            browser.find_element_by_xpath('//*[@id="FBBox"]/a').click()
            sleep(2)
            windows = browser.window_handles
            browser.switch_to.window(windows[-1])
            sleep(5)
            key = browser.find_element_by_xpath(
                '//*[@id="button" and @aria-pressed]').get_attribute("aria-pressed")
            if(key =='false'):
                browser.find_element_by_xpath('//*[@id="button" and @aria-pressed]').click()
                sleep(5)
                browser.close()
                browser.switch_to.window(windows[0])
            else:
                browser.close()
                browser.switch_to.window(windows[0])
                browser.find_element_by_xpath('//*[@id="DoesLike"]/a').click()
        print('第'+str(i)+'次')
def youtube_views(url,browser):
    browser.get(url)
    sleep(3)
    element = browser.find_element_by_xpath('//*[@id="captcha"]/table[1]/tbody/tr/td/img')
    browser.save_screenshot('screenshot.png')

    left = element.location['x']
    top = element.location['y']
    right = element.location['x'] + element.size['width']
    bottom = element.location['y'] + element.size['height']

    im = Image.open('screenshot.png')
    im = im.crop((left, top, right, bottom))
    im = im.resize([120,40])
    result = get_result(im)
    print(result)
    browser.find_element_by_xpath('//*[@id="captcha"]/table[2]/tbody/tr/td/input[1]').send_keys(str(result))
    browser.find_element_by_xpath('//*[@id="captcha"]/table[2]/tbody/tr/td/input[2]').click()
    sleep(3)
    for i in range(6):
        # if (browser.find_element_by_xpath('//*/font/span').text == ''):
        browser.find_element_by_xpath('//*[@id="listall"]/center/a[1]').click()
        sleep(1)
        a = browser.find_element_by_xpath('//*[@id]/font').text
        sleep(int(a[-3:]))
        sleep(3)
        i = i+1
        print('第'+str(i)+'次')
def get_youtube(browser):
    try:
        youtube_subscribers(y_follow,browser)
    except Exception as e:
        print(e)
    try:
        youtube_likes(y_like,browser)
    except Exception as e:
        print(e)
    try:
        youtube_views(y_view,browser)
    except Exception as e:
        print(e)
if __name__ == '__main__':
    browser = main_login(youlike)
    get_youtube(browser)
    print('完成youtube任务！')
