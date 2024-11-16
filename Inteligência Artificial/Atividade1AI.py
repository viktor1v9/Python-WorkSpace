def heuristica_maior_beneficio(capacidade, pesos, beneficios):

    n = len(pesos)  

    itens_selecionados = []  
    peso_total = 0  
    beneficio_total = 0  

   
    itens = [(pesos[i], beneficios[i], i) for i in range(n)]

   
    itens.sort(key=lambda x: x[1], reverse=True)

  
    for peso, valor, indice in itens:
        if peso_total + peso <= capacidade: 
            itens_selecionados.append(indice) 
            peso_total += peso   
            beneficio_total += valor  

    return itens_selecionados, peso_total, beneficio_total



beneficios_investimentos = [40000, 60000, 45000, 15000, 25000]  
pesos_investimentos = [30000, 50000, 40000, 10000, 20000]  
capacidade_maxima = 100000

itens_selecionados, custo_total, retorno_total = heuristica_maior_beneficio(capacidade_maxima, pesos_investimentos, beneficios_investimentos)


nomes_investimentos = ['Ações Empresa X', 'Ações Empresa Y', 'Imóvel Z', 'Títulos Públicos P', 'Fundo de Investimento F']

print("Investimentos selecionados:")
for i in itens_selecionados:
    print(nomes_investimentos[i])

print(f"\nCusto total dos investimentos: R${custo_total}")
print(f"Retorno total dos investimentos: R${retorno_total}")

