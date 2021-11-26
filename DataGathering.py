import numpy as np
import pandas as pd
import requests
import json


names=['andhra_pradesh','arunachal_pradesh','assam','bihar','chhattisgarh','goa','gujarat','haryana',
      'himachal','jandk','jharkhand','karnataka','kerela','madhya_pradesh','maharashtra','manipur',
      'meghalaya','mizoram','nagaland','odisha','punjab','rajasthan','sikkim','tamil_nadu','telengana','tripura',
      'uttar_pradesh','uttarakhand','west_bengal']
latitudes=['15.9129','28.2180','26.2006','25.0961','21.2787','15.2993','22.2587','29.0588','31.1048'
          ,'33.2778','23.6102','15.3173','10.8505','22.973','19.7515','24.6637','25.4670','23.1645',
          '26.1584','20.9517','31.1471','27.0238','27.5330','11.1271','18.1124','23.9408','26.846',
           '30.0668','22.9868']
longitudes=['79.7400','94.7278','92.9376','85.3131','81.8661','74.1240','71.1924','76.0856','77.1734',
           '75.3412','85.2799','75.7139','76.2711','78.6569','75.7139','93.9063','91.3662','92.9376',
           '94.5624','85.0985','75.3412','74.2179','88.512','78.6569','79.0193','91.9882','80.9462',
           '79.0193','87.8550']
print(len(names))
print(len(latitudes))
print(len(longitudes))

API_KEY="d9be5b1607992d9c2eb10dcafe8f42e2"
base_url="http://api.openweathermap.org/data/2.5/air_pollution/history?"
start_date="1609459932"
end_date="1637712732"
print('****************Data Download Started*************************')
for index in range(len(latitudes)):
    complete_url = base_url + "lat=" + latitudes[index] + "&lon=" + longitudes[index]+"&start="+start_date+'&end='+end_date+'&appid='+API_KEY
    response = requests.get(complete_url)
    data = response.json()
    file_name=names[index]+'.json'
    with open(file_name, 'w') as f:
        json.dump(data, f)
    print(file_name,' created!!!')

print('JSON DATA DOWNLOADED!!!!')

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
aqi_data.to_csv('aqi_data.csv',index=False)