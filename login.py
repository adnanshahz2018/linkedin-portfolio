#  Python imports
from selenium import webdriver 
from bs4 import BeautifulSoup
import requests, time

# Local imports
from scrape import scrape

class login:
    browser = None
    profile = scrape()

    def sneak_in(self):
        # startwebdriver ( A selenium driven web brwoser)
        browser = webdriver.Chrome('chromedriver.exe') 
        # Acess LinkedIn Login Page
        browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        one, two = self.get_assets()

        # Login Credentials
        elementID = browser.find_element_by_id('username')
        elementID.send_keys(one)
        elementID = browser.find_element_by_id('password')
        elementID.send_keys(two)
        elementID.submit()

        self.browser = browser
        self.scrape_profile()

    def scrape_profile(self):
        self.browser.get('https://www.linkedin.com/in/adnanxshah/')
        SCROLL_PAUSE_TIME = 1
        # Get scroll height
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        for i in range(5):
            # Scroll down to bottom
            self.browser.execute_script("window.scrollTo(0, window.scrollY + 200);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:   
                break
            last_height = new_height

        self.profile.set_source( (self.browser.page_source) )
        name = self.profile.get_name()
        profession = self.profile.get_profession()
        about = self.profile.get_about()
        experience = self.profile.get_experience()
        print(experience)
        if experience is not None:
            print(name)
            print(profession)
            print(about)
            print(experience)
        else:
            time.sleep(1)
            self.scrape_profile()

    def get_assets(self):
        source = requests.get('https://github.com/adnanshahz2018/portfolio-assests/blob/main/README.md').text
        soup = BeautifulSoup(source, 'lxml')
        article = soup.find('article', attrs={'class':'markdown-body entry-content container-lg'})
        trigger = article.find_all('p')
        labels = trigger[0].text.split('\n')
        return labels[0], labels[1]    
        

if __name__ == "__main__":
    print('\t\tStarting Web Browser ')
    log = login()
    log.sneak_in()

    input('Press any Key to Terminate the Program')


    #  ...