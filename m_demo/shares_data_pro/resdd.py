# -*- coding: utf-8 -*-#

# Name:   resdd.py
# Author: tangzhuang
# Date:   2021/5/15
# desc:
import pandas as pd


data = pd.read_excel('data.xlsx')
t = data[data.EndDate=='2016-06-30 00:00:00']
print(len(set(t['InnerCode'])))

t = data[data.EndDate=='2016-09-30 00:00:00']
print(len(set(t['InnerCode'])))