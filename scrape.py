
#  Python imports
from bs4 import BeautifulSoup

class scrape:
    soup = None
    Source = ''

    def set_source(self, source):
        self.Source = source
        self.soup = BeautifulSoup(self.Source, 'lxml')

    def get_name(self):
        name = self.soup.find('li', attrs={'class': 'inline t-24 t-black t-normal break-words'}).get_text()
        return name

    def get_profession(self):
        profession = self.soup.find('h2', attrs={'class': 'mt1 t-18 t-black t-normal break-words'}).get_text()
        return profession

    def get_about(self):
        about = ''
        element = self.soup.find('p', attrs={'class': 'pv-about__summary-text mt4 t-14 ember-view'})
        spans = element.find_all('span')
        for span in spans:  about += span.text
        about = about.replace('\n','')
        return about

    def get_experience(self):
        exp = self.soup.find('section', attrs={'id': 'experience-section'})
        return exp

    def get_education(self):
        return ''

    def get_project(self):
        return ''

    def get_skill(self):
        return ''

    def get_profile_picture(self):
        return ''



if __name__ == "__main__":
    s = scrape()
    s.get_source()
    
    s.get_experience()
    


"""     Required Data

1. Name
2. Profession
3. About
4. Profile Picture
5. Experience
6. Education 
7. Projects 
8. Skills

- Certificates
- Accomplishments


"""