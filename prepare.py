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
                                    dummy_na=False)
    
    # Combine dataframes to include all variables
    
    df = pd.concat([df,dummy_name],axis=1)
    
    # Rename columns to remove spaces
    
    df = df.rename(columns = {'contract_type_One year' : 'contract_type_One_year', 
                     'contract_type_Two year' : 'contract_type_Two_year', 
                     'payment_type_Bank transfer (automatic)' : 'payment_type_Bank_transfer_(automatic)', 
                     'payment_type_Credit card (automatic)' : 'payment_type_Credit_card_(automatic)', 
                     'payment_type_Electronic check' : 'payment_type_Electronic_check', 
                     'payment_type_Mailed check' : 'payment_type_Mailed_check', 
                     'multiple_lines_No phone service' : 'multiple_lines_No_phone_service', 
                     'online_security_No internet service' : 'online_security_No_internet_service', 
                     'online_backup_No internet service' : 'online_backup_No_internet_service', 
                     'device_protection_No internet service' : 'device_protection_No_internet_service', 
                     'tech_support_No internet service' : 'tech_support_No_internet_service', 
                     'streaming_tv_No internet service' : 'streaming_tv_No_internet_service', 
                     'streaming_movies_No internet service' : 'streaming_movies_No_internet_service', 
                     'internet_service_type_Fiber optic': 'internet_service_type_Fiber_optic'})
    
    # Create a column that gives a count of additional services for each customer
    
    df['service_count'] = (df[['online_security_Yes', 'online_backup_Yes','device_protection_Yes', 
                               'tech_support_Yes', 'streaming_tv_Yes', 'streaming_movies_Yes']] == 1).sum(axis=1)
    
    # Output cleaned DataFrame
    
    return df

def train_validate_test_split(df, target):
    
    # Splits data into train, validate and tests sets for further processesing. Use target variable to stratify data to ensure class frequencies. 
    
    train_validate, test = train_test_split(df, test_size=0.2, random_state=123, stratify=df[target])
    
    train, validate = train_test_split(train_validate, test_size=0.3, random_state=123, stratify=train_validate[target])
    
    # Returns the split data with train making up 56% of the data, validate making up 24% of the data and test representing the remaining 20%
    
    return train, validate, test

def clean_split_telco(df, target):
    
    # Uses both prep and split functions to fully prepare data
    
    cleaned_df = prep_telco(df)
    
    train, validate, test = train_validate_test_split(cleaned_df, target)
    
    # Returns the fully preped data for further analysis
    
    return train, validate, test

def model_split_telco(df):
    
    # This removes non numeric data
    
    mod_split = df[df.columns[df.dtypes != 'object']]
    
    # This removes the target variable to create the x dataset for model training
    
    x = mod_split.drop(columns=['churn'])
    
    # This removes everything but the target variable to great the y dataset for model training
    
    y = mod_split.churn
    
    # Returns datasets needed to test models
    
    return x, y
