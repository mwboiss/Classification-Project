import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

def prep_telco(df):
    
    #This function prepares the data for exploration.
    
    # Drop duplicate columns
    drop_columns = ['internet_service_type_id',
                    'payment_type_id',
                    'contract_type_id']    
    df = df.drop(columns=drop_columns)
    
    # Drop whitespace values in total_charges
    df['total_charges'] = df['total_charges'].str.strip()
    df = df[df.total_charges != '']
    
    # Convert total_charges to the correct data type
    df['total_charges'] = df['total_charges'].astype(float)
    
    # convert categorical data that is binary in nature to numeric binary characters
    df['gender'] = df.gender.str.replace('Male', '1').str.replace('Female', '0')
    df['partner'] = df.partner.str.replace('Yes', '1').str.replace('No', '0')
    df['dependents'] = df.dependents.str.replace('Yes', '1').str.replace('No', '0')
    df['phone_service'] = df.phone_service.str.replace('Yes', '1').str.replace('No', '0')    
    df['paperless_billing'] = df.paperless_billing.str.replace('Yes', '1').str.replace('No', '0')
    df['churn'] = df.churn.str.replace('Yes', '1').str.replace('No', '0')
    df[['gender','partner','dependents','phone_service','paperless_billing','churn']] = \
                                                    df[['gender','partner','dependents',
                                                      'phone_service','paperless_billing',
                                                        'churn']].astype(int)
    
    
    # Create dummy variables for categorical variables
    dummy_name = pd.get_dummies(df[['multiple_lines',
                                    'online_security', 
                                    'online_backup',
                                    'device_protection',
                                    'tech_support',
                                    'streaming_tv',
                                    'streaming_movies',
                                    'contract_type',
                                    'payment_type',
                                    'internet_service_type']],
                                    dummy_na=False,
                                    drop_first=True)
    
    # Combine dataframes to include all variables
    df = pd.concat([df,dummy_name],axis=1)
    
    # Output cleaned DataFrame
    return df

def train_validate_test_split(df, target):
    
    '''
    Splits data into train, validate and tests sets for further processesing.
    '''
    
    train_validate, test = train_test_split(df, test_size=0.2, random_state=123, stratify=df[target])
    
    train, validate = train_test_split(train_validate, test_size=0.3, random_state=123, stratify=train_validate[target])
    
    return train, validate, test

def clean_split_telco(df, target):
    '''
     Uses both prep and split functions to fully prepare data
    '''
    cleaned_df = prep_telco(df)
    
    train, validate, test = train_validate_test_split(cleaned_df, target)
    
    return train, validate, test