# -*- coding: utf-8 -*-#

# Name:   data_pro.py
# Author: tangzhuang
# Date:   2021/5/15
# desc:         

import  pandas as pd


daily_data = pd.read_excel('daily_data.xlsx')
daily_data['flo'] = daily_data['flo'].map(float)
daily_data['flo'] = daily_data['flo']/100
print(daily_data.head())


quarter_data = pd.read_excel('res.xlsx')
quarter_data['EndDate'] = quarter_data['EndDate'].map(str)


def transformdata(x):
    x = str(x)
    if x > '2016-06-30 00:00:00' and x <= '2016-09-30 00:00:00':
        return '2016-06-30 00:00:00'
    elif x > '2016-09-30 00:00:00' and x <= '2016-12-31 00:00:00':
        return '2016-09-30 00:00:00'
    elif x > '2016-12-31 00:00:00' and x <= '2017-03-31 00:00:00':
        return '2016-12-31 00:00:00'
    elif x > '2017-03-31 00:00:00' and x <= '2017-06-30 00:00:00':
        return '2017-03-31 00:00:00'

    elif x > '2017-06-30 00:00:00' and x <= '2017-09-30 00:00:00':
        return '2017-06-30 00:00:00'
    elif x > '2017-09-30 00:00:00' and x <= '2017-12-31 00:00:00':
        return '2017-09-30 00:00:00'
    elif x > '2017-12-31 00:00:00' and x <= '2018-03-31 00:00:00':
        return '2017-12-31 00:00:00'
    elif x > '2018-03-31 00:00:00' and x <= '2018-06-30 00:00:00':
        return '2018-03-31 00:00:00'


    elif x > '2018-06-30 00:00:00' and x <= '2018-09-30 00:00:00':
        return '2018-06-30 00:00:00'
    elif x > '2018-09-30 00:00:00' and x <= '2018-12-31 00:00:00':
        return '2018-09-30 00:00:00'
    elif x > '2018-12-31 00:00:00' and x <= '2019-03-31 00:00:00':
        return '2018-12-31 00:00:00'
    elif x > '2019-03-31 00:00:00' and x <= '2019-06-30 00:00:00':
        return '2019-03-31 00:00:00'


    elif x > '2019-06-30 00:00:00' and x <= '2019-09-30 00:00:00':
        return '2019-06-30 00:00:00'
    elif x > '2019-09-30 00:00:00' and x <= '2019-12-31 00:00:00':
        return '2019-09-30 00:00:00'
    elif x > '2019-12-31 00:00:00' and x <= '2020-03-31 00:00:00':
        return '2019-12-31 00:00:00'
    elif x > '2020-03-31 00:00:00' and x <= '2020-06-30 00:00:00':
        return '2020-03-31 00:00:00'


    elif x > '2020-06-30 00:00:00' and x <= '2020-09-30 00:00:00':
        return '2020-06-30 00:00:00'
    elif x > '2020-09-30 00:00:00' and x <= '2020-12-31 00:00:00':
        return '2020-09-30 00:00:00'
    elif x > '2020-12-31 00:00:00' and x <= '2021-03-31 00:00:00':
        return '2020-12-31 00:00:00'
    else:
        return '2021-03-31 00:00:00'
    # if x >= '2016-06-30 00:00:00' and x < '2016-09-30 00:00:00':
    #     return '2016-06-30 00:00:00'
    # elif x >= '2016-09-30 00:00:00' and x < '2016-12-31 00:00:00':
    #     return '2016-09-30 00:00:00'
    # elif x >= '2016-12-31 00:00:00' and x < '2017-03-31 00:00:00':
    #     return '2016-12-31 00:00:00'
    # elif x >= '2017-03-31 00:00:00' and x < '2017-06-30 00:00:00':
    #     return '2017-03-31 00:00:00'
    #
    # elif x >= '2017-06-30 00:00:00' and x < '2017-09-30 00:00:00':
    #     return '2017-06-30 00:00:00'
    # elif x >= '2017-09-30 00:00:00' and x < '2017-12-31 00:00:00':
    #     return '2017-09-30 00:00:00'
    # elif x >= '2017-12-31 00:00:00' and x < '2018-03-31 00:00:00':
    #     return '2017-12-31 00:00:00'
    # elif x >= '2018-03-31 00:00:00' and x < '2018-06-30 00:00:00':
    #     return '2018-03-31 00:00:00'
    #
    #
    # elif x >= '2018-06-30 00:00:00' and x < '2018-09-30 00:00:00':
    #     return '2018-06-30 00:00:00'
    # elif x >= '2018-09-30 00:00:00' and x < '2018-12-31 00:00:00':
    #     return '2018-09-30 00:00:00'
    # elif x >= '2018-12-31 00:00:00' and x < '2019-03-31 00:00:00':
    #     return '2018-12-31 00:00:00'
    # elif x >= '2019-03-31 00:00:00' and x < '2019-06-30 00:00:00':
    #     return '2019-03-31 00:00:00'
    #
    #
    # elif x >= '2019-06-30 00:00:00' and x < '2019-09-30 00:00:00':
    #     return '2019-06-30 00:00:00'
    # elif x >= '2019-09-30 00:00:00' and x < '2019-12-31 00:00:00':
    #     return '2019-09-30 00:00:00'
    # elif x >= '2019-12-31 00:00:00' and x < '2020-03-31 00:00:00':
    #     return '2019-12-31 00:00:00'
    # elif x >= '2020-03-31 00:00:00' and x < '2020-06-30 00:00:00':
    #     return '2020-03-31 00:00:00'
    #
    #
    # elif x >= '2020-06-30 00:00:00' and x < '2020-09-30 00:00:00':
    #     return '2020-06-30 00:00:00'
    # elif x >= '2020-09-30 00:00:00' and x < '2020-12-31 00:00:00':
    #     return '2020-09-30 00:00:00'
    # elif x >= '2020-12-31 00:00:00' and x < '2021-03-31 00:00:00':
    #     return '2020-12-31 00:00:00'
    # else:
    #     return '2021-03-31 00:00:00'

