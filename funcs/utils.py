import pandas as pd

def get_unified_data():
    # import data from url
    # https://docs.google.com/spreadsheets/d/1NNCMWxn34HJM_7IcZu2tQ34MNNTInApLQiyXG-XiPPc/edit#gid=0
    import gspread
    import pandas as pd

    # Replace with the path to your JSON credentials file
    credentials_path = 'decent-seeker-300808-3d986209761c.json'

    # Authenticate using the credentials
    gc = gspread.service_account(filename=credentials_path)

    # Replace the URL with your Google Sheets URL
    sheet_url = 'https://docs.google.com/spreadsheets/d/1NNCMWxn34HJM_7IcZu2tQ34MNNTInApLQiyXG-XiPPc/edit#gid=0'

    # Open the Google Sheet by URL
    sh = gc.open_by_url(sheet_url)

    # Select the worksheet by title or index
    worksheet = sh.get_worksheet(0)  # Assuming the first sheet is used

    # Get all values from the worksheet
    data = worksheet.get_all_values()

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(data[1:], columns=data[0])  # Assuming the first row contains column headers

    # Save the DataFrame as a CSV file
    csv_file = 'data.csv'
    # df.to_csv(csv_file, index=False)
    return df
    # print(f'Data saved as {csv_file}')

    
    
    