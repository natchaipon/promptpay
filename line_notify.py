import requests
import datetime

def line_notify():
    url = 'https://notify-api.line.me/api/notify'
    token = 'bQ05WiDOitJs9AoUNEQIAAZzh69IGTDDqe0V0RL2ftT'
    headers = {
                'content-type':
                'application/x-www-form-urlencoded',
                'Authorization':'Bearer ' + token
            }
    date_time_now = datetime.datetime.now()
    date_time_now_sub = str(date_time_now)
    # print(date_time_now_sub[])
    msg = "ชำระเงินสำเร็จ" + " " + date_time_now_sub[:-7]
    r = requests.post(url, headers=headers , data = {'message':msg})
    print(r.text)

# line_notify()