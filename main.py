
#  Local imports
import Components as c
from login import login


class Portfolio:
    def creaefile(self, name, data):
        data = self.get_candidate_data(data)
        with open(name + '.html', 'w+') as f:
            print('\tWriting Data in file')
            f.write(data)

    def get_candidate_data(self, data):
        n1 = c.name_profession(data['name'], data['profession'], data['profile_image'])
        explist = list() 
        for exp in data['experience']:
            pr = co = da = de = img = ''
            print('\n Exp:\n ', exp, '\n' )
            try:
                if exp['profession']:   pr = exp['profession']
            except:
                pass
            try:
                if exp['company']:      co = exp['company']
            except:
                pass
            try:
                if exp['date']:         da = exp['date']
            except:
                pass
            try:
                if exp['description']:  de = exp['description']
            except:
                pass
            try:
                if exp['image']:        img = exp['image']
            except:
                pass
            e = c.experience_job_component(pr, co, da, de, img) 
            explist.append(e)
            
        part1 = c.DOCUMENT_START + c.HEAD + c.BODY_START + c.HEADER + n1 + c.about_section(data['about'])
        part2 = c.EXPERIENCE_SECTION_START
        for exp in explist:
            part2 += exp
        part2 += c.EXPERIENCE_SECTION_END

        edulist = list() 
        for edu in data['education']:
            uni = deg = date = img = ''
            # print('\n Edu:\n ', edu, '\n' )
            try:
                if edu['univ']:    uni = edu['univ']
            except:
                pass
            try:
                if edu['date']:    date = edu['date']
            except:
                pass
            try:
                if edu['degree']:  deg = edu['degree']
            except:
                pass
            try:
                if edu['image']:   img = edu['image']
            except:
                pass
            e = c.education_component(uni, deg, date, img) 
            edulist.append(e)

        part3 = c.EDUCATION_SECTION_START
        for edu in edulist:
            if edu: part3 += edu
        part3 += c.EDUCATION_SECTION_END

        part4 = c.PROJECT_SECTION_START + c.project_component('scrape', 'web scraping') + c.project_component('XSS Automation', "Detecting Vulnerbailties") + c.PROJECT_SECTION_END
        part5 = c.BODY_END + c.DOCUMENT_END

        data =  part1 + part2 + part3 + part4 + part5
        return data


if __name__ == "__main__":
    #  Sign-in to the 
    log = login()
    log.sneak_in()
    # log.scrape_profile('adnanxshah')
    # log.scrape_profile('salmannaseer')
    log.scrape_profile('ibrahim-khan-3768a3183')
    data = log.get_data()

    # Create and Save Data in the .html file
    P = Portfolio()
    # P.creaefile('adnanshah', data)
    # P.creaefile('salmannaseer', data)
    P.creaefile('ibrahimkhan', data)

