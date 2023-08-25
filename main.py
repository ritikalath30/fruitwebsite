from bs4 import BeautifulSoup
# with open('index.html','r') as html_file:
#     content = html_file.read()
#     # print(content)
#     soup =BeautifulSoup(content,'lxml')
#     # print(soup.prettify())
#     tags = soup.find('h1')
#     print(tags)
import requests
html_text = requests.get('https://www.udemy.com/course/design-and-develop-a-killer-website-with-html5-and-css3/').text
# print(html_text)
soup = BeautifulSoup(html_text,'lxml')
instructor_name = soup.find('span',class_ = 'instructor-links--names--7UPZj').text
print(instructor_name)
course = soup.find('div',class_ = 'course-landing-page__main-content component-margin')
print(f'''
Instructor: {instructor_name}
Course Outcome: 
''')
course_outcomes = course.find_all('span',class_ = 'what-you-will-learn--objective-item--ECarc')
for course_outcome in course_outcomes:
   print(course_outcome.text)


