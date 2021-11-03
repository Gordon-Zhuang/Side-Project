import requests
import json
import random
from random import randrange
from tqdm import tqdm
from faker import Faker
from datetime import date
from geopy.geocoders import Nominatim
import threading

faker = Faker('zh_TW')
geocoder = Nominatim(user_agent='random_address')



def random_num(digits=None):
    num = ''
    for bit in range(digits):
        num += str(randrange(10))
    return num


def random_mobile():
    return '09' + random_num(digits=8)


def random_address():
    case = randrange(2)
    if case == 0:
        lat = round(random.uniform(24.965376, 25.115544), 6)
        long = round(random.uniform(121.401070, 121.612159), 6)
    elif case == 1:
        lat = round(random.uniform(24.758191, 24.901888), 6)
        long = round(random.uniform(120.978614, 121.025950), 6)
    '''
    elif case == 1:
        lat = round(random.uniform(24.925784, 25.069279), 6)
        long = round(random.uniform(121.155996, 121.372190), 6)
    '''

    location = geocoder.reverse((lat, long))
    try:
        road = location.raw['address']['road']
    except KeyError:
        try:
            road = location.raw['address']['hamlet']
        except KeyError:
            try:
                road = location.raw['address']['neighbourhood']
            except KeyError:
                try:
                    road = location.raw['address']['residential']
                except KeyError:
                    try:
                        road = location.raw['address']['industrial']
                    except KeyError:
                        road = '255號'
    try:
        city = location.raw['address']['city']
    except KeyError:
        city = location.raw['address']['county']
    try:
        suburb = location.raw['address']['suburb']
    except KeyError:
        try:
            suburb = location.raw['address']['suburb']
        except KeyError:
            suburb = location.raw['address']['city_district']

    return city + suburb + road


def WMS():
    #today = date.today()
    #td = today.strftime("%Y/%m/%d")
    #send_d = td + ' 10:00'
    #rec_d = td + ' 16:00'
    #pay = ['到付', '元付']
    order = []
    for x in range(10):
        order.append({
            "Index": x + 1,
            #"customer_name": faker.name(),  # 取件人姓名
            #"customer_tel": random_mobile(),  # 取件人電話
            #"customer_ext": random_num(digits=4),  # 取件人分機
            #"customer_mobile": random_mobile(),  # 取件人手機
            "customer_name": "gordon",  # 取件人姓名
            "customer_tel": "0222222222",  # 取件人電話
            "customer_ext": "19277",  # 取件人分機
            "customer_mobile": "0909090909",  # 取件人手機
            #"customer_addr": random_address(),  # 取件人地址
            "customer_addr": "新北市中和區連城路258號",
            #"sender_name": faker.name(), # 寄件人姓名
            #"sender_dt": send_d,  # 取件日期
            #"sender_tel": random_mobile(),  # 收件人手機
            #"sender_ext": random_num(digits=4),  # 寄件人分機
            #"sender_companyname": faker.company(),  # 取件公司
            #"sender_uno": random_num(digits=8),  # 統一編號
            #"sender_mobile": random_mobile(), # 寄件人電話
            "sender_name": "gordon",  # 寄件人姓名
            "sender_dt" : "2021/09/06 10:00",
            "sender_tel": "0909090909",  # 收件人手機
            "sender_ext": "19277",  # 寄件人分機
            "sender_companyname": "威剛",  # 取件公司
            "sender_uno": "",  # 統一編號
            "sender_mobile": "0909090909",  # 寄件人電話
            #"sender_addr": random_address(),  # 寄件人地址
            "sender_addr": "新北市中和區連城路258號",  # 寄件人地址
            "sender_memo": '',  # 取件備註
            #"receiver_name": faker.name(),  # 收件人姓名
            #"receiver_dt": rec_d,  # 收件日期
            #"receiver_tel": random_mobile(),  # 寄件人手機
            #"receiver_ext": random_num(digits=4),  # 寄件人分機
            #"receiver_mobile": random_mobile(),  # 收件人電話
            "receiver_name": "gordon",  # 收件人姓名
            "receiver_dt": "2021/09/06 16:00",  # 收件日期
            "receiver_tel": "0222222222",  # 寄件人手機
            "receiver_ext": "199",  # 寄件人分機
            "receiver_mobile": "0909090909",  # 收件人電話
            #"receiver_addr": random_address(),  # 收件人地址
            "receiver_addr" : "新北市中和區連城路258號",
            "receiver_memo": "",
            "shipitems": "",
            #"weight": random_num(digits=2),  # 重,
            #"pkg_length":  random_num(digits=2),  # 長,
            #"pkg_width": random_num(digits=2),  # 寬,
            #"pkg_height": random_num(digits=2),  # 高,
            "weight": 20,  # 重,
            "pkg_length": 20,  # 長,
            "pkg_width": 20,  # 寬,
            "pkg_height": 20,  # 高,
            #"basic_charge": random_num(digits=3),
            "basic_charge": 200,# 基本,
            #"overweight_charge": random_num(digits=2),  # 超重,
            "overweight_charge": 0,
            #"overcuft_charge": random_num(digits=2),
            "overcuft_charge": 0,# 超大,
            "ship_delycash": 0,
            "pay_type": '到付',
            "get_flag": "N"
        })
    jstring = {
        "Company": "ADATA",
        "Data_Number": "1987",
        'Order_Message': order
    }

    data = {
        'app_id': 'awayspeed',
        'app_key': "30atYljVtUejUBNKZSAL",
        'jstring': json.dumps(jstring)
    }
    x = requests.post('https://tms-ap.awayspeed.com/AWAYSPEED_API/AwaySpeed_ShipAPI.asmx/WMSOrder', data=data)
    #print(x.text)


if __name__ == "__main__":
    ML_thread = []
    for i in tqdm(range(10)):
        ML_thread.append(threading.Thread(target=WMS))
        ML_thread[i].start()
        #WMS()

    #print(x.text)