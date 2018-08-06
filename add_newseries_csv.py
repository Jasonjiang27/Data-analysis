#-*-coding:utf-8-*-
import os
import csv
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from pymongo import MongoClient

#CUR_PATH = os.path.dirname(os.path.realpath(__file__))
#sys.path.append(CUR_PATH + "/../../../")
from MasCrawler_jyz.crawlerPlatform.commonScripts.commonFunction import findRelateName
from MasCrawler_jyz.crawlerPlatform.crawlerMongodb.model import CarType, CarSeries, CarBrand


host = '47.96.184.66'
port = 3717
client = MongoClient(host, port)
db = client['crawler']
db.authenticate('ugc', 'a1b2c3d4')

def get_series_brand():
    #import pdb;pdb.set_trace()
    #打开原csv文件
    csv_file = open('pcauto_sales.csv', 'r')
    csv_reader_lines = csv.reader(csv_file)
    #打开新csv文件
    new_csv_file = open('pcauto_sales_add.csv','a')
    writer = csv.writer(new_csv_file)
    first_row = ['autohome_series','autohome_brand','autohome_level']
    writer.writerow(first_row)
    num =0
    for line in csv_reader_lines:
        if line[3] !='car_type':
            #import pdb;pdb.set_trace()
        
            #只能使用find_one，若使用find无法获取，因为有多个
            res = db.car_type.find_one({'seriesName':{"$regex":line[3]},'config':{"$exists":True}})
            if res:
                autohome_series = res['seriesName']
                autohome_brand = res['brandName']
                try:
                    config = json.loads(res['config'])
                    autohome_level = config[u'基本参数'][u'级别'].strip()
                except KeyError:
                    
                    autohome_level = None
            else:
                autohome_series = None
                autohome_brand = None
                autohome_level = None

             #try:
                # firstCarType = CarType.objects(s_autohome_id=carSeries.autohome_id).first()
                    #if firstCarType.config!=None:
                    #config = json.loads(firstCarType.config)
                    #autohome_level = config[u"基本参数"][u"级别"].strip()
        else:
            continue
        res_list = [autohome_series, autohome_brand, autohome_level]
        #写入每行
        writer.writerow(res_list)
        num+=1
        print u'写入第{}条数据,车系：{},车品牌：{},车级别:{}'.format(num,autohome_series,autohome_brand,autohome_level)

    new_csv_file.close()
    csv_file.close()


if __name__=='__main__':
    get_series_brand()
    print u'写入完成'
