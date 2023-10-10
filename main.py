# streamlit run main.py
# make a dashboard that shows the data set

import pandas as pd
import streamlit as st
data = pd.DataFrame({'x': [1, 2, 3], 'y': [10, 50, 100]})
st.header('Needarim app')
st.line_chart(data)

