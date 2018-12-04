# -*-coding:utf-8 -*-
from time import sleep
from info import *
from login import main_login
def twitter_tweets(url,browser):#每小时限制45次

    browser.get(url)
    sleep(10)
    print('twitter_tweets,start')
    for i in range(1):
        for j in range(9):
            nodes = browser.find_elements_by_xpath("//*[@id]/center/iframe")
            browser.switch_to.frame(nodes[j])
            browser.find_element_by_xpath('/html/body/center/a[1]').click()
            windows = browser.window_handles
            browser.switch_to.window(windows[-1])
            sleep(3)
            try:
                browser.find_element_by_class_name('button').click()
            except:
                pass
            browser.switch_to.window(windows[0])
            browser.switch_to.frame(nodes[j])
            sleep(3)
            try:
                browser.find_element_by_xpath('/html/body/center/a[2]').click()
            except:
                pass
            sleep(5)
            browser.switch_to.default_content()
        browser.get(url)
        sleep(10)
        print('第' + str(i) + '次')
    print('twitter_tweets,over')
def twitter_retweets(url,browser):
    browser.get(url)
    sleep(10)
    print('twitter_retweets,start')
    for i in range(1):
        for j in range(9):
            print('第' + str(j) + '次')
            nodes = browser.find_elements_by_xpath("//*[@id]/center/iframe")
            browser.switch_to.frame(nodes[j])
            browser.find_element_by_xpath('/html/body/center/a[1]').click()
            windows = browser.window_handles
            browser.switch_to.window(windows[-1])
            sleep(5)
            try:
                browser.find_element_by_name('commit').click()
                sleep(3)
            except Exception as e:
                print(e)
                browser.switch_to.window(windows[0])
                browser.switch_to.frame(nodes[j])
                browser.find_element_by_xpath('/html/body/center/a[2]').click()
                sleep(5)
                browser.switch_to.default_content()
            else:
                try:
                    browser.close()
                except:
                    pass
                browser.switch_to.window(windows[0])
                browser.switch_to.frame(nodes[j])
                browser.find_element_by_xpath('/html/body/center/a[2]').click()
                sleep(5)
                browser.switch_to.default_content()
        browser.get(url)
        sleep(10)
        print('第' + str(i) + '次')
    print('twitter_retweets,over')
def twitter_followers(url,browser):
    browser.get(url)
    sleep(10)
    print('twitter_followers,start')
    for i in range(1):
        nodes = browser.find_elements_by_xpath('//*[@id]/center/center')
        for j in range(len(nodes)):
            sleep(3)
            browser.find_elements_by_xpath('//*[@id]/center/center/a[1]')[j].click()
            sleep(2)
            windows = browser.window_handles
            browser.switch_to.window(windows[-1])
            sleep(3)
            try:
                key = browser.find_element_by_xpath('//*[@id="follow_btn_form"]').get_attribute('class')
                if (key == 'follow '):
                    browser.find_element_by_xpath('//*[@id="follow_btn_form"]').click()
                    sleep(2)
            except:
                pass
            finally:
                browser.close()
                browser.switch_to.window(windows[0])
                browser.find_elements_by_xpath('//*[@id]/center/center/a[2]')[j].click()
            sleep(5)
            state = browser.find_element_by_xpath('//*[@id="txtHint"]/table/tbody/tr[1]/td').text
            if (state == 'Success!'):
                pass
            else:
                browser.find_elements_by_xpath('//*[@id]/center/font/a')[j].click()
                sleep(1)
        print('第'+str(i)+'次')
        browser.get(url)
        sleep(5)
    print('twitter_followers,over')
def twitter_likes(url,browser):#限制每小时15个like
    browser.get(url)
    sleep(10)
    print('twitter_likes,start')
    for i in range(1):
        for j in range(9):
            nodes = browser.find_elements_by_xpath("//*[@id]/center/iframe")
            browser.switch_to.frame(nodes[j])
            browser.find_element_by_xpath('/html/body/center/a[1]').click()
            windows = browser.window_handles
            browser.switch_to.window(windows[-1])
            sleep(5)
            try:
                browser.find_element_by_name('commit').click()
                sleep(3)
            except Exception as e:
                print(e)
            try:
                browser.close()
            except Exception as e:
                print(e)
            browser.switch_to.window(windows[0])
            browser.switch_to.frame(nodes[j])
            browser.find_element_by_xpath('/html/body/center/a[2]').click()
            sleep(5)
            browser.switch_to.default_content()
        browser.get(url)
        sleep(10)
        print('第' + str(i) + '次')
    print('twitter_likes,over')
def get_twitter(browser):
    try:
        twitter_followers(t_follow, browser)
    except Exception as e:
        print(e)
    try:
        twitter_likes(t_like, browser)
    except Exception as e:
        print(e)
    try:
        twitter_tweets(t_tweet, browser)
    except Exception as e:
        print(e)
    try:
        twitter_retweets(t_retweet, browser)
    except Exception as e:
        print(e)
    print('完成twitter任务！')

if __name__ =='__main__':
    browser = main_login(youlike)
    get_twitter(browser)
    print('完成twitter任务！')
