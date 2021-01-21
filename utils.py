
def get_default_msg():
    text = '''Hi! you can enter the keywords to acquire some informations about me:

 * education, background: My education background.
 * cmlab, lab: Information about the lab I'm currently in.
 * intern: My past intern experience.
 * skill(s): The CS related skills that I have.
 * contact: The ways to contact me. 
 * award, honor: Display the selected honors and awards
    
E.g. Enter 'cmlab' or 'lab' can get the information of my lab works.'''
    
    return text

def get_education():
    text = "I'm a senior in National Taiwan University (NTU), majoring in Computer Science & Information Engineering. Until now, my average GPA is 4.17."

    return text

def get_lab_msg():
    text = "I'm currently in Communications and Multimedia Laboratory (CMLab), under the instruction of prof. Winston Hsu.\n"
    text += '''These are topics that l've researched before:
    * Cross-domain few-shot learning
    * Object referring
    * Video trope analysis (ongoing)'''

    return text

def get_intern_msg():
    text = "In last two summer vacations, I've worked in Perfect Corp. and ASUS Intelligent Cloud Service Center(AICS) as an intern.\n"
    text += "The following shows the detail work I've done:\n"
    text += '''
* Perfect Corp.:
  - Period: Jul. 2019 - Aug. 2019
  - Worked in RD-AI-AT team 
  - Extend existing models, and deal with CV-related problem by using deep learning

* AICS:
  - Period: Jul. 2020 - Sep. 2020
  - Worked in Medical-NLU team
  - Add features in their medical searching engine (EMR search)
  - Adapt NLU to help structuring medical record'''

    return text

def get_skill_msg():
    text = '''Those are the CS-related skills that I have:

C/C++ programming
Python programming
Machine learning / Deep learning
Shell scripts
Linux
Basic computer security
Basic frontend / backend'''

    return text

def get_contact_msg():
    text = 'E-mail: b06902066@ntu.edu.tw\n'
    text += 'Phone: 0963-831-276\n'
    text += 'Linkedin: /bing-chen-tsai'

    return text

def get_award_msg():
    text = "Those are the awards that I got:\n"
    text += '''
* Ministry of Education Intercollegiate AI CUP 2019
  - Awards: Honorable Mention
  - This competition is focus on thesis topic classification by utilizing NLP models.

* Thematic Exhibition of Undergraduate
  - Awards: Honorable Mention
  - Our presentation topic: Large Margin Mechanism and Pseudo Query Set on CrossDomain Few-Shot Learning

* Presidential Award
  - In second semester of academic year 2019-2020.'''