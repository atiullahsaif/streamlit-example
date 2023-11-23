import streamlit as st
import rasterio
import numpy as np

# Streamlit app setup
st.title('Weighted Overlay Analysis')

# File uploader for raster layers
uploaded_files = st.file_uploader("Upload your raster layers:", accept_multiple_files=True, type=['tif'])

# User input for weights
weights = []
for file in uploaded_files:
    weight = st.slider(f"Set weight for {file.name}:", 0.0, 1.0)
    weights.append(weight)

# Perform weighted overlay analysis (simplified example using numpy)
if st.button('Perform Overlay'):
    # Read raster data
    raster_data = [rasterio.open(file) for file in uploaded_files]
    
    # Read and process raster data with weights
    weighted_arrays = [r.read(1) * weight for r, weight in zip(raster_data, weights)]
    
    # Calculate the weighted sum
    result_array = np.sum(weighted_arrays, axis=0)
    
    # Display the resulting raster map (simplified example)
    st.image(result_array, caption='Weighted Overlay Result', use_column_width=True)
