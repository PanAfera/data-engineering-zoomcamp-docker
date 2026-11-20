import sys
import pandas as pd


month = int(sys.argv[1])

df = pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})
df["month"] = month
print(df.head())

parquet_df = df.to_parquet(f"data_{month}.parquet", index=False)
print(parquet_df)
print(f"Hello pipeline! The month is {month}.")