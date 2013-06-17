#coding=utf-8
from datetime import datetime

def stringToDateDay(str):
    '''
    根据string返回对应的日期

    date: 2013-05-27
    param: 
        str 格式 'yyyy-MM-dd'
    '''
    date = datetime.strptime(str, '%Y-%m-%d')
    return date

def toDay(date):
    date = date.replace(hour = 0, minute = 0, second = 0)
    return date
    
def toNight(date):
    '''
    到当天的最后1s
    param : 
        datetime 2013-05-27 20:05:12
    return :
        datetime 2013-05-27 23:59:59
    '''
    date = date.replace(hour = 23, minute = 59, second = 59)
    return date
    
def dateToStringSecond(date):
    return date.strftime('%Y-%m-%d %H:%M:%S')