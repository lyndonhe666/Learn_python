import requests
import json
from pyplotz.pyplotz import PyplotZ
from pyplotz.pyplotz import plt


def query_cp(stock_code, start_date, end_date):
    """
    Use to query the closing price for a stock in the designated period and store in a csv file
    
    Args:
        stock_code: code for stock. e.g. cn_600009
        start_date: str, 20180716
        end_date: str, 20180720
    """
    pltz = PyplotZ()
    pltz.enable_chinese()

    payload = {
        'code':stock_code,
        'start':start_date,
        'end':end_date,
        'stat':1,
        'order':'D',
        'period':'d'
    }
    base = 'http://q.stock.sohu.com/hisHq?'
    response = requests.get(base, params=payload)
    response.encoding='gbk'
    res = response.json()
    days = [day[0] for day in res[0]['hq']]
    close_prices = [day[2] for day in res[0]['hq']]
    plt.plot(range(len(days)), list(map(float, close_prices)))
    plt.title(f'股票{stock_code}走势')
    plt.ylabel('收盘价')

