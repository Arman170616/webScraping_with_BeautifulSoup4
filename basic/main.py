from bs4 import BeautifulSoup

with open('basic/home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    courses = soup.find_all(['h1', 'h5', 'h4'])
    for course in courses:
        print(course.text)
