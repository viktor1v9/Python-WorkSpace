import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"c:\Users\victo\Downloads\Most Streamed Spotify Songs 2024.xlsx", sheet_name="Most Streamed Spotify Songs 202")

dfPopularidade = df.groupby('Artist')['Spotify Popularity'].mean().reset_index()
top30 = dfPopularidade.sort_values(by='Spotify Popularity', ascending=False).head(30)

print(dfPopularidade)

sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))
sns.barplot(data=top30, x='Spotify Popularity', y='Artist', palette='viridis')

plt.title("Média de Popularidade no Spotify por Artista")
plt.xlabel("Média de Popularidade")
plt.ylabel("Artista")
plt.show()