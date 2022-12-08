import h5py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### https://anthonylouisdagostino.com/bounding-boxes-for-all-us-states/
### ==> x = longitude
### ==> y = latitude

#################################################
### Alabama
#################################################
### xmin	    ymin	    xmax	    ymax
### -88.473227	30.223334	-84.88908	35.008028
#################################################
AL_LAT_MIN_INDEX = 1201
AL_LAT_MAX_INDEX = 1250
AL_LON_MIN_INDEX = 914
AL_LON_MAX_INDEX = 951

#################################################
### Arkansas
#################################################
### xmin	    ymin	    xmax	    ymax
### -94.617919	33.004106	-89.644395	36.4996
#################################################
AK_LAT_MIN_INDEX = 1229
AK_LAT_MAX_INDEX = 1265
AK_LON_MIN_INDEX = 853
AK_LON_MAX_INDEX = 904

#################################################
### Florida
#################################################
### xmin	    ymin	    xmax	    ymax
### -87.634938	24.523096	-80.031362	31.000888
#################################################
FL_LAT_MIN_INDEX = 1144
FL_LAT_MAX_INDEX = 1210
FL_LON_MIN_INDEX = 923
FL_LON_MAX_INDEX = 1000

#################################################
### Georgia
#################################################
### xmin	    ymin	    xmax	    ymax
### -85.605165	30.357851	-80.839729	35.000659
#################################################
GA_LAT_MIN_INDEX = 1203
GA_LAT_MAX_INDEX = 1250
GA_LON_MIN_INDEX = 943
GA_LON_MAX_INDEX = 992

#################################################
### Kentucky
#################################################
### xmin	    ymin	    xmax	    ymax
### -89.571509	36.497129	-81.964971	39.147458
#################################################
KY_LAT_MIN_INDEX = 1264
KY_LAT_MAX_INDEX = 1291
KY_LON_MIN_INDEX = 903
KY_LON_MAX_INDEX = 980

#################################################
### Louisiana
#################################################
### xmin	    ymin	    xmax	    ymax
### -94.043147	28.928609	-88.817017	33.019457
#################################################
LA_LAT_MIN_INDEX = 1188
LA_LAT_MAX_INDEX = 1230
LA_LON_MIN_INDEX = 860
LA_LON_MAX_INDEX = 912

#################################################
### Mississippi
#################################################
### xmin	    ymin	    xmax	    ymax
### -91.655009	30.173943	-88.097888	34.996052
#################################################
MS_LAT_MIN_INDEX = 1201
MS_LAT_MAX_INDEX = 1250
MS_LON_MIN_INDEX = 882
MS_LON_MAX_INDEX = 919

#################################################
### North Carolina
#################################################
### xmin	    ymin	    xmax	    ymax
### -84.321869	33.842316	-75.460621	36.588117
#################################################
NC_LAT_MIN_INDEX = 1237
NC_LAT_MAX_INDEX = 1266
NC_LON_MIN_INDEX = 956
NC_LON_MAX_INDEX = 1045

#################################################
### South Carolina
#################################################
### xmin	    ymin	    xmax	    ymax
### -83.35391	32.0346	-78.54203	35.215402
#################################################
SC_LAT_MIN_INDEX = 1219
SC_LAT_MAX_INDEX = 1252
SC_LON_MIN_INDEX = 965
SC_LON_MAX_INDEX = 1015

#################################################
### Tennessee
#################################################
### xmin	    ymin	    xmax	    ymax
### -90.310298	34.982972	-81.6469	36.678118
#################################################
TN_LAT_MIN_INDEX = 1249
TN_LAT_MAX_INDEX = 1267
TN_LON_MIN_INDEX = 896
TN_LON_MAX_INDEX = 984

jan_2020 = h5py.File("GPM/3B-MO.MS.MRG.3IMERG.20200101-S000000-E235959.01.V06B.HDF5", mode="r")
feb_2020 = h5py.File("GPM/3B-MO.MS.MRG.3IMERG.20200201-S000000-E235959.02.V06B.HDF5", mode="r")
mar_2020 = h5py.File("GPM/3B-MO.MS.MRG.3IMERG.20200301-S000000-E235959.03.V06B.HDF5", mode="r")
apr_2020 = h5py.File("GPM/3B-MO.MS.MRG.3IMERG.20200401-S000000-E235959.04.V06B.HDF5", mode="r")
may_2020 = h5py.File("GPM/3B-MO.MS.MRG.3IMERG.20200501-S000000-E235959.05.V06B.HDF5", mode="r")
jun_2020 = h5py.File("GPM/3B-MO.MS.MRG.3IMERG.20200601-S000000-E235959.06.V06B.HDF5", mode="r")
jul_2020 = h5py.File("GPM/3B-MO.MS.MRG.3IMERG.20200701-S000000-E235959.07.V06B.HDF5", mode="r")
aug_2020 = h5py.File("GPM/3B-MO.MS.MRG.3IMERG.20200801-S000000-E235959.08.V06B.HDF5", mode="r")
sep_2020 = h5py.File("GPM/3B-MO.MS.MRG.3IMERG.20200901-S000000-E235959.09.V06B.HDF5", mode="r")
oct_2020 = h5py.File("GPM/3B-MO.MS.MRG.3IMERG.20201001-S000000-E235959.10.V06B.HDF5", mode="r")
nov_2020 = h5py.File("GPM/3B-MO.MS.MRG.3IMERG.20201101-S000000-E235959.11.V06B.HDF5", mode="r")
dec_2020 = h5py.File("GPM/3B-MO.MS.MRG.3IMERG.20201201-S000000-E235959.12.V06B.HDF5", mode="r")

