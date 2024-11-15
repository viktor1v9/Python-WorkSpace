import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"c:\Users\victo\Downloads\spotifyDBIntegrada.xlsx", sheet_name="a4dc5967-378c-4e8f-83ef-99f0445")

df['chartWeek'] = pd.to_datetime(df['chartWeek'], dayfirst=True, errors='coerce')

anos = [2020, 2021, 2022, 2023]

sns.set(style="whitegrid")
plt.figure(figsize=(15, 14))  

for i, ano in enumerate(anos):

    df_dezembro = df[(df['chartWeek'].dt.year == ano) & (df['chartWeek'].dt.month == 12)]

    top10_dezembro = df_dezembro[df_dezembro['currentPosition'] <= 10]
  
    top10_dezembro = top10_dezembro.sort_values(by='currentPosition').reset_index(drop=True)
    
    plt.subplot(2, 2, i + 1) 
    sns.barplot(data=top10_dezembro, x='currentPosition', y='artistName', palette='viridis')
    
    plt.title(f"Top 10 Artistas de Dezembro {ano}")
    plt.xlabel("Posição")
    plt.ylabel("Artistas")
  
    plt.xticks(rotation=45, ha='right', fontsize=10)
   
    for index, value in enumerate(top10_dezembro['currentPosition']):
        plt.text(value, index, f"{int(value)}", ha='left', va='center', fontsize=9)

plt.subplots_adjust(hspace=0.5, wspace=0.4)

#plt.savefig(r"c:\Users\victo\Downloads\top10Artistas2020_2024.png", format='png', dpi=300, bbox_inches='tight')

plt.show()
