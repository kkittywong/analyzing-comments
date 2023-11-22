import pandas as pd
import re                           # 正则表达式库
import jieba                        # 结巴分词
import jieba.posseg                 # 词性获取
import collections

#导入数据集 
data = pd.read_csv('/Users/mankiwong/Desktop/Frequency.csv') 
content= ("".join(i for i in data['評論內容'])) 

#预处理
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|\ |"') # 定义正则表达式匹配模式（空格等）
string_data = re.sub(pattern, '', content)     # 将符合模式的字符去除

#文本分词
seg_list_exact = jieba.cut(string_data, cut_all=False, HMM=True)    # 精确模式分词+HMM
object_list = []

#获取停用词
with open('/Users/mankiwong/Desktop/cn_stopwords.txt', encoding='utf-8') as file:
    stopwords = [x.strip() for x in file.readlines()]

#去除停用词（目的是去掉一些意义不大的词）
for word in seg_list_exact:         # 循环读出每个分词
    if word not in stopwords:       # 如果不在去除词库中
        object_list.append(word)    # 分词追加到列表

word_counts = collections.Counter(object_list)       # 对分词做词频统计
word_counts_top = word_counts.most_common(82)    # 获取前82个最高频的词
print(word_counts_top)

import csv
Excel = open("/Users/mankiwong/Desktop/Frequency.csv", 'w', newline = '')   #打开表格文件，若表格文件不存在则创建
write = csv.writer(Excel)    #创建一个csv的writer对象用于写每一行内容
write.writerow(['词语','出现次数'])  #写表格表头
item = list(word_counts.items()) #将字典转化为列表格式
item.sort(key = lambda x: x[1], reverse = True) #对列表按照第二列进行排序
for i in range(82):
    write.writerow(item[i])
