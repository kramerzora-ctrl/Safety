import os 
os.getcwd() 

import pandas as pd

## Cleaning Alemeda
alameda = pd.read_csv('FinalProject/UncleanData/Alameda_14_24.csv')
alameda
trucks_al = alameda[alameda['TRUCK_ACCIDENT'] == 'Y']
trucks_al_parked = trucks_al[(trucks_al['MVIW'] == 'E') | (trucks_al['MVIW'] == '4')]
trucks_al_parked_ramp = trucks_al_parked[(trucks_al['LOCATION_TYPE'] == 'R')]
trucks_al_parked
trucks_al_parked.to_csv('FinalProject/DataCleaning/Alameda_Trucks_Parked.csv', index=False)

##cleaninf fresno
fresno = pd.read_csv('FinalProject/UncleanData/Fresno_14_24.csv')
fresno
trucks_fr = fresno[fresno['TRUCK_ACCIDENT'] == 'Y']
trucks_fr_parked = trucks_fr[(trucks_fr['MVIW'] == 'E') | (trucks_fr['MVIW'] == '4')]
trucks_fr_parked_ramp = trucks_fr_parked[(trucks_fr_parked['LOCATION_TYPE'] == 'R')]
trucks_fr_parked
trucks_fr_parked.to_csv('FinalProject/DataCleaning/Fresno_Trucks_Parked.csv', index=False)


##clean LA
la2 = pd.read_csv('FinalProject/UncleanData/LA_Glendora_Mal_14_24.csv')
la3 = pd.read_csv('FinalProject/UncleanData/LA_Manh_Whit_14_24.csv')
la1 = pd.read_csv('FinalProject/UncleanData/LA_UnI_Glendale_14_24.csv')
la = pd.concat([la1, la2, la3], ignore_index=True)
la
trucks_la = la[la['TRUCK_ACCIDENT'] == 'Y']
trucks_la_parked = trucks_la[(trucks_la['MVIW'] == 'E') | (trucks_la['MVIW'] == '4')]
trucks_la_parked_ramp = trucks_la_parked[(trucks_la_parked['LOCATION_TYPE'] == 'R')]
trucks_la_parked_ramp
trucks_la_parked_ramp.to_csv('FinalProject/DataCleaning/LA_Trucks_Parked.csv', index=False)