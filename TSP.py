import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('Titanic Dataset.csv')
data.head(5)
minimum_age = data['Age'].min()
print('Minium Age :', minimum_age)
maximum_age = data['Age'].max()
print('Maximum Age :', maximum_age)
bins = [0, 15, 30, 45, 60, 75]
data['binned_age'] = pd.cut(data['Age'], bins)
print(data[['binned_age', 'Age']].head())
age_labels = ['Young', 'Young - Adult', 'Middle Aged', 'Middleolder Age',
'Senior']
data['binned_age'] = pd.cut(data['Age'], bins, labels = age_labels)
data['binned_age'].value_counts().plot(kind='bar')
plt.title('Dance Class Age Distribution')
plt.xlabel('Ages')
plt.ylabel('count')
labels = ['PassengerId','Survived','Pclass','Age','SibSp','Parch','Fare']
for label in labels:
 print('Distribution of', label)
 sns.distplot(data[label])
 plt.show()
 print('Skewness -', data[label].skew())
data['log_Sibsp'] = np.log(data['Sibsp'])
data['log_parch'] = np.log(data['parch'])
data['log_Fare'] = np.log(data['Fare'])


