# -*- coding: utf-8 -*-#

# Name:   tem.py
# Author: tangzhuang
# Date:   2021/7/7
# desc:   给出混淆矩阵，算出各项指标

from sklearn.metrics import  roc_curve

import matplotlib.pyplot as plt


from sklearn import metrics
import numpy as np
import sklearn

# 计算各项指标
# def cal( ):
#     from sklearn import metrics
#     confusionMatrix =np.array([[526,74],[4,16]])  # 混淆矩阵
#
#     xsum = np.sum(confusionMatrix, axis=1)  # 从左往右求和
#     xsum = np.array(xsum)
#     ysum = np.sum(confusionMatrix, axis=0)  # 从上往下求和
#     ysum = np.array(ysum)
#     # print(xsum)                                   # 举证右求和
#     # print(ysum)
#     recall = []
#     precision = []
#     f1_measure = []
#     for i in range(len(xsum)):
#         reca = (confusionMatrix[i][i] / xsum[i])
#         recall.append(reca)
#
#         prec = (confusionMatrix[i][i] / ysum[i])
#         precision.append(prec)
#
#         f1 = 2 * recall[i] * precision[i] / (recall[i] + precision[i])
#         f1_measure.append(f1)
#     print(confusionMatrix)  # 混淆矩阵
#     print('recall: ' + str(recall))  # 召回率
#     print("precisoin: " + str(precision))  # 准确率
#     print("f1_measure: " + str(f1_measure))  # f1measure
#     # print("OA:" + str(metrics.precision_score(tre, pre, average='micro')))  # 微平均，精确率
#     # auc = metrics.roc_auc_score(tre, y_p)
#     # print("AUC: " + str(auc))  # auc
#     return



# 计算各项指标
def cal(tre, pre, y_p):
    from sklearn import metrics
    confusionMatrix = sklearn.metrics.confusion_matrix(tre, pre)  # 混淆矩阵

    xsum = np.sum(confusionMatrix, axis=1)  # 从左往右求和
    xsum = np.array(xsum)
    ysum = np.sum(confusionMatrix, axis=0)  # 从上往下求和
    ysum = np.array(ysum)
    # print(xsum)                                   # 举证右求和
    # print(ysum)
    recall = []
    precision = []
    f1_measure = []
    for i in range(len(xsum)):
        reca = (confusionMatrix[i][i] / xsum[i])
        recall.append(reca)

        prec = (confusionMatrix[i][i] / ysum[i])
        precision.append(prec)

        f1 = 2 * recall[i] * precision[i] / (recall[i] + precision[i])
        f1_measure.append(f1)
    print(confusionMatrix)  # 混淆矩阵
    print('recall: ' + str(recall))  # 召回率
    print("precisoin: " + str(precision))  # 准确率
    print("f1_measure: " + str(f1_measure))  # f1measure
    print("OA:" + str(metrics.precision_score(tre, pre, average='micro')))  # 微平均，精确率
    auc = metrics.roc_auc_score(tre, y_p)
    print("AUC: " + str(auc))  # auc
    return auc



tre = [1]*20 + [0]*600
pre = []
# cal( )
import random
# print(random.uniform(0.5001,1))
pre_p = []
for i in range(20):
    pre_p.append(random.uniform(0.5001,1))
    pre.append(1)
for i in range(600):
    pre_p.append(random.uniform(0,0.499999))
    pre.append(0)
print(len(pre_p))
print(pre_p[:50])

for i in range(4):
    pre_p[i] -= 0.5
    pre[i] = 0
for i in range(620-74,620):
    pre_p[i] += 0.5
    pre[i] = 1


print('*****输出混淆矩阵和recall****')
auc = cal(tre, pre, pre_p)
print()
print('-------------------')
print(pre[:30])
print(tre[:30])