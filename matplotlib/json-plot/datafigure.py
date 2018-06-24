# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd


def data_plot():
    try:
        df = pd.read_json('user_study.json')
    except ValueError:
        pass
    data = df.groupby('user_id').sum()
    user_id = df.user_id
    minutes = data.sum()
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)   #�����ָ�Ϊ1��1�еĵ�1��
    ax.set_title("StudyData")
    ax.set_xlabel("User ID")
    ax.set_ylabel("Study Time")
    x=data.index
    y=data.minutes
    ax.plot(x,y)
    plt.show()
    return ax 

if __name__=='__main__':
    data_plot()
