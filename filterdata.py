import pandas as pd

df = pd.read_csv('env_temp_change.csv')

region_name = "Brazil"

region_specific_df = df.loc[df['Area'] == region_name]

region_specific_df.to_csv(header=True)

region_specific_df.to_csv('newdata.csv',header=True)