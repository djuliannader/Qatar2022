from src.configsorteo import seleciones_clasificadas
from src.sorteando import Grupos


print('*************Setting the raffle*****************')
bombos=seleciones_clasificadas()()
for i in range(4):
    print(f'--Pot {i+1}')
    for j in range(len(bombos[1])):
        print(bombos[i][j].nombre)
print('**************************************************')
# llevando a cabo el sorteo sorteo
grupos=Grupos(bombos)
grupos_final=grupos()
print('-----------------------------------------------------')
print(grupos_final)
