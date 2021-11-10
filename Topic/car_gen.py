import pandas as pd
import random
import string
from tqdm import tqdm


def random_num(digits=None):
    num = 0
    for bit in range(digits):
        num = num + random.randint(1, 9) * (10 ** bit)
    return str(num)


def random_plate():
    eng = ''.join(random.choice(string.ascii_uppercase) for x in range(3))
    return eng + '-' + random_num(digits=4)


if __name__ == '__main__':
    station = ['a']
    car_type = ['電動三輪車']
    color = ['黑', '白']
    sample = pd.read_excel("C:/Users/gordon_zhuang/Downloads/carsample.xlsx")
    for x in tqdm(range(100)):
        sample.loc[x] = [
            'test10',
            random.choice(station),
            random_plate(),
            (random.choice(string.ascii_uppercase) + random_num(digits=5)),
            random.choice(car_type),
            '電動三輪車',
            random_num(digits=7),
            random_num(digits=10),
            random.choice(color),
            '2019/05/01',
            '2019/05',
            '2022/05/01',
            random_num(digits=8),
            '2022/12/31',
            '啟用'
        ]
    sample.to_excel("C:/Users/gordon_zhuang/Downloads/100cars.xlsx", index=False)