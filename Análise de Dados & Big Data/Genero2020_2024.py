import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"c:\Users\victo\Downloads\spotifyDBIntegrada.xlsx", sheet_name="a4dc5967-378c-4e8f-83ef-99f0445")

df['chartWeek'] = pd.to_datetime(df['chartWeek'], dayfirst=True, errors='coerce')


df_2020_2024 = df[(df['chartWeek'].dt.year >= 2020) & (df['chartWeek'].dt.year <= 2024)]


generoContagem = df_2020_2024['musicGenre'].value_counts().reset_index()


generoContagem.columns = ['musicGenre', 'Count']

contagem_pop = df_2020_2024['musicGenre'].value_counts().get("Hip hop/Rap", 0)

top10Generos = generoContagem.head(10)

print(generoContagem.head(10))
colors = sns.color_palette("tab10", len(top10Generos))
plt.figure(figsize=(10, 8))
plt.pie(top10Generos['Count'], labels=top10Generos['musicGenre'], autopct='%1.1f%%', startangle=140, colors=colors)


plt.title("Top 10 Gêneros Musicais Mais Escutados de 2020 a 2024")


#plt.savefig(r"c:\Users\victo\Downloads\top10Genero2020_2024.png", format= 'png', dpi=300, bbox_inches='tight' )
plt.show()
#generoContagem.to_excel(r"c:\Users\victo\Downloads\generos_mais_escutados_2020_2024.xlsx", index=False)