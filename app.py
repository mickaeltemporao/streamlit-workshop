import streamlit as st
import numpy as np

"""
# Let's play again
"""

st.write('test')

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
