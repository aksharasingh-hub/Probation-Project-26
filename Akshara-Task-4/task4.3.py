import pandas as pd
import numpy as np
names = ['Aarnav', 'Bella', 'Aerial', 'Diya', 'Cindy',
         'Tulip', 'Gita', 'Aamber', 'Isha', 'Jatin']
df = pd.DataFrame({
    'Name': names,
    'Maths': np.random.randint(50, 101, size=10),
    'Science': np.random.randint(50, 101, size=10),
    'English': np.random.randint(50, 101, size=10)
})
print("Original DataFrame:",df)
print("Average marks per subject:",df[['Maths', 'Science', 'English']].mean())
subject_totals = df[['Maths', 'Science', 'English']].sum(axis=1)
top_student = df.loc[subject_totals.idxmax(),'Name']
print("Student with highest total marks:",top_student)
df['Total']=df[['Maths','Science','English']].sum(axis=1)
df['Result'] = np.where(df['Total'] >= 150, 'Pass', 'Fail')
df = df.sort_values(by='Total', ascending=False).reset_index(drop=True)
print("Final DataFrame:",df)
