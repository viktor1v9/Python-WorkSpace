def hanoi(n, origem, destino, auxiliar):
    if n == 1:   # Quando "n == 1", o disco mais pequeno é movido diretamente da torre de origem para a torre de destino.
        print(f"Mova o disco {n} de {origem} para {destino}")
    else:  
        hanoi(n-1, origem, auxiliar, destino)    #  Mova "n-1" discos da torre de origem para a torre auxiliar, usando a torre de destino como auxiliar.
        print(f"Mova o disco {n} de {origem} para {destino}")
        hanoi(n-1, auxiliar, destino, origem)   # Mova os "n-1" discos da torre auxiliar para a torre de destino, usando a torre de origem como auxiliar.

hanoi(4, 'A', 'C', 'B')