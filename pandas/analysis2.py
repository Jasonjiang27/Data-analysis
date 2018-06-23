import json

def analysis(file,user_id):
    times=0
    minutes=0

    try:
        with open('user_study.json') as f:
            datas = json.load(f)
        for data in datas:
            if data['user_id']!=user_id:
                continue
            else:
                times+=1
                minutes+=data['minutes']
    except:
        pass

    return times,minutes
