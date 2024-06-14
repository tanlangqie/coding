# # # -*- coding: utf-8 -*-#
# #
# # # Name:   tem2.py
# # # Author: tangzhuang
# # # Date:   2021/7/11
# # # desc:
# #
# # # -*- coding: utf-8 -*-#
# #
# # # Name:   tem1.py
# # # Author: tangzhuang
# # # Date:   2021/7/11
# # # desc:
# #
# import sys
#
# for line in sys.stdin:
#     n = map(int, line.split())
#     arr = map(int, line.split())
#
#     arr = sorted(arr)
#     size = len(arr)
#     for i in range(size - 2):
#         for j in range(i + 1, size - 1):
#             for k in range(j + 1, size):
#                 if arr[k] == arr[i] + 2 * arr[j]:
#                     print(arr[k], arr[i], arr[j])
#                 if arr[k] == arr[j] + 2 * arr[i]:
#                     print(arr[k], arr[j], arr[i])
#     print(0)
# arr = [2,7,3,0]
# arr = sorted(arr)
# size = len(arr)
# for i in range(size - 2):
#     for j in range(i+1, size - 1):
#         for k in range(j+1, size):
#             if arr[k] == arr[i] + 2 * arr[j]:
#                 print(arr[k], arr[i], arr[j])
#             if arr[k] == arr[j] + 2 * arr[i]:
#                 print(arr[k], arr[j], arr[i])
# print(0)


import sys

# for line in sys.stdin:
# n = sys.stdin.readline().strip()
# arr = map(int, sys.stdin.readline().strip().split())
# arr = [2, 7, 3, 0]
# arr = [7,7,0]
# arr = sorted(arr)
# size = len(arr)
# flag = 0
# for i in range(size - 2):
#     for j in range(i + 1, size - 1):
#         for k in range(j + 1, size):
#             # print(arr[i],arr[j],arr[k])
#             if arr[k] == arr[i] + 2 * arr[j]:
#                 print(arr[k], arr[i], arr[j])
#                 flag = 1
#
#             if arr[k] == arr[j] + 2 * arr[i]:
#                 print(arr[k], arr[j], arr[i])
#                 flag = 1
# if flag==0:
#     print(0)

import numpy as np

corpus_raw = 'He is the king . The king is royal . She is the royal  queen '

# 大小写转换
corpus_raw = corpus_raw.lower()
words = []
for word in corpus_raw.split():
    if word != '.':
        words.append(word)


# 创建一个字典，将单词转换为整数，并将整数转换为单词。
words = set(words)
word2int = {}
int2word = {}
vocab_size = len(words)
for i, word in enumerate(words):
    word2int[word] = i
    int2word[i] = word

raw_sentences = corpus_raw.split('.')
sentences = []
for sentence in raw_sentences:
    sentences.append(sentence.split())

# 构造训练数据

WINDOW_SIZE = 2
data = []
for sentence in sentences:
    for word_index, word in enumerate(sentence):
        for nb_word in sentence[max(word_index - WINDOW_SIZE, 0): min(word_index + WINDOW_SIZE, len(sentence)) + 1]:
            if nb_word != word:
                data.append([word, nb_word])


# one-hot编码
def to_one_hot(data_point_index, vocab_size):
    """
    对单词进行one-hot representation
    :param data_point_index: 单词在词汇表的位置索引
    :param vocab_size: 词汇表大小
    :return: 1 x vocab_size 的one-hot representatio
    """
    temp = np.zeros(vocab_size)
    temp[data_point_index] = 1
    return temp


# 输入单词和输出单词
x_train = []
y_train = []

for data_word in data:
    x_train.append(to_one_hot(word2int[data_word[0]], vocab_size))
    y_train.append(to_one_hot(word2int[data_word[1]], vocab_size))
a = 3
