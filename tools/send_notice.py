import requests


class SMSSender:
    def __init__(self, n, date, course, location):
        self.template, self.sign = '3e_course_notice', '3ewbs'
        self.url = 'https://yf8l2fce.api.lncld.net/1.1/requestSmsCode'
        self.head = {
            "X-LC-Id": "Yf8L2FCEH7WRJDH4310BdkCR-gzGzoHsz",
            "X-LC-Key": "lzXeOFgnHEdjPn5coU2g5qPW"
        }
        self.params = {
            "template": self.template,
            "sign": self.sign,
            "n": n,
            "course": course,
            "date": date,
            "location": location
        }

    def send_sms(self, number_list):
        for number in number_list:
            print(number)
            self.params["mobilePhoneNumber"] = number
            response = requests.post(url=self.url, headers=self.head, json=self.params)
            print(response.status_code)


def pre_send():
    sender = SMSSender(n='6',
                       date='3月31日上午9点',
                       course='从品牌注册到销售上亿的坑和方法',
                       location='菁蓉汇3A座9楼路演厅')
    number_list = open('phone_numbers.txt').readlines()
    sender.send_sms([number.strip() for number in number_list])

    sender = SMSSender(n='7',
                       date='3月31日下午2点',
                       course='如何进行有效的市场合作',
                       location='菁蓉汇3A座9楼路演厅')
    number_list = open('phone_numbers.txt').readlines()
    sender.send_sms([number.strip() for number in number_list])


from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler


def tick():
    pre_send()


from pytz import timezone

tz_utc_8 = timezone('Asia/Shanghai')
print(tz_utc_8)
scheduler = BlockingScheduler(timezone=tz_utc_8)
run_time = datetime(2019, 3, 30, 9, 30, 10)
scheduler.add_job(tick, 'date', next_run_time=run_time)
print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass
