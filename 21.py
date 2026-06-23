import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', "Matthew", 'Laura', 'kevin', 'Jonas'],
'score': [45.5, 9, 35.5, np.nan, 9, 36, 22.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'no', 'no', 'yes', 'no' ]}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data , index=labels)
print("summary of the basic informmation about this DataFrame and its data:")
print(df.info())
