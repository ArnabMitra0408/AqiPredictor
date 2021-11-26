import numpy as np
import pandas as pd
import requests
import json
from datetime import datetime


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

