import requests
import unicodedata
from bs4 import BeautifulSoup
import csv

response = requests.get("https://bulletin.temple.edu/undergraduate/science-technology/computer-information-science/data-science-computational-analytics-bs/#requirementstext")
soup = BeautifulSoup(response.text, "html.parser")
lst = []
for title in soup.find_all("tr"):
    lst.append((title.get_text()))

for string in lst:
    string = unicodedata.normalize(NFKD,)