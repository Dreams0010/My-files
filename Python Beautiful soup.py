from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd
import numpy as np
import open

Myurl = "https://fbil.org.in/download?op=gsec&mq=o"

# opening up my connection , Grabbing the page
uclient = uReq(Myurl)
page_HTML = uclient.read()

uclient.close()

#HTML parser
page_soup = soup(page_HTML,"html.parser")