grid_grp_jan_2020 = jan_2020["Grid"]
grid_grp_feb_2020 = feb_2020["Grid"]
grid_grp_mar_2020 = mar_2020["Grid"]
grid_grp_apr_2020 = apr_2020["Grid"]
grid_grp_may_2020 = may_2020["Grid"]
grid_grp_jun_2020 = jun_2020["Grid"]
grid_grp_jul_2020 = jul_2020["Grid"]
grid_grp_aug_2020 = aug_2020["Grid"]
grid_grp_sep_2020 = sep_2020["Grid"]
grid_grp_oct_2020 = oct_2020["Grid"]
grid_grp_nov_2020 = nov_2020["Grid"]
grid_grp_dec_2020 = dec_2020["Grid"]

# print(list(grid_grp.keys()))

# for k in grid_grp:
#     h5obj = grid_grp[k]
#     print(f"{k}: {h5obj}")

precip_jan_2020 = grid_grp_jan_2020["precipitation"]
precip_jan_2020 = np.flip(precip_jan_2020[0,:,:].transpose(), axis=0)

precip_feb_2020 = grid_grp_feb_2020["precipitation"]
precip_feb_2020 = np.flip(precip_feb_2020[0,:,:].transpose(), axis=0)

precip_mar_2020 = grid_grp_mar_2020["precipitation"]
precip_mar_2020 = np.flip(precip_mar_2020[0,:,:].transpose(), axis=0)

precip_apr_2020 = grid_grp_apr_2020["precipitation"]
precip_apr_2020 = np.flip(precip_apr_2020[0,:,:].transpose(), axis=0)

precip_may_2020 = grid_grp_may_2020["precipitation"]
precip_may_2020 = np.flip(precip_may_2020[0,:,:].transpose(), axis=0)

precip_jun_2020 = grid_grp_jun_2020["precipitation"]
precip_jun_2020 = np.flip(precip_jun_2020[0,:,:].transpose(), axis=0)

precip_jul_2020 = grid_grp_jul_2020["precipitation"]
precip_jul_2020 = np.flip(precip_jul_2020[0,:,:].transpose(), axis=0)

precip_aug_2020 = grid_grp_aug_2020["precipitation"]
precip_aug_2020 = np.flip(precip_aug_2020[0,:,:].transpose(), axis=0)

precip_sep_2020 = grid_grp_sep_2020["precipitation"]
precip_sep_2020 = np.flip(precip_sep_2020[0,:,:].transpose(), axis=0)

precip_oct_2020 = grid_grp_oct_2020["precipitation"]
precip_oct_2020 = np.flip(precip_oct_2020[0,:,:].transpose(), axis=0)

precip_nov_2020 = grid_grp_nov_2020["precipitation"]
precip_nov_2020 = np.flip(precip_nov_2020[0,:,:].transpose(), axis=0)

precip_dec_2020 = grid_grp_dec_2020["precipitation"]
precip_dec_2020 = np.flip(precip_dec_2020[0,:,:].transpose(), axis=0)

lon = grid_grp_jan_2020["lon"]
lat = grid_grp_jan_2020["lat"]

df_lon = pd.DataFrame(lon)
df_lon.to_csv("data/lon.csv")

df_lat = pd.DataFrame(lat)
df_lat.to_csv("data/lat.csv")

months = {
    "jan": precip_jan_2020,
    "feb": precip_feb_2020,
    "mar": precip_mar_2020,
    "apr": precip_apr_2020,
    "may": precip_may_2020,
    "jun": precip_jun_2020,
    "jul": precip_jul_2020,
    "aug": precip_aug_2020,
    "sep": precip_sep_2020,
    "oct": precip_oct_2020,
    "nov": precip_nov_2020,
    "dec": precip_dec_2020
}

