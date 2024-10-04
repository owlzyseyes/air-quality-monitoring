import pandas as pd
import geopandas as gpd

#load the data from the csv file
df = pd.read_csv('data/computed_stats/african_countries_no2_monthly.csv')

#function to clean the data
def clean_data(df):
    # Drop column: 'abbreviati'
    df = df.drop(columns=['abbreviati'])
    # Drop column: 'wld_rgn'
    df = df.drop(columns=['wld_rgn'])
    return df

df_clean = clean_data(df)

#export the data as a csv file
df_clean.to_csv('data/computed_stats/no2_africa_cleaned.csv', index=False)
