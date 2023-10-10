import pandas as pd

def get_unified_data():
    data = pd.read_csv('data/unified.csv', encoding='utf-8')
    
    # add field full name:
    data['שם מלא'] = data['שם'] + ' ' + data['שם משפחה']
    
    # fill na with empty string
    data = data.fillna('')
    
    return data


    
    
    