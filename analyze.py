import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('password.csv', index_col='Unnamed: 0')
plt.figure(figsize=(12,12))
df['user'].value_counts()[:10].plot.pie(autopct='%1.1f%%', shadow=True)
plt.title('Top 10 username')
plt.axis('equal')
plt.savefig('top10username.png')