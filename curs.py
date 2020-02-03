import re
import pandas as pd
from urllib.request import urlopen
import datetime
def curs():
    r = r'Долар США.+?\n.+?\n.+?(?P<nbu>\d+?.\d+?)<'
    url1 = 'https://bank.gov.ua/markets/exchangerates/?date='
    url2 = '&period=daily'
    date = datetime.datetime.strptime('2018-01-01', '%Y-%m-%d')
    res = {}
    for i in range(0, 424):
        date += datetime.timedelta(days=1)
        dates = date.strftime('%d.%m.%Y')
        request = urlopen(url1 + dates + url2)
        c = list(re.finditer(r, str(request.read(), encoding='utf-8', errors='ignore')))
        try:
            curs = float('.'.join(c[0].group('nbu').split(',')))
            if curs > 500:
                curs = curs/100
        except Exception:
            curs = 0
        res[date] = curs
    res = pd.DataFrame.from_dict(res, orient='index', columns=['UAH/USD'])
    res.index = res.index.to_period(freq='D')
    res.to_csv('curs.csv')
curs()