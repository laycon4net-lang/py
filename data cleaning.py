import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df =pd.read_csv("country_vaccinations.csv")
df.head(10)
df.isnull().any()
subset = df.iloc[:5200, :]
plt.figure(figsize=(12, 8))
sns.heatmap(subset.isnull(), cbar=False, cmap="viridis")
plt.show()
df.head(10)
df.dropna(how="all")
df.fillna(method="bfill")
df.interpolate()
df_dropped = df.dropna()
df_dropped