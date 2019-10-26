import requests

def line_notify():
    url = 'https://notify-api.line.me/api/notify'
    token = 'bQ05WiDOitJs9AoUNEQIAAZzh69IGTDDqe0V0RL2ftT'
    headers = {
                'content-type':
                'application/x-www-form-urlencoded',
                'Authorization':'Bearer ' + token
            }

    # while True:
    msg = "ชำระเงินสำเร็จ"
    r = requests.post(url, headers=headers , data = {'message':msg})
    print(r.text)

# line_notify()