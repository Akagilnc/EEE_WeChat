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

    @staticmethod
    def send_sms(number_list):
        for number in number_list:
            print(number)
            # self.params["mobilePhoneNumber"] = number
            # response = requests.post(url=self.url, headers=self.head, json=self.params)
            # print(response.status_code)


def pre_send():
    sender = SMSSender(n='4',
                       date='2019 年 10 月 31 号',
                       course='创业公司 的 法律风险防控',
                       location='菁蓉汇3A座9楼路演厅')
    number_list = open('phone_numbers.txt').readlines()
    print(number_list)
    sender.send_sms([number.strip() for number in number_list])


from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler


def tick():
    pre_send()


if __name__ == '__main__':
    from pytz import timezone

    tz_utc_8 = timezone('Asia/Shanghai')
    print(tz_utc_8)
    scheduler = BlockingScheduler(timezone=tz_utc_8)
    run_time = datetime(2019, 3, 23, 9, 30, 00)
    scheduler.add_job(tick, 'date', next_run_time=run_time)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
