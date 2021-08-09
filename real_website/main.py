from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.careerjet.com.bd/search/jobs?s=python&l=Bangladesh')

print(html_text)
