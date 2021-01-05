
import Components as c

class Portfolio:
    
    def creaefile(self, name):
        data = self.get_candidate_data()
        with open(name + '.html', 'w+') as f:
            f.write(data)

    def get_candidate_data(self):
        n1 = c.name_profession('adnan', 'researcher') 
        e1 = c.experience_job_component('VisionX', 'Developer', 'I want to grow') 
        e2 = c.experience_job_component('Arbisoft', 'Engineer', 'I am Learning Fast ')
        part1 = c.DOCUMENT_START + c.HEAD + c.BODY_START + c.HEADER + n1 + c.about_section('About Content')
        part2 = c.EXPERIENCE_SECTION_START + e1 + e2 + c.EXPERIENCE_SECTION_END
        part3 = c.EDUCATION_SECTION_START + c.education_component('namal', 'BS CS', 'Four Year Bachelor Degree') + c.education_component('Air University', 'MS CYS', 'Capital Islamabad') + c.EDUCATION_SECTION_END
        part4 = c.PROJECT_SECTION_START + c.project_component('scrape', 'web scraping') + c.project_component('XSS Automation', "Detecting Vulnerbailties") + c.PROJECT_SECTION_END
        part5 = c.BODY_END + c.DOCUMENT_END
        return  part1 + part2 + part3 + part4 + part5


if __name__ == "__main__":
    P = Portfolio()
    P.creaefile('adnanshah')