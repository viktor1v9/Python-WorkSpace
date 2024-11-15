import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"c:\Users\victo\Downloads\Copy of hot-100-current.xlsx", sheet_name="a4dc5967-378c-4e8f-83ef-99f0445")


contagem_artistas = df['artistName'].value_counts()
proporcao_artistas = df['artistName'].value_counts(normalize=True) * 100


tabelaArtistas = pd.DataFrame({
    'artistName': contagem_artistas.index,
    'Contagem de Músicas': contagem_artistas.values,
    'Proporção de Músicas (%)': proporcao_artistas.values
})


print(tabelaArtistas)

top50Artistas = tabelaArtistas.sort_values(by='Proporção de Músicas (%)', ascending=False).head(50)
sns.set(style="whitegrid")
plt.figure(figsize=(12, 10))
sns.barplot(data=top50Artistas, x='Proporção de Músicas (%)', y='artistName', palette='viridis')

plt.title("Top 50 Artistas - Proporção de Músicas no Hot 100")
plt.xlabel("Proporção de Músicas (%)")
plt.ylabel("Artista")
plt.savefig(r"c:\Users\victo\Downloads\top50Artistas_proporcao.png", format= 'png', dpi=300, bbox_inches='tight' )
plt.show()

