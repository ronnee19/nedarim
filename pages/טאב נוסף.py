# # streamlit_app.py

# import streamlit as st
# from streamlit_gsheets import GSheetsConnection

# # Create a connection object.
# conn = st.experimental_connection("gsheets", type=GSheetsConnection)

# df = conn.read()

# # Print results.
# for row in df.itertuples():
#     st.write(f"{row.name} has a :{row.pet}:")

# print all the installed packages with their versions
print(pip freeze)