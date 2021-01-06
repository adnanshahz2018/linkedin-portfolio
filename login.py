
#  Python imports
from selenium import webdriver 
from bs4 import BeautifulSoup
import requests
import time

def sneak_in():
    # startwebdriver ( A selenium driven web brwoser)
    browser = webdriver.Chrome('chromedriver.exe') 

    # Acess LinkedIn Login Page
    browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    
    one, two = get_assets()

    # Login Credentials
    elementID = browser.find_element_by_id('username')
    elementID.send_keys(one)

    elementID = browser.find_element_by_id('password')
    elementID.send_keys(two)

    time.sleep(2)
    elementID.submit()

    browser.get('https://www.linkedin.com/in/adnanxshah/')
    source = browser.page_source

    b = BeautifulSoup(source, 'lxml')
    prof = b.find_all('h2', attrs={'class':'mt1 t-18 t-black t-normal break-words'})
    for p in prof:
        print('\n\t Profession = ', p.get_text() )

def get_assets():
    source = requests.get('https://github.com/adnanshahz2018/portfolio-assests/blob/main/README.md').text
    soup = BeautifulSoup(source, 'lxml')
    article = soup.find('article', attrs={'class':'markdown-body entry-content container-lg'})
    trigger = article.find_all('p')
    labels = trigger[0].text.split('\n')

    return labels[0], labels[1]    
    

if __name__ == "__main__":
    print('\t\tStarting Web Browser ')
    sneak_in()


    #  ...