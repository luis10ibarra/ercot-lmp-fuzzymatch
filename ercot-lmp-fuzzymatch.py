# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:00:35 2024

@author: Luis.Ibarra
"""

import pandas as pd 

file1 = 'Settlement_Points_09062024_134422.csv'
file2 = 'NOIE_Mapping_09062024_134422.csv' 
file3 = 'MORA_November20241.xlsx' 

sp = pd.read_csv(file1) 
noie = pd.read_csv(file2) 
mora = pd.read_excel(file1)

print(sp)
print(noie)
print(mora)
