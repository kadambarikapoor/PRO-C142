import pandas as pd

df = pd.read_csv('articles.csv')
df = df.sort_values('total_events', ascending = False)
output = df.head(20).values.tolist()
print(output)