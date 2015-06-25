import pandas as pd


def clean_loan_data():
    df = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

    # Clean data and engineer features
    df['Interest.Rate'] = df['Interest.Rate'].apply(lambda x: float(x[:-1]))
    find_mid = lambda x: (float(x[:3]) + float(x[-3:])) / 2
    df['FICO.Score'] = df['FICO.Range'].apply(find_mid)
    
    return df