daily_data['EndDate'] = daily_data['TradingDay'].apply(lambda x:transformdata(x))

print(daily_data.head())

data = pd.merge(daily_data,quarter_data[['EndDate','InnerCode','weight']],on=['EndDate','InnerCode'],how='inner')
print('data...')
print(data.head())
data['increase'] = data['flo'] * data['weight']


res = data.groupby(['TradingDay'],as_index=False)['increase'].sum()


daily_value = [1578.07911304649]
base = daily_value[-1]
# res['daily_value'] = base * res[['increase']]
day_list = ['2016-06-30 00:00:00', '2016-09-30 00:00:00','2016-12-31 00:00:00','2017-03-31 00:00:00',
            '2017-06-30 00:00:00', '2017-09-30 00:00:00','2017-12-31 00:00:00','2018-03-31 00:00:00',
            '2018-06-30 00:00:00', '2018-09-30 00:00:00', '2018-12-31 00:00:00', '2019-03-31 00:00:00',
            '2019-06-30 00:00:00', '2019-09-30 00:00:00', '2019-12-31 00:00:00', '2020-03-31 00:00:00',
            '2020-06-30 00:00:00', '2020-09-30 00:00:00', '2020-12-31 00:00:00', '2021-03-31 00:00:00'
            ]
for i in range(len(res)):
    if str(res.iloc[i,0]) in day_list:
        daily_value.append(base * (1+res.iloc[i,1]))
        base = daily_value[-1]
    else:
        daily_value.append(base * (1+res.iloc[i, 1]))

res['daily_value'] = daily_value[1:]




data['increase']  = data['increase'] .apply(lambda x: str(x * 100) + '%')
data['weight']  = data['weight'] .apply(lambda x: str(x * 100) + '%')
data['flo']  = data['flo'] .apply(lambda x: str(x * 100) + '%')
data.to_excel('data.xlsx',index=False)


print('res...')
print(res.head())
res.to_excel('res_1.xlsx',index=False)