# !/usr/bin/env python
# coding: utf-8
# author:liujian
import threading.Thread


# 继承自threading.Thread
class MySqlThread(threading.Thread):
    def run(self):
        apply(self.func, self.args)

    def __init__(self, func, agrs, name=""):
        threading.Thread.__init__(self)
        self.func = func
        self.args = agrs
        self.name = name


threads = []


def insert_db(row):
    sqliteThread = MySqlThread()
