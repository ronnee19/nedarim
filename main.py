# streamlit run main.py
# make a dashboard that shows the data set

import pandas as pd
import streamlit as st
from funcs.utils import get_unified_data

st.set_page_config(layout="wide")


st.header('טבלת נעדרים')


# data = get_unified_data()

data = pd.read_csv('data/data.csv', encoding='utf-8')

# שם	שם ביניים	שם משפחה	ת.ז.	מס' דרכון	מין	גיל	אזרח/ית / חייל/ת	תמונה	צבע עיניים	צבע שיער	גובה	מבנה גוף	לבוש	סימנים על הגוף	טלפון 1 של הנעדר/ת	טלפון 2 של הנעדר/ת	מספר של מישהו נוסף שנמצא איתו	כתובת מייל של הנעדר/ת	כתובת מגורים של הנעדר/ת	שעת קשר אחרונה	מיקום אחרון	סטטוס מקורי	מקור מידע סטטוס מקורי	מופיע באתר "נעדרים"	מצב רפואי	שם המדווח	טלפון של המדווח/ת	כתובת מייל של המדווח/ת	קרבת המדווח/ת לנעדר/ת	סטטוס עדכני	מקור מידע סטטוס עדכני	תאריך עדכון אחרון	יצר קשר עם משפחה/חברים	מקור מידע	פייסבוק	אינסטגראם	טוויטר	טיקטוק	קונפליקט במידע	הערות										
# use the abot to create a table columns
if st.checkbox('Show all columns'):
    cols = data.columns
else:
    cols = ['שם', 'שם משפחה', 'ת.ז.', 'מין', 'גיל', 'אזרח/ית / חייל/ת', 'טלפון 1 של הנעדר/ת', 'שם המדווח/ת 1', 'טלפון של המדווח/ת 1']


st.table(data[cols])

# download csv button


# st.line_chart(data)

