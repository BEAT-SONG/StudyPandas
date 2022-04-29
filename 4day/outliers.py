#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np

def outliers_iqr3(dframe, data) :
    # Q1과 Q3 값 확인하기
    # percentile() : 25%와 75% 시점의 데이터 값을 알려준다.(retrun)
    q1, q3 = np.percentile(data, [25, 75])
    print(q1)
    print(q3)
    
    # IQR 값 계산하기
    iqr = q3 - q1

    print(iqr)
    
    # 최대값 계산하기
    upper_bound = q3 + (iqr*1.5)
    print(upper_bound)
    
    # 최소값 계산하기
    lower_bound = q1 - (iqr*1.5)
    print(lower_bound)
    
    # 나이 데이터에서 이상치 데이터 조회하기
    df_temp = dframe[(data < lower_bound) |
                   (data  > upper_bound)]
      
    print(len(df_temp))
    print(df_temp)

