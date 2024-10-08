import pandas as pd

# Load the CSV file into a DataFrame
file_path_1 = '/Users/edocampione/Desktop/Meng Engineering Science/4YP/data/ExxonMobil_CRSP_daily_data_2010_2014.csv' # Daily technical data (CRSP)
file_path_2 = '/Users/edocampione/Desktop/Meng Engineering Science/4YP/data/ExxonMobil_Compustat_q_data_2010_2014.csv' # Fundamental data (Compustat)
file_path_3 = '/Users/edocampione/Desktop/Meng Engineering Science/4YP/data/ExxonMobil_Compustat_quarterly_ratiodata_2010_2014.csv' # Fundamental ratios (Compustat)

df1 = pd.read_csv(file_path_1)
df2 = pd.read_csv(file_path_2)
df3 = pd.read_csv(file_path_3)

#Convert date columns to datetime format
df1['date'] = pd.to_datetime(df1['date'])  # CRSP daily data
df2['datadate'] = pd.to_datetime(df2['datadate'])  # Fundamental data
df3['qdate'] = pd.to_datetime(df3['qdate'])  # Financial ratios data

# Sort by qdate and public_date to ensure the most recent public_date comes last
df3_sorted = df3.sort_values(by=['qdate', 'public_date'])

# Drop duplicates to keep only the latest public_date for each qdate
df3_latest = df3_sorted.drop_duplicates(subset='qdate', keep='last')

# First merge daily technical data (df1) with fundamental data (df2)
# Merge on the nearest quarter date for Exxon
df_combined_1_2 = pd.merge_asof(
    df1,  # Daily data sorted by date
    df2,  # Fundamental data sorted by quarterly date
    left_on='date', right_on='datadate',  # Merge on dates
    direction='backward'  # Merge to the closest past quarter
)

# Now merge with the cleaned financial ratios (df3_latest)
df_combined_all = pd.merge_asof(
    df_combined_1_2.sort_values('date'),  # Combined data sorted by date
    df3_latest.sort_values('qdate'),  # Financial ratios sorted by quarterly date
    left_on='date', right_on='qdate',  # Merge on dates
    direction='backward'  # Merge to the closest past quarter
)

# Filter the DataFrame to remove unnecessary/repeated collumns
columns_to_keep = [
    'date', 'BIDLO', 'ASKHI', 
    'PRC', 'VOL', 'RET', 'OPENPRC', 
    'epsfxq', 'ltq', 'niq', 'revtq', 
    'capxy', 'npm', 'de_ratio', 'curr_ratio', 'ptb'
]
df_filtered = df_combined_all[columns_to_keep]

# Add price moving average collumns
df_filtered['MA_5'] = df_filtered['PRC'].rolling(window=5).mean()
df_filtered['MA_20'] = df_filtered['PRC'].rolling(window=20).mean()
df_filtered['MA_5'] = df_filtered['MA_5'].fillna(df_filtered['PRC'].expanding().mean())
df_filtered['MA_20'] = df_filtered['MA_20'].fillna(df_filtered['PRC'].expanding().mean()) # Replace NaN values with the average of available values up to that point


#df_filtered.to_csv('filtered_exxon_data.csv', index=False)