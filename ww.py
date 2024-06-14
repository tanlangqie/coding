# -*- coding: utf-8 -*-#

# Name:   ww.py
# Author: tangzhuang
# Date:   2021/7/13
# desc:         

# import pandas as pd
# import sklearn as sklearn
# from sklearn.feature_extraction import DictVectorizer
# from sklearn import tree
# import pydotplus
# from sklearn.externals.six import StringIO
# # pandas 读取 csv 文件，header = None 表示不将首行作为列
# data = pd.read_csv('data/test.csv', header=None)
# # 指定列
# data.columns = ['Diet Habits', 'viviparous animal', 'Aquatic animals', 'Can fly','mammal']
#
# # sparse=False意思是不产生稀疏矩阵
# vec = sklearn.feature_extraction.DictVectorizer(sparse=False)
# # 先用 pandas 对每行生成字典，然后进行向量化
# feature = data[['Diet Habits', 'viviparous animal', 'Aquatic animals']]
#
# X_train = vec.fit_transform(feature.to_dict(orient='record'))
# # 打印各个变量
# print('show feature\n', feature)
# print('show vector\n', X_train)
# print('show vector name\n', vec.get_feature_names())
# print('show vector name\n', vec.vocabulary_)
# Y_train = data['mammal']
# clf = tree.DecisionTreeClassifier(criterion='entropy')

ss = [1,2,3]
print(ss[:1])


from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

llm = OpenAI(model_name="text-davinci-003")

# 告诉他我们生成的内容需要哪些字段，每个字段类型式啥
response_schemas = [
    ResponseSchema(name="bad_string", description="This a poorly formatted user input string"),
    ResponseSchema(name="good_string", description="This is your response, a reformatted response")
]

# 初始化解析器
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

# 生成的格式提示符
# {
#	"bad_string": string  // This a poorly formatted user input string
#	"good_string": string  // This is your response, a reformatted response
#}
format_instructions = output_parser.get_format_instructions()

template = """
You will be given a poorly formatted string from a user.
Reformat it and make sure all the words are spelled correctly

{format_instructions}

% USER INPUT:
{user_input}

YOUR RESPONSE:
"""

# 将我们的格式描述嵌入到 prompt 中去，告诉 llm 我们需要他输出什么样格式的内容
prompt = PromptTemplate(
    input_variables=["user_input"],
    partial_variables={"format_instructions": format_instructions},
    template=template
)

promptValue = prompt.format(user_input="welcom to califonya!")
llm_output = llm(promptValue)

# 使用解析器进行解析生成的内容
output_parser.parse(llm_output)