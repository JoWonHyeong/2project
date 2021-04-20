import Oracle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

v = 50
n = 10
vol_bucket = []
price = []
volsum = 0
order = 0
price_bucket = 0
sellsum = 0
buysum = 0
a = 0
pin = 0
pin_sum = 0
price_sum = 0
size = 0

while(True):
    vpin = 0
    kakaosize = len(Oracle.select())

    if (size < kakaosize): #### 데이터 읽는 조건
        size = kakaosize
        order = int(Oracle.oneselect()[1])
        volsum += abs(order)
        if (order < 0):
            sellsum += volsum
            volsum = 0
        if (order > 0):
            buysum += volsum
            volsum = 0
        while (sellsum + buysum >= v):
            if (order < 0):
                sell = v - buysum
                pin = abs(sell - buysum)
                vol_bucket.append([sell, buysum, pin])
                sellsum = sellsum - sell
                buysum = 0
                sell = 0
                if (len(vol_bucket) == n):
                    for i in range(len(vol_bucket)):
                        pin_sum += vol_bucket[i][1]
                    vpin = (pin_sum / (n * v) * 100)
                    pin_sum = 0
                    del vol_bucket[0]
            else:

                buy = v - sellsum
                pin = abs(sellsum - buy)
                vol_bucket.append([sellsum, buy, pin])
                buysum = buysum - buy
                sellsum = 0
                buy = 0
                if (len(vol_bucket) == n):
                    for i in range(len(vol_bucket)):
                        pin_sum += vol_bucket[i][0]
                    vpin = (pin_sum / (n * v) * 100)
                    pin_sum = 0
                    del vol_bucket[0]
        if(vpin!=0):
            print(vpin)