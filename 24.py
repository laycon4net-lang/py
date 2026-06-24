import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', "Matthew", 'Laura', 'kevin', 'Jonas'],
'studdy hours': [45.5, 9, 35.5, np.nan, 9, 36, 22.5, np.nan, 8, 19],
'score': [100, 85, 24, 93, 67, 3, 18, 87, 20, 10],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'no', 'no', 'yes', 'no' ]}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data , index=labels)
print("summary of the basic informmation about this DataFrame and its data:")
print(df.info())
