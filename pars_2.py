from bs4 import BeautifulSoup
import re

with open("devcasino_scr1_var1.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

sections = soup.find_all("div", class_= re.compile("wlc-sections"))
sections_list = {}

for section in sections:
    section_classes = section.get("class")
    sections_list[section_classes[0]]= section_classes

print(sections_list)

    


