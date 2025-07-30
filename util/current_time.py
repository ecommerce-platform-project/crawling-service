from datetime import datetime, timezone, timedelta
import time
import random

now = datetime.now()



def get_current_time():

    # 한국 시간 (UTC+9)
    kst = timezone(timedelta(hours=9))
    korea_time = datetime.now(kst)
    return korea_time.strftime("%Y-%m-%d %H:%M:%S %Z")

def custom_sleep(start, end):
    custom_time = random.uniform(start, end)
    time.sleep(custom_time)