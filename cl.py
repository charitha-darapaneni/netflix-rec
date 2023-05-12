import math

import pandas as pd


# splitting the years into start year and end year
df = pd.read_csv(r'C:\umkc\courses\cc\proj\netflix popular movies dataset\n_movies.csv')
# print(df)

df[['startyear', 'endyear']] = df['year'].str.split('-', expand=True)

df = df.drop('year', axis=1)
df.to_csv(r'C:\umkc\courses\cc\proj\netflix popular movies dataset\preprocessed_data.csv')

# cleaning the start year so it doesn't have any special characters
df_c = pd.read_csv(r'C:\umkc\courses\cc\proj\netflix popular movies dataset\preprocessed_data.csv')
df_c['startyear'] = df_c['startyear'].str.extract('(\d+)')
df_c.to_csv(r'C:\umkc\courses\cc\proj\netflix popular movies dataset\preprocessed_data.csv')


# converting datatype of votes
df = pd.read_csv(r'C:\umkc\courses\cc\proj\netflix popular movies dataset\preprocessed_data.csv')


def conv(value):
    if isinstance(value, str):
        return int(value.replace(',', ''))
    elif isinstance(value, float) and not math.isnan(value):
        return int(value)
    elif pd.isna(value):
        return value


df['votes'] = df['votes'].apply(conv)

df.to_csv(r'C:\umkc\courses\cc\proj\netflix popular movies dataset\preprocessed_data.csv')


# converting rating datatype into float
df = pd.read_csv(r'C:\umkc\courses\cc\proj\netflix popular movies dataset\preprocessed_data.csv')
df['rating'] = df['rating'].astype(float)

# converting duration
df['duration'] = df['duration'].str.replace('min', '').fillna(0)
df['duration'] = df['duration'].astype(int)

df['startyear'] = df['startyear'].fillna(0).astype(int)
df['endyear'] = df['endyear'].replace(' ', pd.NaT)
df['endyear'] = df['endyear'].fillna(0).astype(int)

df['votes'] = df['votes'].fillna(0).astype(int)
df['certificate'] = df['certificate'].fillna(0).astype(str)
df['title'] = df['title'].fillna(0).astype(str)
df.to_csv(r'C:\umkc\courses\cc\proj\netflix popular movies dataset\preprocessed_data.csv')



print(df['certificate'])
