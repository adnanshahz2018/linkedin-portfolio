#  Python imports
from selenium import webdriver 
from bs4 import BeautifulSoup
import requests, time

# Local imports
from scrape import scrape

class login:
    data = {}
    browser = None
    profile = scrape()

    def get_data(self):
        return self.data

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
        # Calling the Scrape function
        self.browser = browser
        self.scrape_profile()

    def scrape_profile(self):
        self.browser.get('https://www.linkedin.com/in/adnanxshah/')
        # Get scroll height
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        for i in range(5):
            try:
                # Scroll down to bottom
                self.browser.execute_script("window.scrollTo(0, window.scrollY + 200);")
                # Wait to load page
                time.sleep(1)
                # Calculate new scroll height and compare with last scroll height
                new_height = self.browser.execute_script("return document.body.scrollHeight")
                # if new_height == last_height:   break
                # last_height = new_height
            except:
                pass

        self.profile.set_source( (self.browser.page_source) )
        name = self.profile.get_name()
        self.data['name'] = name
        profession = self.profile.get_profession()
        self.data['profession'] = profession 
        about = self.profile.get_about()
        self.data['about'] = about
        experience = self.profile.get_experience()
        self.data['experience'] = experience
        if experience is not None:
            # print(profession)
            # print(about)
            for exp in experience:
                # print(exp)
                # print(exp['profession'])
                # print(exp['company'])
                # print(exp['date'])
                # print(exp['description'])
                pass
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

