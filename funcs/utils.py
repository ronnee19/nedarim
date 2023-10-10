import os
import io
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'project_key.json'
FILE_ID = '1qjZbjZFKagBDH-DG_HKdOmj7WU5R9xX3ZeE87flPHNw'
SCOPES = ['https://www.googleapis.com/auth/drive']
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

drive_service = build('drive', 'v3', credentials=credentials)

def download_and_process_csv():
    request = drive_service.files().export_media(fileId=FILE_ID, mimeType='text/csv')
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    f = fh.getvalue().decode('utf-8')
    f =  pd.read_csv(io.StringIO(f))
    
    # process the data
    f = process_unified_sheet(f)
    return f

# function that takes as input a pandas dataframe and uploads it to google drive as a sheet file
def upload_dataframe_to_drive(dataframe):
    """
    Uploads a Pandas DataFrame to Google Drive as a Google Sheets file with the same FILE_ID.

    :param dataframe: Pandas DataFrame to upload.
    """
    # Export the DataFrame to a temporary CSV file
    temp_csv_file = 'temp_dataframe.csv'
    dataframe.to_csv(temp_csv_file, index=False)

    # Create a media file upload request
    media_body = MediaFileUpload(temp_csv_file, mimetype='text/csv', resumable=True)

    # Update the existing file with the same FILE_ID
    drive_service.files().update(fileId=FILE_ID, media_body=media_body).execute()

    # Delete the temporary CSV file
    os.remove(temp_csv_file)




# def upload_df_to_drive(df):
#     file_name = 'unified'
#     df.to_csv(file_name, encoding='utf-8', index=False)
#     file_metadata = {
#         'name': file_name,
#         'mimeType': 'application/vnd.google-apps.spreadsheet'
#     }
#     media = MediaFileUpload(file_name,
#                             mimetype='application/vnd.google-apps.spreadsheet',
#                             resumable=True)
#     created = drive_service.files().create(body=file_metadata,
#                                            media_body=media,
#                                            fields='id').execute()
#     print('File ID: {}'.format(created.get('id')))



#### PROCESSING ####
def process_unified_sheet(df):
    # add field full name:
    df['שם מלא'] = df['שם'] + ' ' + df['שם משפחה']
    
    # fill na with empty string
    df = df.fillna('')
    
    return df


# import pandas as pd

# def get_unified_data():
#     data = pd.read_csv('data/unified.csv', encoding='utf-8')
    
#     # add field full name:
#     data['שם מלא'] = data['שם'] + ' ' + data['שם משפחה']
    
#     # fill na with empty string
#     data = data.fillna('')
    
#     return data


    
    
    