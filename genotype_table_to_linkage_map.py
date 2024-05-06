#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 08:54:03 2024

@author: patrick.woods
"""

#Goal: Convert F2 hapmap to linkage map format #

import pandas as pd
import numpy as np
import os
os.chdir('/Users/patrick.woods/Desktop/python_practice/linkage_map/')

map = pd.read_table('f2_hapmap.hmp.txt')
map.info()
map.head()

map.iloc[0,1]

col = map.iloc[0:,1]
print(col)
type(col)
new_col = []

for i,r in col.iterrows():
    print(r)

#out of loop testing
loop_col = map[[f]] #extracts each column as a dataframe which allows us to use .loc and .iloc
f2_gt_list = []
type(loop_col.iloc[0,0]) #c24
loop_col.iloc[1,0] #uso31
loop_col.iloc[2,0] #f1


linkage_map = pd.DataFrame()
type(linkage_map)
linkage_map['ID'] = map['ID']
print(linkage_map)

for f in map.iloc[:,1:2]:
    
    loop_col = map[[f]] #extracts each column as a dataframe which allows us to use .loc and .iloc
    f2_gt_list = []
    
    for i,r in loop_col.iterrows():
        
        #print(str(r) == str(r))
        #print(loop_col.iloc[[i],:])
        
        
        if str(r.iloc[0]) == str(loop_col.iloc[0,0]): #testing for C24 genotype
           f2_gt_list.append('A')
           
        elif str(r.iloc[0]) == str(loop_col.iloc[1,0]): #testing for USO31 genotype
           f2_gt_list.append('B')
        
        elif str(r.iloc[0]) == str(loop_col.iloc[2,0]): #tetsing for F1 genotype
           f2_gt_list.append('H')
        
        else:
            f2_gt_list.append('NA')
    
    f2_gt_list_np = np.array(f2_gt_list)
    
    linkage_map[f] = f2_gt_list_np.tolist()
    
    
print(linkage_map)







