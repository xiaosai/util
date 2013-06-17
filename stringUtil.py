#coding:utf-8

'''
# 查找子串第n次出现时的索引

author: zhangsaiyong
created: 2013-05-27
'''
def findSubStr(str, substr, n) :
    result = 0
    subLen = len(substr)
    if n <= 0 :
        return -1
    while n > 0:
        index = str.find(substr)
        if index == -1:
            return -1
        else:
            str = str[index + subLen :]
            n -= 1
            result = result + index + subLen
    return result - subLen