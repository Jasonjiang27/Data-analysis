import pandas as pd


def quarter_volume():
    data = pd.read_csv('apple.csv',header=0)#读取csv文件
    s = data.Volume
    #转化为时间序列
    s.index = pd.to_datetime(data.Date)
    #按季度重采样，并计算总和后排序，取排名第二高的季度
    second_volume = s.resample('Q').sum().sort_values()[-2]
    return second_volume

