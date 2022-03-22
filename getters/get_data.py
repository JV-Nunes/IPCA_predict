
from distutils import extension
from email import header
import encodings
from fileinput import filename
from pkgutil import iter_modules
from turtle import heading
import requests
import urls_dict as u
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
        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find_all('table', attrs={'id':'grd_DXMainTable'})

        table.find_all('tr')

        headings = []
        for item in table:
            if 'Inflação' in item.getText():
                
                unicode = item.getText()
                string = unicodedata.normalize('NFKD', unicode).encode('ascii', 'ignore')
                print(string)
                headings.append(string.strip('\n'))
        
        print(headings)


        # datasets = []
        # for row in table.find_all("tr")[1:]:
        #     dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
        #     datasets.append(dataset)
        # print(dataset)




if __name__=='__main__':

    url = u.urls.get('Inflação Esperada')
    headers = u.headers
    get_ipca = GetExpectedInflation(url, headers)

    get_ipca.download_page_content()
