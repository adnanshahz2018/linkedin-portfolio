
#  Python imports
from selenium import webdriver 
from bs4 import BeautifulSoup
import requests
import time


if __name__ == "__main__":
    print('Starting Web Browser ')

    # startwebdriver ( A selenium driven web brwoser)
    browser = webdriver.Chrome('chromedriver.exe') 

    # Acess LinkedIn Login Page
    browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    
    # Login Credentials
    elementID = browser.find_element_by_id('username')
    elementID.send_keys('adnanshahz2015@gmail.com')

    elementID = browser.find_element_by_id('password')
    elementID.send_keys('zeshan2015')

    time.sleep(2)
    elementID.submit()

    browser.get('https://www.linkedin.com/in/adnanxshah/')
    source = browser.page_source

    b = BeautifulSoup(source, 'lxml')
    prof = b.find_all('h2', attrs={'class':'mt1 t-18 t-black t-normal break-words'})
    for p in prof:
        print('\n\t Profession = ', p.get_text() )

   

    #  ...