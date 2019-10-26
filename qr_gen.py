import pyqrcode
import requests
import time
from PIL import Image

state = False
response = None
qr_show = None

def generate_qr():
    global state
    global response
    global qr_show

    part_file = "C:/Users/Natchaipon/Documents/promptplay/url.png"

    if state == False:
        gen_id = requests.get('https://scb.azurewebsites.net/api/Qr')
        response = gen_id.json()
        # print(response)
        url = pyqrcode.create(response['data']['qrRawData'])
        url.png(part_file , scale=5)

        qr_show = Image.open(part_file)
        qr_show.show()
        time.sleep(5)
        # print(qr_show.bits, qr_show.size, qr_show.format)
        qr_show.close()
        state = True

    if state == True:
        check_money = requests.get('https://scb.azurewebsites.net/api/verify/' + str(response['verifyId']))
        response_check_money = check_money
        if response_check_money.text == 'true':
            print("ชำระเงินสำเร็จแล้ว")
            # qr_show.close()
            state = False



if __name__ == '__main__':
    while True:
        generate_qr()
        time.sleep(2)



