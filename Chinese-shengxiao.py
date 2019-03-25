#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2019/03/11 10:19
# @Software: PyCharm

#记录生肖，根据年份判断生肖。

chinese_shengxiao ='猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = int(input("Please enter the year of birth:"))

if (chinese_shengxiao[year % 12]) == "狗":
    print("Dog year Wang Wang Wang!")
for year in range(1994, 2020):
    print("%d年的生肖是%s！" % (year, chinese_shengxiao[year % 12]))

