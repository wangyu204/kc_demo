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

import pandas as pd
import plotly as py
import plotly.figure_factory as pyff
#from plotly.tools import FigureFactory as pyff
#
import zsys
import ztools as zt
import ztools_str as zstr
import ztools_draw as zdr
import zpd_talib as zta
#
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

#================================
#1 预处理

pd.set_option('display.width', 450)    
pyplt=py.offline.plot    
#---------------

#2
xcod='600663'
fss='data/'+xcod+'.csv'
df=pd.read_csv(fss,index_col=0)
df=df.sort_index()
print('\n#2,df.tail()')
print(df.tail())

#3
print('\n#3,plot-->tmp/tmp_.html')
hdr,fss='k线图-'+xcod,'tmp/tmp_.html'
df2=df.tail(100)

#
# plotly函数接口变化，取消了vol成交量图形
#
zdr.drDF_cdl(df2,ftg=fss,m_title=hdr)

#4
print('\n#4,ok')