def create_precipitation_data_per_state(month):
    precip = months[month]
    df_precipitation = pd.DataFrame(precip)
    alabama = df_precipitation.iloc[AL_LAT_MIN_INDEX:AL_LAT_MAX_INDEX+1,AL_LON_MIN_INDEX:AL_LON_MAX_INDEX+1]
    arkansas = df_precipitation.iloc[AK_LAT_MIN_INDEX:AK_LAT_MAX_INDEX+1,AK_LON_MIN_INDEX:AK_LON_MAX_INDEX+1]
    florida = df_precipitation.iloc[FL_LAT_MIN_INDEX:FL_LAT_MAX_INDEX+1,FL_LON_MIN_INDEX:FL_LON_MAX_INDEX+1]
    georgia = df_precipitation.iloc[GA_LAT_MIN_INDEX:GA_LAT_MAX_INDEX+1,GA_LON_MIN_INDEX:GA_LON_MAX_INDEX+1]
    kentucky = df_precipitation.iloc[KY_LAT_MIN_INDEX:KY_LAT_MAX_INDEX+1,KY_LON_MIN_INDEX:KY_LON_MAX_INDEX+1]
    louisiana = df_precipitation.iloc[LA_LAT_MIN_INDEX:LA_LAT_MAX_INDEX+1,LA_LON_MIN_INDEX:LA_LON_MAX_INDEX+1]
    mississippi = df_precipitation.iloc[MS_LAT_MIN_INDEX:MS_LAT_MAX_INDEX+1,MS_LON_MIN_INDEX:MS_LON_MAX_INDEX+1]
    north_carolina = df_precipitation.iloc[NC_LAT_MIN_INDEX:NC_LAT_MAX_INDEX+1,NC_LON_MIN_INDEX:NC_LON_MAX_INDEX+1]
    south_carolina = df_precipitation.iloc[SC_LAT_MIN_INDEX:SC_LAT_MAX_INDEX+1,SC_LON_MIN_INDEX:SC_LON_MAX_INDEX+1]
    tennessee = df_precipitation.iloc[TN_LAT_MIN_INDEX:TN_LAT_MAX_INDEX+1,TN_LON_MIN_INDEX:TN_LON_MAX_INDEX+1]

    nrow = df_precipitation.shape[0]
    ncol = df_precipitation.shape[1]

    alabama_new = pd.DataFrame(index=range(alabama.shape[0] * alabama.shape[1]), columns=["lat_index", "latitude", "lon_index", "longitude", "state", month])
    arkansas_new = pd.DataFrame(index=range(arkansas.shape[0] * arkansas.shape[1]), columns=["lat_index", "latitude", "lon_index", "longitude", "state", month])
    florida_new = pd.DataFrame(index=range(florida.shape[0] * florida.shape[1]), columns=["lat_index", "latitude", "lon_index", "longitude", "state", month])
    georgia_new = pd.DataFrame(index=range(georgia.shape[0] * georgia.shape[1]), columns=["lat_index", "latitude", "lon_index", "longitude", "state", month])
    kentucky_new = pd.DataFrame(index=range(kentucky.shape[0] * kentucky.shape[1]), columns=["lat_index", "latitude", "lon_index", "longitude", "state", month])
    louisiana_new = pd.DataFrame(index=range(louisiana.shape[0] * louisiana.shape[1]), columns=["lat_index", "latitude", "lon_index", "longitude", "state", month])
    mississippi_new = pd.DataFrame(index=range(mississippi.shape[0] * mississippi.shape[1]), columns=["lat_index", "latitude", "lon_index", "longitude", "state", month])
    north_carolina_new = pd.DataFrame(index=range(north_carolina.shape[0] * north_carolina.shape[1]), columns=["lat_index", "latitude", "lon_index", "longitude", "state", month])
    south_carolina_new = pd.DataFrame(index=range(south_carolina.shape[0] * south_carolina.shape[1]), columns=["lat_index", "latitude", "lon_index", "longitude", "state", month])
    tennessee_new = pd.DataFrame(index=range(tennessee.shape[0] * tennessee.shape[1]), columns=["lat_index", "latitude", "lon_index", "longitude", "state", month])

    southeast_states_df = {
        "Alabama": [alabama, alabama_new],
        "Arkansas": [arkansas, arkansas_new],
        "Florida": [florida, florida_new],
        "Georgia": [georgia, georgia_new],
        "Kentucky": [kentucky, kentucky_new],
        "Louisiana": [louisiana, louisiana_new],
        "Mississippi": [mississippi, mississippi_new],
        "North Carolina": [north_carolina, north_carolina_new],
        "South Carolina": [south_carolina, south_carolina_new],
        "Tennessee": [tennessee, tennessee_new]
    }

    southeast_states = {
        "Alabama": [AL_LAT_MIN_INDEX, AL_LAT_MAX_INDEX, AL_LON_MIN_INDEX, AL_LON_MAX_INDEX],
        "Arkansas": [AK_LAT_MIN_INDEX, AK_LAT_MAX_INDEX, AK_LON_MIN_INDEX, AK_LON_MAX_INDEX],
        "Florida": [FL_LAT_MIN_INDEX, FL_LAT_MAX_INDEX, FL_LON_MIN_INDEX, FL_LON_MAX_INDEX],
        "Georgia": [GA_LAT_MIN_INDEX, GA_LAT_MAX_INDEX, GA_LON_MIN_INDEX, GA_LON_MAX_INDEX],
        "Kentucky": [KY_LAT_MIN_INDEX, KY_LAT_MAX_INDEX, KY_LON_MIN_INDEX, KY_LON_MAX_INDEX],
        "Louisiana": [LA_LAT_MIN_INDEX, LA_LAT_MAX_INDEX, LA_LON_MIN_INDEX, LA_LON_MAX_INDEX],
        "Mississippi": [MS_LAT_MIN_INDEX, MS_LAT_MAX_INDEX, MS_LON_MIN_INDEX, MS_LON_MAX_INDEX],
        "North Carolina": [NC_LAT_MIN_INDEX, NC_LAT_MAX_INDEX, NC_LON_MIN_INDEX, NC_LON_MAX_INDEX],
        "South Carolina": [SC_LAT_MIN_INDEX, SC_LAT_MAX_INDEX, SC_LON_MIN_INDEX, SC_LON_MAX_INDEX],
        "Tennessee": [TN_LAT_MIN_INDEX, TN_LAT_MAX_INDEX, TN_LON_MIN_INDEX, TN_LON_MAX_INDEX]
    }

    for state in southeast_states:
        index = 0
        indices = southeast_states[state]
        df_precipitation = southeast_states_df[state][0]
        df_precipitation_new = southeast_states_df[state][1]
        for i in range(indices[0], indices[1]+1):
            for j in range(indices[2], indices[3]+1):
                df_precipitation_new.iloc[index]["lat_index"] = i
                df_precipitation_new.iloc[index]["lon_index"] = j

                latitude = df_lat.iloc[i][0]
                longitude = df_lon.iloc[j][0]
            
                df_precipitation_new.iloc[index]["latitude"] = latitude
                df_precipitation_new.iloc[index]["longitude"] = longitude
                df_precipitation_new.iloc[index][month] = df_precipitation.iloc[i - indices[0]][j]
                df_precipitation_new.iloc[index]["state"] = state

                index += 1

        df_precipitation_new.to_csv("data/" + state + "/" + month + ".csv")

