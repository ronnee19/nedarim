# streamlit run main.py
# make a dashboard that shows the data set

import pandas as pd
import streamlit as st
from funcs.utils import download_and_process_csv

# st.set_page_config(layout="wide")
st.markdown("""
<style>
body {
  unicode-bidi:bidi-override;
  direction: RTL;
}
[data-testid=column] [data-testid=stVerticalBlock]{
    height: 20px;
}
</style>
    """, unsafe_allow_html=True)

st.header('טבלת נעדרים')


# data = get_unified_data()

st.session_state['uni_data'] = download_and_process_csv()

# use the abot to create a tab  le columns
if st.checkbox('הצג את כל העמודות'):
    cols = st.session_state['uni_data'].columns
else:
    cols = ['שם', 'שם משפחה', 'ת.ז.', 'מין', 'גיל', 'אזרח/ית / חייל/ת', 'טלפון 1 של הנעדר/ת', 'שם המדווח/ת 1', 'טלפון של המדווח/ת 1']

# write the table in the center of the page
st.write(st.session_state['uni_data'][cols])


# download csv button


# st.line_chart(data)

