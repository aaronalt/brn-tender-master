import pandas as pd
import numpy as np
import datetime

date = str(datetime.date.today()).replace('-','')

def lot_data():

    sheet = 'https://docs.google.com/spreadsheets/d/152n781XHvDZGf_3qVXwEmYnOH-HQeyl-eaOq1NoOBqs/export?format=csv&id=152n781XHvDZGf_3qVXwEmYnOH-HQeyl-eaOq1NoOBqs&gid=647647855'

    csv_df = pd.read_csv(sheet, engine='python', header=0, delimiter=",", error_bad_lines=False, converters={'REF_INTERNAL':lambda x: str(x)})
    df = csv_df.replace(np.nan, '', regex=True)
    df['PRODUCT']=df['PRODUCT'].str.replace(', ','-')
    df['LOT_DESCRIPTION']=df['LOT_DESCRIPTION'].str.replace(',',' ').str.lstrip()
    df['LOT_DESCRIPTION_ORIGINAL']=df['LOT_DESCRIPTION_ORIGINAL'].str.replace(',',' ').str.lstrip()
    df['LOT_PRICE']=df['LOT_PRICE'].str.replace(',','')

    df.to_csv('brn-tender-master_lot-data.csv')
    return

def tender_details():

    sheet = 'https://docs.google.com/spreadsheets/d/152n781XHvDZGf_3qVXwEmYnOH-HQeyl-eaOq1NoOBqs/export?format=csv&id=152n781XHvDZGf_3qVXwEmYnOH-HQeyl-eaOq1NoOBqs&gid=0'

    csv_df = pd.read_csv(sheet, engine='python', header=0, delimiter=",", error_bad_lines=False, converters={'REF_INTERNAL':lambda x: str(x)})
    df = csv_df.replace(np.nan, '', regex=True)

    df['COUNTRY']=df['COUNTRY'].str.replace(',',' ')
    df['TITLE']=df['TITLE'].str.replace(',','.')
    df['ADDRESS']=df['ADDRESS'].str.replace(',',' ')
    df['TEL']="+"+df['TEL']

    df.to_csv('brn-tender-master_tender-details.csv')
    return

def ted_data():

    sheet = 'https://docs.google.com/spreadsheets/d/152n781XHvDZGf_3qVXwEmYnOH-HQeyl-eaOq1NoOBqs/export?format=csv&id=152n781XHvDZGf_3qVXwEmYnOH-HQeyl-eaOq1NoOBqs&gid=2098872239'

    df = pd.read_csv(sheet, engine='python', header=0, delimiter=",", error_bad_lines=False, converters={'Internal REF':lambda x: str(x)})

    df.to_csv('brn-tender-master_ted-data.csv')
    return

lot_data()
tender_details()
ted_data()