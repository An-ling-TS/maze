#clock.py
#定时器脚本
import time

class Clock():
    def __init__(self,name,length):
        self.name=name
        self.length=length
        self.time_=0
        self.start_time=0.0
        self.end_time=0.0
    def start(self):
        self.start_time = time.time()
    def stop(self):
        self.end_time = time.time()
    def timing(self):
        self.end_time = time.time()
        if self.end_time-self.start_time>self.length:
            return True
        return False

