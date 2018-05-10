from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.storychina.cn")
bs_obj = BeautifulSoup(html.read(),'html.parser')
text_list = bs_obj.find_all("ul","nav fixed fl")
for index,text in enumerate(text_list):
    print(index,text.get_text())
html.close()