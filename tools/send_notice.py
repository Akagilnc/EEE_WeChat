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
    sender = SMSSender(n='19',
                       date='5月8日，今天晚上7点',
                       course='路演怎么演',
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
run_time = datetime(2019, 5, 8, 10, 15, 00)
scheduler.add_job(tick, 'date', next_run_time=run_time)
print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass


