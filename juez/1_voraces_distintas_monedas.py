import math


def cambio_monedas(monedas, cambio):
    sol = []
    i = 0
    while i < len(monedas) and cambio>0:
        while cambio >= monedas[i]:
            cambio -= monedas[i]
            sol.append(monedas[i])
        i += 1
    return sol,cambio


dineroTienda = int(input().strip())
numTiposMoneda = int(input().strip())
cambios={}
equivalencias={}
for _ in range(numTiposMoneda):
    cambiosAct=list(input().strip().split())
    equivalencias[cambiosAct[0]]=float(cambiosAct[1])
    cambios[cambiosAct[0]]=list(map(int, cambiosAct[2:]))
numCompras = int(input().strip())
min=0x3F3F3F3F
best=""
for i in range(numCompras):
    tipo, cantidad = input().strip().split()
    dineroTienda+=math.ceil(int(cantidad)*equivalencias[tipo])
    sol,restante=cambio_monedas(cambios[tipo], int(cantidad))
    print("Pedido "+str(i+1)+ " paga con ", end = "")
    print(*sol)
print("Dinero al final del dia: "+str(dineroTienda))