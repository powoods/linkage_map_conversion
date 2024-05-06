#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:54:03 2024

@author: patrick.woods
"""

#v2

def hapmap_to_linkage_map_v2(hapmap, parent1_row_index=0, parent1_col_index=0, parent2_row_index=1,parent2_col_index=0, f1_row_index=2,f1_col_index=0):
    '''
    Function Description : 
    --------------------
        A function that takes in a TASSEL5 formatted HapMap genotype file and converts it to an F2 linkage map (A, H, B) formatted file that can be input
        into software such as JoinMap for calculating genetic distances. All arguments other than 'hapmap' have default values that assume the order of
        samples in the TASSEL5 formatted HapMap is as follows: parent_1, parent_2, F1, F2_1, F2_2, F2_3,F2_4, etc. If the HapMap does not explicitly have
        parent 1, parent 2 and the F1 in this specific order, the respective row and column indexes will need to be changed to the correct values.
    
    Parameters
    ----------
    hapmap : String
        A string that is the title of a tab deliminted 'hapmap' text file produced using TASSEL5 that contains the genotype call across all samples for every marker.
        The genotypes can be coded however is preferred.
    parent1_row_index : Integer, optional
        Integer indicating the row index for parent 1's genotype call for each marker. The default is 0.
    parent1_col_index : Integer, optional
        Integer indicating the column index for parent 1's first genotype call for each marker. The default is 0.
    parent2_row_index : Integer, optional
        Integer indicating the row index for parent 2's first genotype call for each marker. The default is 1.
    parent2_col_index : Integer, optional
        Integer indicating the column index for parent 2's first genotype call for each marker. The default is 0.
    f1_row_index : Integer, optional
        Integer indicating the row index for the F1's first genotype call for each marker. The default is 2.
    f1_col_index : Integer, optional
        Integer indicating the column index for the F1's first genotype call for each marker. The default is 0.

    Returns
    -------
    linkage_map : pandas DataFrame
        A tabular pandas DataFrame type object that contains the converted genotypes in A, H, and B formats.

    '''
    

    import pandas as pd
    import numpy as np
    
    map = pd.read_table(hapmap, index_col=0)
    map = map.drop(map.columns[[0,1,2,3,4,5,6,7,8,9]], axis=1)
    
    map = map.transpose()
    map = map.reset_index()
    
    linkage_map = pd.DataFrame() #creating an empty data frame to store the linkage map converted genotypes in
    linkage_map['ID'] = map['index']
    
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
lm= table_to_linkage_map_v2('f2_hapmap_diploid.hmp.txt')

lm.to_csv('converted_map3.csv', index = False)







