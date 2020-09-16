import sys
import os
import re
from itertools import chain
import jieba
import profile

def readtxt(filename):  # 将文件读取并分行保存
    orig = []
    with open(filename,'r',encoding="UTF-8") as f:
        orig = [line.strip() for line in f.readlines() if line.strip() != '']
    f.close()

    reg=r'[《》‘’“”：！？……、，。\s]'
    managed_txt = [re.split(reg,line) for line in orig]
    
    jieba_txt = []
    for item_1 in managed_txt:
        for item_2 in item_1:
            jieba_txt.append(jieba.lcut(item_2))

    fin_txt = list(chain(*jieba_txt))

    return fin_txt


def compare(lines1,lines2):  # 比对文件

    count = 0
    for line in lines1:
        if lines2.count(line) > 0:
            count +=1
    return count / max(len(lines1),len(lines2))


def write_ans(degree,ans_path):  # 讲答案输出到指定文件
    ans = str('相似度为%.2f%%' % degree)
    ans_file = open(ans_path,'w',encoding='UTF-8')
    ans_file.write(ans)
    ans_file.close()   


orig_file = sys.argv[1]
test_file = sys.argv[2]

orig_txt = readtxt(orig_file)
test_txt = readtxt(test_file)

degree = compare(orig_txt,test_txt)
write_ans(degree,sys.argv[3])

profile.run('readtxt')
profile.run('compare')
profile.run('write_ans')
#print('相似度为%.2f' % degree)'
