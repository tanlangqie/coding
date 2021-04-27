# -*- coding: utf-8 -*-#

# Name:   roc_threshold.py
# Author: tangzhuang
# Date:   2021/4/24
# desc: 根据模型的roc曲线来调整模型分类阈值
# 参考 https://www.bilibili.com/video/BV1nk4y117se?from=search&seid=15555758036498078196


from sklearn.metrics import  roc_curve

import matplotlib.pyplot as plt


from sklearn import metrics
import numpy as np
import sklearn

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



from sklearn.metrics import confusion_matrix





#真实标签
tre = [1,0,0,1,1]

#预测的概率
pre_p = [0.46,0.3,0.7,0.9,0.8]

#预测的标签
pre = [0,0,0,1,1]


print('*****输出混淆矩阵和recall****')
auc = cal(tre, pre, pre_p)
print()

print('*****输出最优分类阈值****************')
fpr,tpr,thresholds = roc_curve(tre,pre_p)
J = tpr - fpr
ids = np.argmax(J)
best_threshold = thresholds[ids]
print('fpr:{}'.format(fpr))
print('tpr:{}'.format(tpr))
print('thresholds:{}'.format(thresholds))
print('best_threshold:{}'.format(best_threshold))
print()



print('*******绘制roc曲线*******')
plt.plot(fpr, tpr, 'k--', label='ROC (area = {0:.2f})'.format(auc), lw=2)

plt.xlim([-0.05, 1.05])  # 设置x、y轴的上下限，以免和边缘重合，更好的观察图像的整体
plt.ylim([-0.05, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')  # 可以使用中文，但需要导入一些库即字体
plt.title('ROC Curve')
plt.legend(loc="lower right")
plt.show()
