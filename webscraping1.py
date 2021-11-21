
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
url="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
r= requests.get(url)
htmlcontent=r.content
#print(htmlcontent)
soup=BeautifulSoup(htmlcontent)
#print(soup.prettify)
results=soup.find('h1')
print(results)