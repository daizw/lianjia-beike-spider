#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 二手房信息的数据结构


class ErShou(object):
    def __init__(self, district, area, name, price, desc, pic, 
            url, xiaoqu_url, xiaoqu_name, hid, unit_price):
        self.district = district
        self.area = area
        self.price = price
        self.name = name
        self.desc = desc
        self.pic = pic
        self.url = url
        self.xiaoqu_url = xiaoqu_url
        self.xiaoqu_name = xiaoqu_name
        self.hid=hid
        self.unit_price=unit_price

    def text(self):
        return ','.join([self.url,
                self.hid,
                self.district,
                self.area,
                self.xiaoqu_name,
                self.name,
                self.price,
                self.unit_price,
                self.desc,
                '"""'+self.pic+'"""',
                ])


