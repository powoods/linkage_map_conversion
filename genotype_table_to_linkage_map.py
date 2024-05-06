#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 08:54:03 2024

@author: patrick.woods
"""

#v1

def table_to_linkage_map(file, parent1_row_index=0, parent1_col_index=0, parent2_row_index=1,parent2_col_index=0, f1_row_index=2,f1_col_index=0, id_col = 'ID'):
    '''
    

    Parameters
    ----------
    file : String
        A string that is the title of a tab deliminted text file containing the genotype call across all samples for every marker.
        The genotype file is very simple with the first column being the genotype IDs and every subsequent column being their genotype calls
        at every marker. Each marker is its own separate column. The genotypes can be coded however is preferred.
    parent1_row_index : Integer, optional
        Integer indicating the row index for parent 1's genotype call. The default is 0.
    parent1_col_index : Integer, optional
        DESCRIPTION. The default is 0.
    parent2_row_index : TYPE, optional
        DESCRIPTION. The default is 1.
    parent2_col_index : TYPE, optional
        DESCRIPTION. The default is 0.
    f1_row_index : TYPE, optional
        DESCRIPTION. The default is 2.
    f1_col_index : TYPE, optional
        DESCRIPTION. The default is 0.
    id_col : TYPE, optional
        DESCRIPTION. The default is 'ID'.

    Returns
    -------
    linkage_map : TYPE
        DESCRIPTION.

    '''
    

    import pandas as pd
    import numpy as np
    
    map = pd.read_table(file)
    
    linkage_map = pd.DataFrame() #creating an empty data frame to store the linkage map converted genotypes in
    linkage_map['ID'] = map[id_col]
    
    for f in map.iloc[:,1:]: #iterating over all column after the first column which containins sample IDs.
        
        loop_col = map[[f]] #extracts each column as a dataframe which allows us to use .loc and .iloc
        f2_gt_list = []
        
        for i,r in loop_col.iterrows():
            
            if str(r.iloc[0]) == str(loop_col.iloc[parent1_row_index,parent1_col_index]): #testing for parent 1 genotype
               f2_gt_list.append('A')
               
            elif str(r.iloc[0]) == str(loop_col.iloc[parent2_row_index,parent2_col_index]): #testing for parent 2 genotype
               f2_gt_list.append('B')
            
            elif str(r.iloc[0]) == str(loop_col.iloc[f1_row_index,f1_col_index]): #tetsing for F1 genotype
               f2_gt_list.append('H')
            
            else:
                f2_gt_list.append('NA')
        
        f2_gt_list_np = np.array(f2_gt_list)
        
        linkage_map[f] = f2_gt_list_np.tolist()
        
    return linkage_map


### testing out the function with default parameters       
lm= table_to_linkage_map('f2_hapmap_diploid_tp.txt')

lm.to_csv('converted_map2.csv', index = False)





