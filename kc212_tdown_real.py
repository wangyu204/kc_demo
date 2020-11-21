# -*- coding: utf-8 -*-
'''
TopQuant-简称TQ极宽智能量化回溯分析系统，培训课件-配套教学python课件程序

Top极宽量化(原zw量化)，Python量化第一品牌 
by Top极宽·量化开源团队 2017.10.1 首发

网站： www.TopQuant.vip      www.ziwang.com
QQ群: Top极宽量化1群，124134140
      Top极宽量化2群，650924099
      Top极宽量化3群，450853713
  
'''

import os,arrow,shutil  
import numpy as np
import pandas as pd
import tushare as ts

#  TopQuant
import zsys 
import ztools as zt
import ztools_datadown as zddown

#----------
#-----------------
print('''
      本案例取消
      因为pd,mpl,ts，openCV，sklearn,tf部分基础模块库，api函数接口改了
      有兴趣的用户，请自行根据提示信息，修改相关源码

      开源项目，函数API接口，参数变化，属于很正常的现象
      每次大的版本升级，都会有个别模块库函数API接口变化，
      这种因为版本变化，引发的程序代码冲突，称为：版本冲突
      所以，使用开源软件，要养成多动手搜索/查看最新版本的软件文档/函数接口餐宿
      ''')
#-----------------


#1 下载股票实时数据文件
rss=zsys.rdatReal
zt.f_dirDel(rss) 
print('rs0:',rss)
#默认是下载5分钟分时数据
xtyp='5' 
print('xtyp:',xtyp)


#
#2 指数代码文件，下载所有指数实时数据
# 指数数据文件名是以“inx_”开头
finx='inx\\inx_code.csv'
print('\n#2,finx,',finx)
zddown.down_min_all(rss,finx,xtyp,fgIndex=True)



#3 股票代码文件，下载所有股票实时数据，可使用自定义股票池代码文件
#fstk='inx\\stk_code.csv'
fstk='data/stk_pool.csv'
print('\n#3,fstk,',fstk)
zddown.down_min_all(rss,fstk,xtyp,fgIndex=False)


