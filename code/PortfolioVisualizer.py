
import requests

from bs4 import BeautifulSoup

import re

import pandas as pd

fund1 = "MUB"
fund2 = "VTEB"
bench = "VWITX"
sdate = "1%2F1%2F2015"
edate = "1%2F31%2F2020"
url   = 'https://www.portfoliovisualizer.com/fund-performance?s=y&symbol=' + fund1 + \
      '&symbols=' + fund2 + '&benchmark=' + bench + '&startDate=' + sdate + '&endDate=' + edate

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

response = requests.get(url, headers = headers)

soup = BeautifulSoup(response.text, 'lxml')

# list of all 13 charts in string format 
charts_text = [chart.text for chart in soup.find_all('script')[3:16]]

# charts_dataframe[i] is the dataframe format of chart i
charts_dataframe = []

for chart_number, chart_text in enumerate(charts_text):
  chart_data = []

  if 'arrayToDataTable' in chart_text:
    for row in re.findall(r'\[(.*?)\]', re.findall(r"arrayToDataTable\(\[(.*?)\]\);", chart_text)[0]):
      chart_data.append([string.strip("'") for string in row.split(', ')])
    charts_dataframe.append(pd.DataFrame(chart_data[1:], columns = chart_data[0]).apply(pd.to_numeric, errors = 'ignore'))

  elif 'addRows' in chart_text:
    chart_data.append([column[1] for column in re.findall("addColumn\('(.*?)','(.*?)'\);", chart_text)])
    for row in re.findall("new Date(.*?)]", chart_text):
      chart_data.append(row.split(', '))
    charts_dataframe.append(pd.DataFrame(chart_data[1:], columns = chart_data[0]).apply(pd.to_numeric, errors = 'ignore'))

  else:
    print('Error at Chart {}!'.format(chart_number))
    charts_dataframe.append(None)

for dataframe in charts_dataframe:
  print(dataframe.head(n = 2), "\n")
