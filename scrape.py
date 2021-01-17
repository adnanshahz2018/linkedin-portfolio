
#  Python imports
from Components import education_component
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

    def get_profile_image(self):
        image = self.soup.find('img', attrs={'class': 'pv-top-card__photo presence-entity__image EntityPhoto-circle-9 lazy-image ember-view'})['src']
        return image
        
    def get_about(self):
        about = ''
        element = self.soup.find('p', attrs={'class': 'pv-about__summary-text mt4 t-14 ember-view'})
        spans = element.find_all('span')
        for span in spans:  about += span.text
        about = about.replace('\n','')
        return about

    def get_experience(self):
        exp_list = list()
        experience = self.soup.find('section', attrs={'id': 'experience-section'})
        section_list = experience.find_all('li', attrs={'class': 'pv-entity__position-group-pager pv-profile-section__list-item ember-view'})
        for lis in section_list:
            info ={}
            if not lis:
                continue
            else:
                sec = lis.find('section')
            try:
                img = sec.find('img')
                # print(' ------------------------------------------------------------------------------------------------- \n Scrape-Source:\n', img['src'])
                info['image'] = img['src']
            except:
                pass
            try:  
                prof = sec.find('h3', attrs={'class': 't-16 t-black t-bold'})
                # print(' ------------------------------------------------------------------------------------------------- \n prof:\n', prof.get_text())
                info['profession'] = prof.get_text()
            except: 
                pass
            try:    
                h4 = sec.find('h4', attrs={'class': 'pv-entity__date-range t-14 t-black--light t-normal'})
                date = h4.find_all('span')[1].get_text()
                # print(' ------------------------------------------------------------------------------------------------- \n date:\n', date)
                info['date'] = date
            except: 
                pass
            try:    
                comp = sec.find('p', attrs={'class': 'pv-entity__secondary-title t-14 t-black t-normal'})
                # print(' ------------------------------------------------------------------------------------------------- \n comp:\n', comp.get_text())
                info['company'] = comp.get_text()
            except: 
                pass
            try:  
                div = lis.find('div', attrs={'class':'pv-entity__extra-details t-14 t-black--light ember-view'})
                desc = div.find('p', attrs={'class': 'pv-entity__description t-14 t-black t-normal inline-show-more-text inline-show-more-text--is-collapsed ember-view'})
                if not desc:
                    desc = div.find('p', attrs={'class': 'pv-entity__description t-14 t-black t-normal mb4 inline-show-more-text inline-show-more-text--is-collapsed ember-view'})
                # print('------------------------------------------------------------------------------------------------- \n desc:\n', desc.get_text())
                info['description'] = desc.get_text()
            except: 
                pass
                
            if info:
                exp_list.append(info)
        return exp_list
       
    def get_education(self):
        edu_list = list()
        education = self.soup.find('section', attrs={'id': 'education-section'})
        education_list = education.find_all('li', attrs={'class': 'pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view'})
        for lis in education_list:
            info = {}
            if not lis: continue
            try:
                img = lis.find('img')
                # print(' ------------------------------------------------------------------------------------------------- \n Scrape-Source:\n', img['src'])
                info['image'] = img['src']
            except:
                pass
            try:  
                uni = lis.find('h3', attrs={'class': 'pv-entity__school-name t-16 t-black t-bold'})
                # print(' ------------------------------------------------------------------------------------------------- \n University:\n', uni.get_text())
                info['univ'] = uni.get_text()
            except: 
                pass
            try:   
                data = lis.find_all('time')
                date = data[0].get_text() + '-' + data[1].get_text()
                # print(' ------------------------------------------------------------------------------------------------- \n date:\n', date)
                info['date'] = date
            except: 
                pass
            try: 
                deg = '' 
                spans = lis.find('span', attrs={'class':'pv-entity__comma-item'})
                for s in spans:
                    deg += s.get_text()
                # print('------------------------------------------------------------------------------------------------- \n deg:\n', desc.get_text())
                info['degree'] = deg.get_text()
            except: 
                pass
                
            if info:    
                edu_list.append(info)
        return edu_list
       
    def get_project(self):
        return ''

    def get_skill(self):
        return ''

    def get_profile_picture(self):
        return ''



if __name__ == "__main__":
    s = scrape()


"""     Required Data

1. Name
2. Profession
3. About
4. Profile Picture
5. Experience
6. Education 
7. Skills

- Projects 
- Certificates
- Accomplishments

"""