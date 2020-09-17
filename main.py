import os, re, sys
from itertools import chain
import jieba, numpy, cProfile


class BlankTxtError(Exception):
    def __init__(self):
        print("文本为空")
        ans_file = open(sys.argv[3], 'w', encoding='UTF-8')
        ans_file.write("相似度为0.00%%")
        ans_file.close()


def readtxt(filename):
    #逐行读取文件，并根据标点符号进行分段，最后用jieba对文本进行分词处理

    orig = []
    with open(filename, 'r', encoding="UTF-8") as f:
        orig = [line.strip() for line in f.readlines() if line.strip() != '']
    f.close()

    reg = r'[《》‘’“”：！？……、，。\s]'
    managed_txt = [re.split(reg, line) for line in orig]

    jieba_txt = []
    for item_1 in managed_txt:
        for item_2 in item_1:
            jieba_txt.append(jieba.lcut(item_2))

    fin_txt = list(chain(*jieba_txt))

    return fin_txt


def compare(orig_txt, test_txt):
    #采用余弦相似度算法计算两个文本的相似程度

    f1 = []
    f2 = []
    merge_txt = list(set(orig_txt + test_txt))
    for i in merge_txt:
        count1 = 0
        count2 = 0
        for j in orig_txt:
            if i == j:
                count1 += 1
        f1.append(count1)
        for k in test_txt:
            if i == k:
                count2 += 1
        f2.append(count2)
    return (numpy.dot(f1, f2) / (numpy.linalg.norm(f2, ord=2) * numpy.linalg.norm(f1, ord=2)))


def write_ans(degree, ans_path):
    #将文本的相似度格式化并输出到指定文件

    ans = str('相似度为%.2f%%' % degree)
    ans_file = open(ans_path, 'w', encoding='UTF-8')
    ans_file.write(ans)
    ans_file.close()


if __name__ == '__main__':
    orig_file = sys.argv[1]
    test_file = sys.argv[2]

    orig_txt = readtxt(orig_file)
    test_txt = readtxt(test_file)
    if len(test_txt) == 0 or len(orig_txt) == 0:
        raise BlankTxtError
    else:
        degree = compare(orig_txt, test_txt)
        write_ans(degree, sys.argv[3])


    cProfile.run('readtxt(orig_file)')
    cProfile.run('readtxt(test_file)')
    cProfile.run('compare(orig_txt, test_txt)')
    cProfile.run('write_ans(degree, sys.argv[3])')

