import json
import pandas as pd

def analysis(file,user_id):
    try:
        df = pd.read_json(file)#��ȡjson�ļ�
    except ValueError:
        return 0,0
    df = df[df['user_id']==user_id].minutes  #ѡ��user_id��minutes����
    times = df.count()   #ͳ��user_id�Ĵ���
    minutes = df.sum()   #����ʱ���ܺ�
    return times,minutes   #����ʱ�䣬������

