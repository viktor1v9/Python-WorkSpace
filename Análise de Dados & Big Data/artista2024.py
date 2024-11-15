import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel(r"c:\Users\victo\Downloads\Most Streamed Spotify Songs 2024.xlsx", sheet_name="Most Streamed Spotify Songs 202")

top10_artistas_2024 = df.groupby('Artist')['Spotify Streams'].sum().nlargest(10).reset_index()

sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))

sns.barplot(data=top10_artistas_2024, x='Artist', y='Spotify Streams', palette='viridis')

plt.title("Top 10 Artistas de 2024 por Spotify Streams")
plt.xlabel("Artistas")
plt.ylabel("Spotify Streams")

plt.xticks(rotation=45, ha='right', fontsize=10)

for index, value in enumerate(top10_artistas_2024['Spotify Streams']):
    plt.text(index, value, f"{int(value):,}", ha='center', va='bottom', fontsize=9)

#plt.savefig(r"c:\Users\victo\Downloads\top10Artistas2024_SpotifyStreams.png", format='png', dpi=300, bbox_inches='tight')

plt.show()



