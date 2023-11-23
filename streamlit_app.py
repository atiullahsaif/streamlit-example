import streamlit as st
import geopandas as gpd
import rasterio
from rasterio import features
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

# Streamlit app setup
st.title('Weighted Overlay Analysis')

# File uploader for raster layers
restriction_file = st.file_uploader("Upload 'restriction' shapefile:", type=['shp'])
parking_file = st.file_uploader("Upload 'parking' shapefile:", type=['shp'])

# Check if files are uploaded
if restriction_file and parking_file:
    # Read shapefiles
    restriction_data = gpd.read_file(restriction_file)
    parking_data = gpd.read_file(parking_file)

    # Convert shapefiles to raster (assuming a specific raster resolution)
    # Replace 'transform' and 'shape' with appropriate values based on your data
    transform = rasterio.transform.from_bounds(*restriction_data.total_bounds, width=500, height=500)
    shape = (500, 500)
    
    # Rasterize the shapefiles to create raster arrays
    restriction_raster = features.rasterize(
        [(geom, 1) for geom in restriction_data.geometry],
        out_shape=shape,
        transform=transform,
        fill=0,
        dtype='float64'
    )
    
    parking_raster = features.rasterize(
        [(geom, 1) for geom in parking_data.geometry],
        out_shape=shape,
        transform=transform,
        fill=0,
        dtype='float64'
    )

    # Apply weights
    restriction_weight = 2
    parking_weight = 3

    # Perform weighted overlay calculation
    weighted_overlay = (restriction_raster * restriction_weight) + (parking_raster * parking_weight)

    # Display the resulting overlay map
    plt.imshow(weighted_overlay, cmap='viridis')
    plt.title('Weighted Overlay Result')
    plt.colorbar(label='Overlay Value')
    plt.axis('off')

    # Show the plot in Streamlit
    st.pyplot(plt)

    # Option to download the resulting overlay map
    def download_overlay():
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        return buffer

    st.markdown("### Download Result")
    buffer = download_overlay()
    st.download_button(label="Download Overlay Map", data=buffer, file_name='weighted_overlay.png', mime='image/png')
