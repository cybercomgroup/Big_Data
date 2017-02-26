import sys
import pandas as pd

df = pd.read_csv(sys.stdin)


print(df.info())
print("-----------------------------")
print(df.describe())
print("-----------------------------")
print(df.head())
