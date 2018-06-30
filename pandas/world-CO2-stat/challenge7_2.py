import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 


def data_clean():
    #读取数据
    data = pd.read_excel("ClimateChange.xlsx",sheetname='Data')
    #选择数据
    df_co2 = data[data['Series code']=='EN.ATM.CO2E.KT'].set_index('Country code')
    df_gdp = data[data['Series code'] == 'NY.GDP.MKTP.CD'].set_index('Country code')
    #缺失值替换
    df_co2_nan = df_co2.replace({'..':pd.np.NaN})
    df_gdp_nan = df_gdp.replace({'..':pd.np.NaN})
    #缺失值填充
    df_co2_fill = df_co2_nan.iloc[:,5:].fillna(
            method='ffill',axis=1).fillna(method='bfill',axis=1)
    
    df_gdp_fill = df_gdp_nan.iloc[:,5:].fillna(
            method='ffill',axis=1).fillna(method='bfill',axis=1)
    #数据合并
    df_co2_fill['CO2-SUM']=df_co2_fill.sum(axis=1)
    df_gdp_fill['GDP-SUM']=df_gdp_fill.sum(axis=1)
    
    df_merge = pd.concat([df_co2_fill['CO2-SUM'],df_gdp_fill['GDP-SUM']],axis=1)
    #缺失值填充为0
    df_merge_fill = df_merge.fillna(value=0)
    
    return df_merge_fill

def co2_gdp_plot():
    df_clean = data_clean()
    #数据归一化处理
    df_max_min = (df_clean - df_clean.min()) / (df_clean.max() - df_clean.min())
    #获得中国归一化的数据
    china = []
    for i in df_max_min[df_max_min.index=='CHN'].values:
        china.extend(np.round(i, 3).tolist())
    #获得五个常任理事国的标签及对应的坐标刻度
    countries_label = ['USA', 'CHN', 'FRA', 'RUS', 'GBR']
    #获取国家标签作为刻度标签
    sticks_labels= []
    #获取国家相应的序号对应的刻度坐标
    labels_position=[]

    for i in range(len(df_max_min)):
        if df_max_min.index[i] in countries_label:
            sticks_labels.append(df_max_min.index[i])
            labels_position.append(i)

    #绘图
    fig = plt.subplot()
    df_max_min.plot(
            kind = 'line',
            title = 'GDP-CO2',
            ax = fig
            )
    plt.xlabel("Countries")
    plt.ylabel("Values")
    plt.xticks(labels_position, sticks_labels, rotation='vertical')
    plt.show()
    return fig,china

if __name__=='__main__':
    co2_gdp_plot()

