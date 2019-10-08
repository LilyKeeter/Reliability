import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
import Gen5Info as Info

directory = r'C:\gen5\prp'
resultPath = r'C:\gen5\preprocessed'

#Cleaning/debug function
def cleanApril(df, delete):
    for column in list(Info.columns.keys()):
        trash=[value for value in df[column].unique() if value not in Info.columns.get(column)]
        trash=[value for value in trash if str(value)!='nan']
        row = [[df[df[column]==value].index[0],df[df[column]==value].index[-1]] for value in trash]
        if len(trash)!=0 and not delete:
            print(column, 'trash values: ', trash, 'row indeces: ', row)
        if delete:
            for s in row:
                df.drop(df.index[s[0]:s[1]], inplace=True)

for fileName in os.listdir(directory):

    #Load dataset
    df = pd.read_csv(os.path.join(directory,fileName))   
    print(fileName)
    
    if fileName=='NL0437_C3.csv' or fileName=='NL0441_C4.csv':
        df.dropna(subset=['WHTRMODE'], inplace=True)
        cleanApril(df,True)
    
    df['WHTRMODE'] = df['WHTRMODE'].apply(lambda x: 'Heat Pump' if x=='Heat-Pump' else x)
    
    df.to_csv(os.path.join(resultPath,fileName), index = False)
    print('\n\n\n')