for month in months:
    create_precipitation_data_per_state(month)

states_new_df = {
    "Alabama": None,
    "Arkansas": None,
    "Florida": None,
    "Georgia": None,
    "Kentucky": None,
    "Louisiana": None,
    "Mississippi": None,
    "North Carolina": None,
    "South Carolina": None,
    "Tennessee": None
}

def create_precipitation_data_final():
    for state in states_new_df:
        states_new_df[state] = pd.read_csv("data/" + state + "/jan.csv")

        states_new_df[state]['feb'] = pd.read_csv("data/" + state + "/feb.csv")['feb']
        states_new_df[state]['mar'] = pd.read_csv("data/" + state + "/mar.csv")['mar']
        states_new_df[state]['apr'] = pd.read_csv("data/" + state + "/apr.csv")['apr']
        states_new_df[state]['may'] = pd.read_csv("data/" + state + "/may.csv")['may']
        states_new_df[state]['jun'] = pd.read_csv("data/" + state + "/jun.csv")['jun']
        states_new_df[state]['jul'] = pd.read_csv("data/" + state + "/jul.csv")['jul']
        states_new_df[state]['aug'] = pd.read_csv("data/" + state + "/aug.csv")['aug']
        states_new_df[state]['sep'] = pd.read_csv("data/" + state + "/sep.csv")['sep']
        states_new_df[state]['oct'] = pd.read_csv("data/" + state + "/oct.csv")['oct']
        states_new_df[state]['nov'] = pd.read_csv("data/" + state + "/nov.csv")['nov']
        states_new_df[state]['dec'] = pd.read_csv("data/" + state + "/dec.csv")['dec']

        states_new_df[state].to_csv("data/" + state +  "/compiled.csv")

create_precipitation_data_final()

df_precipitation = pd.concat([
    states_new_df["Alabama"],
    states_new_df["Arkansas"],
    states_new_df["Florida"],
    states_new_df["Georgia"],
    states_new_df["Kentucky"],
    states_new_df["Louisiana"],
    states_new_df["Mississippi"],
    states_new_df["North Carolina"],
    states_new_df["South Carolina"],
    states_new_df["Tennessee"]
])

df_precipitation['avg'] = df_precipitation.iloc[:,6:].mean(axis=1)
df_precipitation = df_precipitation.iloc[:,[2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]]

df_precipitation.to_csv("data/precipitation_data_final.csv")
