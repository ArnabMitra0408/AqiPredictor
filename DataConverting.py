import numpy as np
import pandas as pd
import requests
import json
from datetime import datetime

names=['andhra_pradesh','arunachal_pradesh','assam','bihar','chhattisgarh','goa','gujarat','haryana',
      'himachal','jandk','jharkhand','karnataka','kerela','madhya_pradesh','maharashtra','manipur',
      'meghalaya','mizoram','nagaland','odisha','punjab','rajasthan','sikkim','tamil_nadu','telengana','tripura',
      'uttar_pradesh','uttarakhand','west_bengal']
print('******************Converting To DataFrame Now*********************')
co=[]
no=[]
no2=[]
o3=[]
so2=[]
pm2_5=[]
pm10=[]
nh3=[]
aqi=[]
state_name=[]
timestamp=[]
for name in names:
    with open(name+'.json') as f:
        data = json.load(f)
        for i in range(len(data['list'])):
            aqi.append(data['list'][i]['main']['aqi'])
            co.append(data['list'][i]['components']['co'])
            no.append(data['list'][i]['components']['no'])
            no2.append(data['list'][i]['components']['no2'])
            o3.append(data['list'][i]['components']['o3'])
            so2.append(data['list'][i]['components']['so2'])
            pm2_5.append(data['list'][i]['components']['pm2_5'])
            pm10.append(data['list'][i]['components']['pm10'])
            nh3.append(data['list'][i]['components']['nh3'])
            temp_date=int(data['list'][i]['dt'])
            date=datetime.utcfromtimestamp(temp_date).strftime('%Y-%m-%d %H:%M:%S')
            timestamp.append(date)
            state_name.append(name)
        del data


aqi_data=pd.DataFrame(aqi,columns=['aqi'])
aqi_data['co']=co
aqi_data['no']=no
aqi_data['no2']=no2
aqi_data['o3']=o3
aqi_data['so2']=so2
aqi_data['pm2_5']=pm2_5
aqi_data['pm10']=pm10
aqi_data['nh3']=nh3
aqi_data['state']=state_name
aqi_data['timestamp']=timestamp
aqi_data.to_csv('aqi_data.csv',index=False)
print('************Dataset Created!!!!!!!!*******************')