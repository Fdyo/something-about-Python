__author__ = 'Fdyo'
#coding: utf-8
import webbrowser
import urllib2
target_url = raw_input('Please enter the Microsoft Product url address:')
def create_affiliate_url(target_url):
    real_url = target_url.split('?')[0].strip()
    affiliate_url = 'http://clkuk.tradedoubler.com/click?p(235166)a(2771711)g(22471872)url(' + real_url + ')'
    return affiliate_url
affiliate_url = create_affiliate_url(target_url)
print affiliate_url
webbrowser.open(affiliate_url)



