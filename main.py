# -*-coding:utf-8 -*-
from info import *
from subtwitter import get_twitter
from subyoutube import get_youtube

from login import main_login

if __name__ == '__main__':
    browser = main_login(youlike)
    get_twitter(browser)
    get_youtube(browser)
    browser.close()
