import pandas as pd
data = {
    'Name': ['Adi', 'Bobby', 'Candy', 'Oggy', 'Isa'],
    'Age': [20, 21, 19, 22, 20],
    'Marks': [85, 90, 75, 95, 88]
}
df = pd.DataFrame(data)
print("First 3 rows:",df.head(3))
print("Name column:",df['Name'])
print("Rows where Marks > 85:")
print(df[df['Marks'] > 85])
df['Grade'] = ['B', 'A', 'C', 'A', 'B']
print("DataFrame with Grade column:",df['Grade'])
df_dropped = df.drop('Age', axis=1)
print("DataFrame after dropping Age column:",df_dropped)
