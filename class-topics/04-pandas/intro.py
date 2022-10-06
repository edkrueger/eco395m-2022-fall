import os

import pandas as pd

PATH = os.path.join("facebook", "reaction_counts.csv")

df = (
	pd.read_csv(PATH, parse_dates=["status_published"])
	.set_index("status_published")
)

print(df.dtypes)

print(df.columns)

series_1 = df["num_sads"]
series_2 = df["num_angrys"]

print(series_1)
print(series_2)

print(series_1 + series_2)
print(series_1 * series_2)

print(series_1.mean())
print(series_1.sum())
print(series_1.std())

print(series_1.sort_index())
print(series_1.sort_values())

print(
	df.reset_index()
	.assign(date=lambda df_: df_["status_published"].dt.date)
	.sort_values(["date", "num_sads"], ascending=[True, False])
	)

# print(series_1["2016-10-17 14:17:24"])
