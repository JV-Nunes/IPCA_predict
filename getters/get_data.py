import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname('__file__'), '../../')))
from distutils import extension
from email import header
import encodings
from fileinput import filename
from pkgutil import iter_modules
from turtle import heading
import requests
from . import urls_dict as u
import zipfile
from bs4 import BeautifulSoup
import unicodedata

#Made by João Victor Nunes

class GetIPCA:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def download_page_content(self, file_name, extension):
        '''Executa o download de um arquivo a partir de uma página da internet'''
        #Getting url and headers from external dict
        base_url = self.url
        print('Scraping url:', base_url)

        #Testing request object
        test_page = requests.get(base_url, headers=headers)

        if test_page.status_code == 200:
            print('Approved access')
        else:
            print('Access Denied. Check headers...')

        #Download content from webpage
        page = requests.get(base_url, headers=headers)

        #Saving zip file
        with open(f'Data/zip/{file_name}.{extension}', 'wb') as file:
            file.write(page.content)

        print('Downloaded file:', f'Data/zip/{file_name}.{extension}')

    def exctract_zip_file(self, file_name, extracted_extension):
        '''Extrai um arquivo .zip'''
        with zipfile.ZipFile(f'Data/zip/{file_name}.zip', 'r') as zip_ref:
            zip_ref.extractall(f'Data/extracted/{file_name}.{extracted_extension}')

        print('Extracted File:', f'Data/extracted/{file_name}.{extracted_extension}')

    def run(self, download_file_name, download_extension, extracted_extension):
        '''Executa os métodos de download e extração do arquivo zipado'''
        self.download_page_content(download_file_name, download_extension)
        self.exctract_zip_file(download_file_name, extracted_extension)

class GetExpectedInflation:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def download_page_content(self):
        '''Armazena dados de uma tabela HTML a partir de uma página da internet'''
        #Getting url and headers from external dict
        base_url = self.url
        print('Scraping url:', base_url)

        #Testing request object
        test_page = requests.get(base_url, headers=self.headers)

        if test_page.status_code == 200:
            print('Approved access')
        else:
            print('Access Denied. Check headers...')

        #Download content from webpage
        page = requests.get(base_url, headers=self.headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find_all('table', attrs={'id':'grd_DXMainTable'})

        data = []
        headings = []
        for item in table[:10]:
            if 'Inflação' in item.getText():
                unicode = item.getText()
                #print(str(unicode).split('\n')[8][:-1])
                headings.append(str(unicode).split('\n')[8][:-1])

            #print(item.getText())
            #print(type(item.getText()))
            data.append(item.getText().split('\n'))
        
        return headings, data

    def clean_data(self, headings, data):
        
        ano = []
        mes = []
        valor = []
        for item in data[0][11:]:
            if item != '':
                ano.append(item[:4])
                mes.append(item[5:7])
                valor.append(item[7:])
        
        return headings, ano, mes, valor

    def run(self):
        headings, data = self.download_page_content()
        headings, ano, mes, valor = self.clean_data(headings, data)

        return headings, ano, mes, valor 


if __name__=='__main__':

    url = u.urls.get('Inflação Esperada')
    headers = u.headers
    get_ipca = GetExpectedInflation(url, headers)

    get_ipca.run()