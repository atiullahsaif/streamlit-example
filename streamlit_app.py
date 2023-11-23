import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt

# Streamlit app setup
st.title('Weighted Overlay Analysis for CITYAM')

# Path to the shapefiles
restriction_path = r'C:\Users\saifa2\Downloads\Helsinki Geodata\restriction.shp'
parking_path = r'C:\Users\saifa2\Downloads\Helsinki Geodata\parking.shp'

# Load shapefiles
restriction = gpd.read_file(restriction_path)
parking = gpd.read_file(parking_path)

# User-defined weights
weight_restriction = 2
weight_parking = 3

# Perform weighted overlay analysis (simple example)
if st.button('Perform Overlay'):
    # Perform overlay operation (e.g., intersection, union, etc.)
    overlay_result = restriction.intersection(parking)
    
    # Apply weights
    overlay_result['weighted_score'] = overlay_result.geometry.area * (weight_restriction + weight_parking)
    
    # Display the resulting overlay map
    fig, ax = plt.subplots()
    overlay_result.plot(ax=ax, column='weighted_score', legend=True)
    st.pyplot(fig)
