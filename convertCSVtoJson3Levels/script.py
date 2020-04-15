import configparser
import json
from collections import OrderedDict
from itertools import groupby

import pandas as pd

config = configparser.RawConfigParser()   
configFilePath = 'config.config'
config.read(configFilePath,encoding='utf-8')

dataFile = config.get('Config', 'datacsvFile')
jsonOuputFile =  config.get('Config', 'jsonOutFile')
sheetExcelName =  config.get('Config', 'sheetName')
df = pd.read_csv(dataFile, encoding='utf-8', dtype=str)
# df = pd.read_excel(dataFile, sheet_name=sheetExcelName, encoding='utf-8', dtype=str)

d=dict()

names = df.columns.values.tolist()
data = df.values

results = dict()
results2 = dict()
results3 = dict()
results4 = dict()
  

data2 = [dict(zip(names, d)) for d in data]
for item in data2:  

    sku = item["sku"]
    jan = item["jan"]

    if pd.isnull(sku):
        continue
    if pd.isnull(jan):
        continue

    key1 = item["key1"]
    key2 = item["key2"]
    key3 = item["key3"]
    key4 = item["key4"]
    
    del item["key1"]
    del item["key2"]
    del item["key3"]
    del item["key4"]

    #for key4
    if not pd.isnull(key4):
        list_key1=[] 
        for k in results.keys():
            list_key1.append(k)
        if not key1 in list_key1:
            list_item=[]
            results2={}
            results3={}
            results4={}
            list_item.append(item)
            results4.update({key4:list_item})
            results3.update({key3:results4})
            results2.update({key2:results3})  
            results.update({key1:results2})
        else:
            list_key2 = []
            for k in results2.keys():
                list_key2.append(k)
            if not key2 in list_key2:
                list_item=[]
                results3={}
                results4={}
                list_item.append(item)
                results4.update({key4:list_item})
                results3.update({key3:results4})
                results2.update({key2:results3}) 
            else:
                list_key3=[]
                for k in results3.keys():
                    list_key3.append(k)
                if not key3 in list_key3:
                    list_item=[]
                    results4={}
                    list_item.append(item)
                    results4.update({key4:list_item})
                    results3.update({key3:results4})
                else:   
                    list_key4=[]
                    for k in results4.keys():
                        list_key4.append(k)
                    if not key4 in list_key4:
                        list_item=[]
                        list_item.append(item)
                        results4.update({key4:list_item})
                    else:   
                        list_item.append(item)
                        results4.update({key4:list_item})
    else: 
        list_key1=[] 
        for k in results.keys():
            list_key1.append(k)
        if not key1 in list_key1:
            list_item=[]
            results2={}
            results3={}
            list_item.append(item)
            results3.update({key3:list_item})
            results2.update({key2:results3})  
            results.update({key1:results2})
        else:
            list_key2 = []
            for k in results2.keys():
                list_key2.append(k)
            if not key2 in list_key2:
                list_item=[]
                results3={}
                list_item.append(item)
                results3.update({key3:list_item})
                results2.update({key2:results3}) 
            else:
                list_key3=[]
                for k in results3.keys():
                    list_key3.append(k)
                if not key3 in list_key3:
                    list_item=[]
                    list_item.append(item)
                    results3.update({key3:list_item})
                else:   
                    list_item.append(item)
                    results3.update({key3:list_item})
        

 


# print(json.dumps(results2, indent=4,ensure_ascii=False))

# export the final result to a json file
with open(jsonOuputFile, 'w',encoding='utf-8') as outfile:
    json.dump(results, outfile,indent=4,ensure_ascii=False)
