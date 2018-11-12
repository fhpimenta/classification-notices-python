from bs4 import BeautifulSoup
from urllib import request
import pandas as pd

dataset = pd.read_csv('urls.csv')
categorias = dataset['category'].values
urls = dataset['url'].values
textos = []

for url,categoria in zip(urls,categorias):
    page = request.urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')

    classname = 'story-body__inner'
    if categoria == 'sport':
        classname = 'story-body'

    div = soup.find('div', class_=classname)
    texto = ''
    for paragraph in div.find_all('p'):
        texto += paragraph.text

    textos.append(texto)
    print(categoria)


test_dataset = pd.DataFrame({'category': categorias, 'text': textos})
test_dataset.to_csv('test.csv',encoding='utf-8')