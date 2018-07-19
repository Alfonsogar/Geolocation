#This program will import, clean and save all the geodata obtained from the web.

import geopandas
import pickle

regions_list = ['tarapaca', 'antofagasta', 'atacama', 'coquimbo', 'valparaiso',
                  'Libertador_Bernardo_OHiggins', 'maule', 'biobio', 'araucania',
                  'los_lagos', 'Aysén_del_General_Ibáñez_del_Campo', 'Magallanes_y_La_Antártica_Chilena',
                 'los_Rios', 'arica_y_Parinacota']
#As MANZANA_IND_C17.shp from metropolitano have not been found. we will use this provisional list

#regions_list =  ['tarapaca', 'antofagasta', 'atacama', 'coquimbo', 'valparaiso',
#                  'Libertador_Bernardo_OHiggins', 'maule', 'biobio', 'araucania',
#                  'los_lagos', 'Aysén_del_General_Ibáñez_del_Campo', 'Magallanes_y_La_Antártica_Chilena',
#                 'metropolitana', 'los_Rios', 'arica_y_Parinacota']

ruta = "../Geo_data"
columns_to_keep = ['MANZENT_I', 'TOTAL_PERS', 'geometry']

list_dataframes=[]

for region in regions_list:
    aux=[]
    #Load data
    path_entidad = ruta+region+"/ENTIDAD_C17.shp"
    path_manzana = ruta+region+"/MANZANA_IND_C17.shp"
    
    entidad_raw = geopandas.read_file(path_entidad)
    manzana_raw = geopandas.read_file(path_manzana)
    
    #Keeping columns
    entidad = entidad_raw[columns_to_keep]
    manzana = manzana_raw[columns_to_keep]
    
    #saving into a list
    aux.append(entidad)
    aux.append(manzana)
    
    #Adding to main list
    list_dataframes.append(aux)
    
    
# list_dataframes[x][0] = entidad dataframe
# list_dataframes[x][1] = manzana dataframe

#Export in binary
with open('../geodata.txt', 'wb') as fp:
    pickle.dump(list_dataframes, fp)