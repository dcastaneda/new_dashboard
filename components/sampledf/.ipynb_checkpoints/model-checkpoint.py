import pandas as pd

df_costos = pd.read_csv('./data/dfsample/costos.csv')

df_opsales = pd.read_csv('./data/dfsample/opsales.csv')

df_markers = pd.read_csv('./data/dfsample/markers.csv')

# dataset de prueba para el mapa
datatest ={'DEPARTAMENTO': ['SANTANDER', 'ANTIOQUIA', 'CUNDINAMARCA', 'BOYACA'], 
       'COUNT':[99, 900, 9000,900000], 
       'COD_DPTO':['68', '05', '25','15']} 
  
df_maptest = pd.DataFrame.from_dict(datatest)


df_mapfull=pd.read_excel('./assets/secop2_infra_dpto.xlsx',names=['DEPARTAMENTO','COD_DPTO','N_COUNT','COUNT'],dtype={"DEPARTAMENTO":"string","COD_DPTO":"string","N_COUNT":"int32","COUNT":"int32"})

df_mapfull = df_mapfull[['DEPARTAMENTO','COD_DPTO','COUNT','N_COUNT']]
df_mapfull['COD_DPTO']=df_mapfull['COD_DPTO'].replace({'5':'05','8':'08'})

#foo=list(df_mapfull.DEPARTAMENTO)
#op=[foo,foo]
