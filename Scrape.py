import requests
import unicodedata
from bs4 import BeautifulSoup
import csv

response = requests.get("https://bulletin.temple.edu/undergraduate/science-technology/computer-information-science/data-science-computational-analytics-bs/#requirementstext")
soup = BeautifulSoup(response.text, "html.parser")
# lst = []
# for title in soup.find_all("tr"):
#     lst.append((title.get_text()))

# lst = [unicodedata.normalize("NFKD",string) for string in lst]
# for item in lst:
#     if "Total" in item:
#         lst = lst[:lst.index(item)]
#         break
    
# print(lst)
# lst = []
# for title in soup.find_all("a"):
#     lst.append(title.get_text())

# lst = [unicodedata.normalize("NFKD",string) for string in lst]

# def 
lst = []
courselist = soup.find(class_="sc_courselist")
title = courselist.find_all("a")
for item in title:
    lst.append(item.get_text())
lst = [unicodedata.normalize("NFKD",string) for string in lst]
print(lst)