import streamlit as st
import pandas as pd
# from googleapiclient.discovery import build
# from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
# from google.oauth2 import service_account


# SERVICE_ACCOUNT_FILE = 'project_key.json'
# FILE_ID = '1qjZbjZFKagBDH-DG_HKdOmj7WU5R9xX3ZeE87flPHNw'
# SCOPES = ['https://www.googleapis.com/auth/drive']
# credentials = service_account.Credentials.from_service_account_file(
#     SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# drive_service = build('drive', 'v3', credentials=credentials)

# def download_and_export_csv(file_id):
#     request = drive_service.files().export_media(fileId=file_id, mimeType='text/csv')
#     fh = io.BytesIO()
#     downloader = MediaIoBaseDownload(fh, request)
#     done = False
#     while not done:
#         status, done = downloader.next_chunk()
#     return fh.getvalue().decode('utf-8')

# # function to upload file to google drive
# def upload_file_to_google_drive(file_name, file_path, folder_id=None):
#     file_metadata = {
#         'name': file_name,
#         'parents': [folder_id]
#     }
#     media = MediaFileUpload(file_path, mimetype='text/csv')
#     file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
#     return file.get('id')

# # Download the Google Sheets file and export it as CSV
# st.write('Downloading and exporting file...')
# csv_data = download_and_export_csv(FILE_ID)
# st.success('File downloaded and exported.')

# # Read the CSV data
# df = pd.read_csv(io.StringIO(csv_data))
# edited_df = st.dataframe(df)



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


st.title('מילוי מידע נעדר קיים')

# c1, c2 = st.columns(2)

full_name = st.selectbox(label='בחר שם', options=st.session_state['uni_data']["שם מלא"])
# c2.button('הצג פרטים')

st.subheader('פרטים אישיים')

filled_info, not_filled_info = st.tabs(['מידע קיים', 'מידע חסר'])

idx = st.session_state['uni_data'][st.session_state['uni_data']['שם מלא'] == full_name].index[0]

def saveToState():
    for i in st.session_state['uni_data'].columns:
        if st.session_state['uni_data'].loc[idx, i] != '':
            st.session_state['uni_data'].loc[idx, i] = st.session_state[i]

with filled_info:
    for i in st.session_state['uni_data'].columns:
        if st.session_state['uni_data'].loc[idx, i] != '':
            input_value = st.session_state['uni_data'].loc[idx, i]
            user_input = st.text_input(i, input_value, key=i)

    st.button("שמירה", on_click=saveToState, key="save_filled")
    
with not_filled_info:
    for i in st.session_state['uni_data'].columns:
        if st.session_state['uni_data'].loc[idx, i] == '':
            input_value = st.session_state['uni_data'].loc[idx, i]
            user_input = st.text_input(i, input_value, key=i)

    st.button("שמירה", on_click=saveToState, key="save_unfilled")