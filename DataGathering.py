import numpy as np
import pandas as pd
import requests
import json

names=['north-delhi','north-west-delhi','south-delhi','north-east-delhi','west-delhi','south-west-delhi'
      ,'south-east-delhi','new-delhi','central-delhi','east-delhi','noida-sector52','noida-sector62',
      'greater-noida-sector2','noida-sector16','noida-sector10','noida-sector23','gurgaon','faridabad',
      'noida-sector40','noida-sector100','noida-sector150','noida-sector120','noida-sector163']
latitudes=['28.7886','28.7186','28.4817','28.7184','28.6663','28.5929','28.5630','28.613',
          '28.6643','28.6280','28.5867','28.6280','28.5794','28.5787','28.5905','28.5929','28.4595',
           '28.4089','28.5632','28.5452','28.4223','28.5865','28.4791']
longitudes=['77.1412','77.0685','77.1873','77.2580','77.0680','77.0346','77.2611','77.2090',
           '77.2167','77.2956','77.3728','77.3649','77.450','77.3174','77.3317','77.3528','77.0266',
           '77.3178','77.3540','77.3679','77.4903','77.3963','28.4791']
print(len(names))
print(len(latitudes))
print(len(longitudes))

API_KEY="d9be5b1607992d9c2eb10dcafe8f42e2"
base_url="http://api.openweathermap.org/data/2.5/air_pollution/history?"
start_date="1606435932"
end_date="1637712732"
for index in range(len(latitudes)):
    complete_url = base_url + "lat=" + latitudes[index] + "&lon=" + longitudes[index]+"&start="+start_date+'&end='+end_date+'&appid='+API_KEY
    response = requests.get(complete_url)
    data = response.json()
    file_name=names[index]+'.json'
    with open(file_name, 'w') as f:
        json.dump(data, f)
    print(file_name,' created!!!')