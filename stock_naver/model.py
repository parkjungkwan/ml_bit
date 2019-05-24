import pandas as pd

class StockModel:
    def __init__(self, item):
        self.item = item
        self.code = ''

    def model(self):
        code_df = pd.read_html("http://kind.krx.co.kr/disclosureSimpleSearch.do", header="0")[0]
        code_df.종목코드 = code_df.종목코드.map('{:06d}'.format) #종목코드 6자리
        self.code = '00593'
        code_df = code_df.rename(columns={'회사명: ': 'name', '종목코드': 'code'})
        print(code_df.head())

    def get_url(self, item_name, code_df):
        code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False)
        url = "https://finance.naver.com/item/sise_day.nhn?code={code}".format(code=self.code)

        print("요청 url = {}".format(url))
        return url