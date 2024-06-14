#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/18 7:04 下午
# @Author  : tangzhuang
# @File    : isolationforset.py 
# @title   : 
from sklearn.ensemble import IsolationForest
import  numpy as np

mod = IsolationForest ()
X = np.array([[1,1],[1,2],[2,1],[0,1],[8,4],[0,0],[-1,-1]])
mod.fit(X)
res=mod.predict(X)
print(res)