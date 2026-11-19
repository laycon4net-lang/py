import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('Titanic Dataset.csv')
data.head(5)
sns.countplot(data=data, x='Gender', hue='Survived')
plt.title("Survival by Gender")
plt.show()
sns.countplot(data=data, x='Pclass', hue='Survived')
plt.title("Survival by passenger Class")
plt.show()
sns.histplot(data['Age'], bins=40, kde=False)
plt.title("Distribution of passenger Age")
plt.xlabel("Age")
plt.ylabel("Number of passengers")
plt.show()
sns.countplot(data=data, x='Gender')
plt.title("passengers by gender")
plt.show()
sns.countplot(
    data=data,
    x='Survived',
    hue='Sibsp',
    palette="mako"
)
plt.title("Survival by Number of parents/children")
plt.show()
sns.histlot(data['Fare'], kde=True)