from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from fbprophet import Prophet

if __name__ == '__main__':
    driver = webdriver.Chrome('chromedriver')
    url = 'https://bitcoincharts.com/charts/korbitKRW#rg730ztgSzm1g10zm2g25zv'
    driver.get(url)
    xpath = """//*[@id="content_chart"]/div/div[2]/a"""
    variable = driver.find_element_by_xpath(xpath)
    driver.execute_script("return arguments[0].scrollIntoView();", variable)
    variable.click()
    # 그 메뉴가 보일 때까지 스크롤해서 내려가서 클릭하라
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())

    table = soup.find('table', 'data')

    print(table)
    print(table)

    # print(str(table))
    df = pd.read_html(str(table))

    """
    df.Capacity = df.Capacity.str.replace(r"\[.*\]", "")
    bitcoin = df[0]
    print(bitcoin.head())
    bitcoin['Close'].plot(figsize=(12,6), grid=True)
    df = pd.DataFrame({'ds': bitcoin['Timestamp'], 'y': bitcoin['Close']})
    print(df)
    prophet = Prophet(yearly_sessionality=True, daily_sessonality=True)
    prophet.fit(df)
    future = prophet.make_future_dataframe(perods=30)
    forecast = prophet.predict(future)
    prophet.plot(forecast)
    """















