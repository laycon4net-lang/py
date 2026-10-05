import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
HouseDF = pd.read_csv("USA_Housing.csv")
HouseDF.head()
HouseDF.info()
HouseDF.describe()
sns.pairplot(HouseDF)
plt.figure(figsize=(8,6))
plt.show()
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm',
    linewidths=0.5
)
plt.title("Correlation Heatmap")
plt.show()


