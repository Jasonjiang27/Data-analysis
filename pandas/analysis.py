import json
import pandas as pd

def analysis(file,user_id):
    try:
        df = pd.read_json(file)#读取json文件
    except ValueError:
        return 0,0
    df = df[df['user_id']==user_id].minutes  #选择user_id的minutes数据
    times = df.count()   #统计user_id的次数
    minutes = df.sum()   #计算时间总和
    return times,minutes   #返回时间，分钟数

