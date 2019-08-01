import datetime
import random

def get_time_stamp():
    now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S");  # 生成当前时间
    random_num = random.randint(0, 10000);  # 生成的随机整数n，其中0<=n<=100
    if random_num <= 10:
        random_num = str(0) + str(random_num);
    unique_num = str(now_time) + str(random_num);
    return unique_num