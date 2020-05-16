import pathlib
import codecs
import string
PATH = pathlib.Path(__file__).parent
from bs4 import BeautifulSoup 
import os
os.chdir(PATH)

with codecs.open(r"section5.html" , "r") as f:
    soup = BeautifulSoup(f.read(), "lxml")
sections = [i.text.strip(" :\n").strip() for i in soup.find_all("label")]
print(sections)
