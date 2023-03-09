# import pandas_datareader as web
# start_date='2021-11-01'
# end_date = '2021-12-01'
# data = web.data.Data.DataReader('000001.sz','yahoo',start_date,end_date)
# data.head()

# import tushare as ts
# data = ts.get_hist_data('000001',start='2021-11-01',end='2021-12-01')
# data.head()
# data = get_price('000001.XSHE',start='2021-11-01',end='2021-12-01')
# data.head()
# symbol = 'ltx_usdt'
# 'https'

from urllib.request import urlopen
import json
import  pandas as pd
pd.set_option('expand_frame_repr', False)
#抓取交易对的symbol
symbol = 'ltc_usdt'
url = 'https://www.okex.com/api/v1/ticker.do?symbol=' + symbol
print('dddd')
print(url)
exit()
# url = 'https://www.okex.com/api/v1/ticker.do?symbol=%s' % symbol
# #抓取数据
# content = urlopen(url,timeout=15).read()
# #将数据转化为dataframe
# json_data = json.loads(content.decode("utf-8"))
# df = pd.DataFrame(json_data,dtype='float')
# #对df进行处理
# df = df[['ticker']].T
# print(df)
