# AUTOGENERATED! DO NOT EDIT! File to edit: 00_digdata.ipynb (unless otherwise specified).

__all__ = ['#url', 'url', 'headers', 'session', 'r', 'soup', 'getdata', 'overall_information', 'province_information',
           'area_information', 'news']

# Cell
from bs4 import BeautifulSoup
from parser import * #regex_parser
import re
import json
import time
import logging
import datetime
import requests
import pprint

# Cell
#url = "https://3g.dxy.cn/newh5/view/pneumonia"
url = "https://ncov.dxy.cn/ncovh5/view/pneumonia?from=singlemessage&isappinstalled=0"
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
}

# Cell
session = requests.session()
session.headers.update(headers)

# Cell
r = session.get(url)

# Cell
#pprint.pprint(r.text)

# Cell
soup = BeautifulSoup(r.content, 'lxml')

# Cell
def getdata():
    return 2

# Cell
overall_information = re.search(r'\{("id".*?)\}', str(soup.find('script', attrs={'id': 'getStatisticsService'})))
province_information = re.search(r'\[(.*?)\]', str(soup.find('script', attrs={'id': 'getListByCountryTypeService1'})))
area_information = re.search(r'\[(.*)\]', str(soup.find('script', attrs={'id': 'getAreaStat'})))
news = re.search(r'\[(.*?)\]', str(soup.find('script', attrs={'id': 'getTimelineService'})))