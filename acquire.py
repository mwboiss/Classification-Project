import pandas as pd
import os
from env import username, password, host

def get_db_url(db_name, username = username, password = password, host = host):
    '''
    This function takes in the database name (db), the host, username, and password 
    from users env file and creates a url used to a query the database using pandas
    read_sql function.
    '''
    url = f'mysql+pymysql://{username}:{password}@{host}/{db_name}'
    return url

def get_telco_data(use_cache=True):
    '''
    This function uses the create_url() funciton to retrieve the requested data and 
    returns a dataframe.
    '''
    filename = 'telco.csv'
    if os.path.exists(filename) and use_cache:
        print('Using cached csv file...')
        return pd.read_csv(filename)
    
    print('Getting a fresh copy from the database...')
    url = get_db_url('telco_churn')
    telco_data = pd.read_sql('''
    SELECT *
    FROM customers
    JOIN contract_types
    USING(contract_type_id)
    JOIN payment_types
    USING(payment_type_id)
    JOIN internet_service_types
    USING(internet_service_type_id)
    ''', url)
    
    print('Saving to csv...')
    telco_data.to_csv(filename, index=False)
    return telco_data