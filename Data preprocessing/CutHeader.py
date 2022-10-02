#%%
import os
#import tensorflow as tf
#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

# 측정데이터의 헤더 정보를 제거하고 
# 전압데이터만을 cuted.tmp 로 저장합니다. 
path = os.getcwd()
file_name = "CSM1.ROW"
file_path = path + "\\" + file_name
file_pathW = path + "\\" + "cuted.tmp"

f = open(file_path, 'r', encoding='utf-8')
fw = open(file_pathW, 'w', encoding='utf-8')
#rdr = csv.reader(f)
#for line in rdr:
#    print(line)
trigger = False
for line in f:
    if trigger == False:
        tmpbuf = line.split('\t')
        if tmpbuf[0] == "Roll":
            trigger = True
            fw.write(line)
    else:
        fw.write(line)
f.close()
fw.close()

cutf = pd.read_csv(file_pathW,sep='\t')
cutf.head(10)


#%%