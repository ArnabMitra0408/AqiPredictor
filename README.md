# AqiPredictor
* Created a tool which able to predict the Air Quality Index of any given location.
* Data was gathered using OpenWeatherMap API
* Link for api: https://openweathermap.org/api/air-pollution
* Optimized KNN Classifier, Logistic Regression, Random Forest Classifier, Xgboost Classifier to reach the best model


## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle, xgboost, requests, geopy

## Data Collection
* Data was gathered using OpenWeatherMap API
* AQI data for all 29 states of India was taken from 1st January 2021 to 24th November 2021. 
* API required latitude and longitude of the place. So, all coordinates of states were gathered.
* Readings were spaced at 1 hour.
* Finally, 29 json files were created. 
* Json files were parsed to create the final dataframe.

## Dataset Overview
* Carbon monoxide 
* Nitrogen monoxide (NO)
* Nitrogen dioxide (NO2)
* Ozone (O3)
* Sulphur dioxide (SO2) 
* Ammonia (NH3) 
* particulates (PM2.5 and PM10)
* TimeStamp
* State

## EDA

Avg AQI per state was observed. It showed that punjab is the most polluted state with an average AQI of 4.67.
![image](https://user-images.githubusercontent.com/56645508/146666916-c46d933d-0ad3-4cd5-b6a0-3414e75159c6.png)

## Model Creation

4 different models were tested on the dataset. Their performance was validated using Stratified K-Fold Cross Validation.
Avg accuracy of each model is as follows:

*	**KNN** : 93.20%
*	**Logistic Regression**: 94.38%
*	**Random Forest Classifier**: 99.89%
*	**Xgboost Classifier**: 99.97%

## Productionization 
In this step, I built a flask API  that was hosted on local server. The api took the location entered by the user as input. The coordinates of the location are being found using geopy module. Those coordinates are being fed into the OpenWeatherMap api to get the pollutant data of that region. Based on that data the AQI is predicted using Xgboost model

 Below are the screenshots for the same:
 ![image](https://user-images.githubusercontent.com/56645508/146667192-d50232d0-d82f-42e7-9895-8f19a531c225.png)

![image](https://user-images.githubusercontent.com/56645508/146667198-9e0fe2b7-d686-4483-88db-ea12ac178215.png)

![image](https://user-images.githubusercontent.com/56645508/146667203-e303abb3-0bac-4493-b158-e55a27664063.png)

temp work
