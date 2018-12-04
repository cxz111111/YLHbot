# -*-coding:utf-8 -*-
from info import *
from subtwitter import get_twitter
from subyoutube import get_youtube
import sys
from login import main_login

if __name__ == '__main__':
    browser = main_login(youlike)
    if(sys.argv[1]=='ty'):
        get_twitter(browser)
        get_youtube(browser)
    if(sys.argv[1]=='t'):
        get_twitter(browser)
    if(sys.argv[1]=='y'):
        get_youtube(browser)
    else:
        print('出错了')
    browser.quit()
