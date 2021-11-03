import requests
import json
from tqdm import tqdm
import threading
import time
import random


def WMS():
    order = []
    addr = ["新北市板橋區縣民大道二段7號","新北市板橋區雙十路二段209號", "新北市中和區中山路三段122號", "新北市中和區景新街419號", "新北市永和區大新街28號", "新北市土城區青雲路152號1樓", "新北市土城區中華路一段28號"]
    for x in range(100):
        order.append({
            "Index": x + 1,
            "customer_name": "gordon",  # 取件人姓名
            "customer_tel": "0222222222",  # 取件人電話
            "customer_ext": "19277",  # 取件人分機
            "customer_mobile": "0909090909",  # 取件人手機
            "customer_addr": random.choice(addr),
            "sender_name": "gordon",  # 寄件人姓名
            "sender_dt" : "2021/09/06 10:00",
            "sender_tel": "0909090909",  # 收件人手機
            "sender_ext": "19277",  # 寄件人分機
            "sender_companyname": "威剛",  # 取件公司
            "sender_uno": "",  # 統一編號
            "sender_mobile": "0909090909",  # 寄件人電話
            "sender_addr": random.choice(addr),  # 寄件人地址
            "sender_memo": '',  # 取件備註
            "receiver_name": "gordon",  # 收件人姓名
            "receiver_dt": "2021/09/06 16:00",  # 收件日期
            "receiver_tel": "0222222222",  # 寄件人手機
            "receiver_ext": "199",  # 寄件人分機
            "receiver_mobile": "0909090909",  # 收件人電話
            #"receiver_addr" : "新北市中和區連城路258號",
            "receiver_addr": random.choice(addr),
            "receiver_memo": "",
            "shipitems": "",
            "weight": 200,  # 重,
            "pkg_length": 2,  # 長,
            "pkg_width": 2,  # 寬,
            "pkg_height": 2,  # 高,
            "basic_charge": 200,# 基本,
            "overweight_charge": 0,
            "overcuft_charge": 0,# 超大,
            "ship_delycash": 0,
            "pay_type": '到付',
            "get_flag": "N"
        })
    jstring = {
        "Company": "Pressure",
        "Data_Number": "1987",
        'Order_Message': order
    }

    data = {
        'app_id': 'awayspeed',
        'app_key': "30atYljVtUejUBNKZSAL",
        'jstring': json.dumps(jstring)
    }
    requests.post('https://tms-ap.awayspeed.com/AWAYSPEED_API/AwaySpeed_ShipAPI.asmx/WMSOrder', data=data)
if __name__ == "__main__":
    start = time.time()
    ML_thread = []
    for i in tqdm(range(1000)):
        #ML_thread.append(threading.Thread(target=WMS))
        #ML_thread[i].start()
        WMS()
    end = time.time()
    during = end - start
    print(during)