from stock_naver.controller import StockController
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet
import plotly.offline as offline
import plotly.graph_objs as go


if __name__ == '__main__':
    model = StockController('삼성전자')
    url = model.model()
    driver = webdriver.Chrome('chromedriver')
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())

    df = pd.DataFrame()

    for page in range(1, 10):
        page_url = '{url}&page={page}'.format(url=url, page=page)
        df = df.append(pd.read_html(page_url, header=0)[0], ignore_index=True)
    df = df.dropna() # 결측값 제거
    #print(df.head())

    df = df.rename(columns = {'날짜': 'date', '종가' : 'close', '전일비' : 'diff',
                              '시가' : 'open', '고가' : 'high', '저가': 'low', '거래량' : 'volume'})
    #원핫인코딩
    df[['close','diff','open','high','low','volume']] = \
        df[['close','diff','open','high','low','volume']].astype(int)
    df['date'] = pd.to_datetime(df['date'])

    df = df.sort_values(by=['date'], ascending=True)
    print(df.head())






