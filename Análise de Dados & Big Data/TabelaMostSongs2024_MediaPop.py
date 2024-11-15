import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"c:\Users\victo\Downloads\Most Streamed Spotify Songs 2024.xlsx", sheet_name="Most Streamed Spotify Songs 202")

#contagemArtista = df['Artist'].value_counts()
#print(contagemArtista)

#Billie Eilish     5
#MUSIC LAB JPN     4
#Teddy Swims       2
#Kendrick Lamar    2
#Taylor Swift      2

artistas = ['Billie Eilish', 'MUSIC LAB JPN', 'Teddy Swims', 'Kendrick Lamar', 'Taylor Swift']

dadosPopularidade = []

for artista in artistas:
    filtroArtist = df[df['Artist'] == artista]
    mediaPopularidade = filtroArtist['Spotify Popularity'].mean()
    dadosPopularidade.append({'Artista': artista, 'Média Popularidade': mediaPopularidade})

dfPopularidade = pd.DataFrame(dadosPopularidade)    
print(dfPopularidade)

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(data=dfPopularidade, x='Artista', y='Média Popularidade', palette='viridis')
plt.title("Média de Popularidade no Spotify por Artista")
plt.xlabel("Artista")
plt.ylabel("Média de Popularidade")
plt.show()

