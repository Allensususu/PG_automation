import numpy as np
import pandas as pd
#import finlab_crypto
import time 
#from finlab_crypto import Strategy
import datetime
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import xlwings as xw
import os
from pathlib import Path
from dateutil import parser
import datetime 
from datetime import timedelta, datetime, timezone,datetime
import datetime

def get_data_range(start_day):
    start = datetime.datetime.strptime(start_day, "%Y-%m-%d")
    end = datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d")
    date_generated = [start + datetime.timedelta(days=x) + datetime.timedelta(days=1) for x in range(0, (end - start).days)] 
    #    print(date.strftime("%Y-%m-%d"))
    return  date_generated

def add_rs_rank():
    btc = pd.read_csv(".\\history\\BTCUSDT-1d-data.csv", parse_dates=True, index_col=0)
    date = btc.index
    if "rs_rank" not in btc :
        btc = btc.assign(rs_rank=-1)
    btc = btc.groupby(btc.index).first()

    files = Path("history").glob("*.csv")
    for file in files:
        ohlcv  = pd.read_csv(file, parse_dates=True, index_col=0)
        if "rs_rank" not in ohlcv :
            ohlcv = ohlcv.assign(rs_rank=-1)
            ohlcv.to_csv(file)
                
    for y in range(len(btc)):
        if ( str(btc.at[(date[0]+ datetime.timedelta(days=y)) , "rs_rank"] )== "nan" ) or (str(btc.at[(date[0]+ datetime.timedelta(days=y)) , "rs_rank"] )== "-1"):
            rs_rank = []
            files = Path("history").glob("*.csv")
            for file in files:
                ohlcv  = pd.read_csv(file, parse_dates=True, index_col=0)
                ohlcv  = ohlcv.groupby(ohlcv.index).first()
                close = ohlcv.close
                ohlcv = ohlcv[:str(date[0]+ datetime.timedelta(days=y))[:10]]
                if str(date[0]+ datetime.timedelta(days=y))[:10] not in ohlcv.index :
                    continue

                if "rs_rank" not in ohlcv :
                    ohlcv = ohlcv.assign(rs_rank=-1)
                    #ohlcv.to_csv(file)
                #if ohlcv.at[day,"rs_rank"] == -1:
                if len(ohlcv) > 200:
                    year_return = (close[-1] - close[-200]) / close[-200]
                    print(year_return)
                    rs_rank.append([file, year_return])
                if len(ohlcv) < 200 and len(ohlcv) >= 10 :
                    year_return = (close[-1] - close[2]) / close[2]
                    print(year_return)
                    rs_rank.append([file, year_return])
                 
            rs_rank =sorted(rs_rank, key = lambda s: s[1])

            for i in range(len(rs_rank)):
                rs_rank[i] = [rs_rank[i][0],int(i/len(rs_rank)*100)]

            for i in rs_rank:
                ohlcv  = pd.read_csv(i[0], parse_dates=True, index_col=0)
                ohlcv  = ohlcv.groupby(ohlcv.index).first()
                if "rs_rank" not in ohlcv :
                    ohlcv = ohlcv.assign(rs_rank=-1)
                ohlcv.loc[date[0]+ datetime.timedelta(days=y), "rs_rank"] = i[1]    # day is date_list day
                ohlcv.to_csv(i[0])
            print(rs_rank)
            print(date[0]+ datetime.timedelta(days=y))