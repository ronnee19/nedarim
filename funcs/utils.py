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

# function to upload file to google drive asa google sheets
def upload_file_to_google_drive(df : pd.DataFrame):
    file_metadata = {
        'name': 'unified',
        'mimeType': 'application/vnd.google-apps.spreadsheet'
    }
    media = MediaFileUpload('data/unified.csv', mimetype='text/csv')
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return file.get('id')


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


    
    
    