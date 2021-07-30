import streamlit as st
import pandas as pd
import geopandas as gpd

URL_CSV = 'https://data.toulouse-metropole.fr/explore/dataset/bornes-wi-fi/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B'
df = gpd.read_file( './bornes-wi-fi.csv', sep= ';' )
#pd.read_csv( '' )

st.write( df['Geo Shape'].iloc[0] )

st.write( df )

