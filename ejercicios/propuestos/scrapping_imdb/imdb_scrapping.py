"""
Nombre del programa:
Descripción:
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 9/2/23
"""

# import scrapy
import os
import pandas as pd
from ydata_profiling import ProfileReport


# os.system('scrapy startproject imbd practica')
# os.system('cd practica && scrapy genspider "movies-released-in-2022" '
#          '"www.imdb.com/search/title/?release_date=2022-01-01,2022-12-31&runtime=1,&sort=release_date,'
#          'asc&count=250"')
# os.system('cd practica && scrapy crawl "movies-released-in-2022"')
# os.system('mkdir -p dataset')
os.system('cd practica && scrapy crawl "movies-released-in-2022" -O ../dataset/dataset.json')

df = pd.read_json('dataset/dataset.json')
# print(len(df))
# df.head()

df.to_csv('dataset/dataset.csv')

profile = ProfileReport(df, explorative=True)
# profile

os.system('mkdir -p reports')
profile.to_file('reports/dataset-report.html')
