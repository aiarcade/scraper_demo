from PyPDF2 import PdfFileReader
from bs4 import BeautifulSoup as bs4

import requests

header={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36' ,'Connection':'close'}

def download_pdf(url,out_name):
   
    r = requests.get(url, stream=True,headers=header)

    with open(out_name, 'wb') as fd:
        for chunk in r.iter_content(2000):
            fd.write(chunk)

def get_items(url):
    base_url="https://dhs.kerala.gov.in/"
    page = requests.get(url,headers=header)
    text= page.text
    
    soup = bs4(text, 'lxml')
    items=soup.findAll('div', attrs = {'id': "pl-8208"} )
    links=[]
    for item in items[0].findAll('a'):
        links.append([item.text,base_url+item['href']])
    return  links

def get_doc_link(url):
    base_url="https://dhs.kerala.gov.in/"
    page = requests.get(url,headers=header)
    text= page.text
    
    soup = bs4(text, 'lxml')
    items=soup.findAll('div', attrs = {'class': "entry-content"} )
    link=items[0].findAll('a')[0]
    return base_url+link['href']

def data_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)

        # get the first page
        page = pdf.getPage(1)
        #print(page)
        #print('Page type: {}'.format(str(type(page))))

        text = page.extractText()
        
        i=text.find('Results')
        para=text[i:i+500].replace("\n","")
        #print(para)
        nums=[int(s) for s in para.split() if s.isdigit()]
        return nums[0]