
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

beneficios_objetos = [2, 1, 3, 4, 4] 
pesos_objetos = [4, 5, 7, 10, 6] 
capacidade_maxima = 23  


itens_selecionados, peso_total, beneficio_total = heuristica_maior_beneficio(capacidade_maxima, pesos_objetos, beneficios_objetos)

print(f"Itens selecionados: {itens_selecionados}")
print(f"Peso total na mochila: {peso_total}")
print(f"Valor total dos itens: {beneficio_total}")