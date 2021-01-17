
DOCUMENT_START = ''' 
<!DOCTYPE html>
<html class="no-js" lang="en">
'''

HEAD = ''' 
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>My Portfolio</title>
	<link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
	<link rel="icon" href="favicon.ico" type="image/x-icon">
    <link href="https://fonts.googleapis.com/css?family=Lato:300,400,700,900" rel="stylesheet">
    <link rel="stylesheet" href="libs/font-awesome/css/font-awesome.min.css">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/styles.css" rel="stylesheet">
</head>
'''

BODY_START = '''
<body>
    <div id="mobile-menu-open" class="shadow-large">
        <i class="fa fa-bars" aria-hidden="true"></i>
    </div>
'''

HEADER = '''
<header>
    <div id="mobile-menu-close">
        <span>Close</span> <i class="fa fa-times" aria-hidden="true"></i>
    </div>
    <div class="static-menu">
        <ul id="menu" class="shadow">
            <li>
                <a href="#about">About</a>
            </li>
            <li>
                <a href="#experience">Experience</a>
            </li>
            <li>
                <a href="#education">Education</a>
            </li>
            <li>
                <a href="#projects">Projects</a>
            </li>
            <li>
                <a href="#skills">Skills</a>
            </li>
            <li>
                <a href="#contact">Contact</a>
            </li>
        </ul>
    </div>
</header>
'''

EXPERIENCE_SECTION_START = '''
<div id="experience" class="background-alt">
<h2 class="heading">Experience</h2>

<div id="experience-timeline">
'''

EXPERIENCE_SECTION_END = '''
    </div>
</div>
'''

EDUCATION_SECTION_START = '''
<div id="education">
    <h2 class="heading">Education</h2>

'''

EDUCATION_SECTION_END = ''' 
</div>
'''

PROJECT_SECTION_START = '''
<div id="projects" class="background-alt">
<h2 class="heading">Projects</h2>
    <div class="container">
        <div class="row">
'''

PROJECT_SECTION_END = '''
        </div>
    </div>
</div>
'''

SKILL_SECTION_START = '''
    <div id="skills">
    <h2 class="heading">Skills</h2>
    <ul>
'''

SKILL_SECTION_START = '''
    </ul>
</div>
'''

BODY_END = '''
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="js/scripts.min.js"></script>
</body>
'''

DOCUMENT_END = '''
</html>
'''


def name_profession(name, profession, image):
    return f'''
            <div id="lead">
                <div id="lead-content">
                    <img class="profile-image" alt="''' + name + f'''" src="''' + image + f'''" /> 
                    <h2 style="color:black;">{name}</h2>
                    <h3>{profession}</h3>
                </div>
                <div id="lead-overlay"></div>
            </div>
            '''

def about_section(about_content):
    return f'''
            <div id="about">
                <div class="container">
                    <div class="row">
                        <div class="col-md-4">
                            <h2 class="heading">About Me</h2>
                        </div>
                        <div class="col-md-8">
                            <p>
                                {about_content}
                            </p>
                        </div>
                    </div>
                </div>
            </div>
            '''

def experience_job_component(profession, company, date, description, image):
    return f'''
            <div data-date="''' + date + f'''">
            <table>
                <td>
                <img src="''' + image + f'''" alt="''' + company + f'''" />
                </td>
                <td>
                    &nbsp; &nbsp;
                </td>
                <td>
                <h3> {company} </h3>
                <h4>{profession}</h4>
                </td>
                </table>
                <p>
                    {description}
                </p>
            </div>
            '''

def education_component(university, degree, date, image):
    return f'''
            <div class="education-block">
                <table>
                    <td>
                        <img src="''' + image + f'''" alt="''' + university + f'''" />
                    </td>
                    <span class="education-date">''' + date + f'''</span>
                    <td>
                        <h3>{university}</h3>
                        <h4>{degree}</h4>
                    <td>
                </table>
            </div>
            '''

def project_component(name, description, github_link='#'):
    return f'''
            <div class="project shadow-large">
            <div class="project-image">
                <img src="images/project.jpg" />
            </div>
            <div class="project-info">
                <h3>{name}</h3>
                <p>
                    {description}
                </p>
                <a href="{github_link}">View Project</a>
            </div>
        </div>
        '''


# ...