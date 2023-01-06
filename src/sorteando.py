from random import seed
from random import randint
import sys

#seed(22)

class Grupos():
    def  __init__(self,lista_paises) -> None:
        self.lista_paises=lista_paises
        self.lista_paisesxgrupo=[]
        self.gruposfinal={"Group 1":[] ,"Group 2":[],"Group 3":[],"Group 4":[], "Group 5":[],
          "Group 6": [], "Group 7":[], "Group 8":[] }
    
    def acomodando_cabezas_serie(self, object, grupo:int,ran):
        self.lista_paisesxgrupo.append([object])
        self.gruposfinal[f"Group {grupo}"]=[object.nombre]
        del self.lista_paises[0][ran]
        return None

    def validando_grupo(self,confe,grupo,bombo)->bool:
        try:
            confe_grupo=[self.lista_paisesxgrupo[grupo-1][elementos].confederacion for elementos
                 in range(len(self.lista_paisesxgrupo[grupo-1]))]
        except:
            print(f'The raffle failed. Last team from confederation {confe} can not be acommodated' )
            sys.exit('Error in the configuration of groups')
        if confe == 'UEFA' and  len(self.lista_paisesxgrupo[grupo-1]) < bombo:
            if confe_grupo.count('UEFA')<2:
                return True
        elif confe not in confe_grupo and  len(self.lista_paisesxgrupo[grupo-1]) < bombo:
            return True
        print(f'--- It is not allowed in Group {grupo }')
        return False

    def acomodando_equipoengrupo(self,object,grupo,bombo,ran):
        equipo=object.nombre
        bol=self.validando_grupo(object.confederacion,grupo,bombo)
        if bol:
            self.lista_paisesxgrupo[grupo-1].append(object)
            self.gruposfinal[f"Group {grupo}"].append(equipo)
            del self.lista_paises[bombo-1][ran]
            print(f'{equipo} goes to gruop {grupo}')
            print(self.gruposfinal)
            return grupo
        return self.acomodando_equipoengrupo(object,grupo+1,bombo,ran)
        



    def acomodando_bombo(self,bombo:int):
        print(f'************************** The teams in Pot {bombo} are going to be raffled *****************************')
        i=0
        while len(self.lista_paises[bombo-1])>0:
            if len(self.lista_paisesxgrupo[i]) < bombo:
                value=randint(0,len(self.lista_paises[bombo-1])-1)
                print(f'(*) The chosen country is {self.lista_paises[bombo-1][value].nombre}')
                k=self.acomodando_equipoengrupo(self.lista_paises[bombo-1][value],i+1,bombo,value)
                if i==k:
                    i=i+1
            else:
                i=i+1


                

    def __call__(self):
        # asignando el grupo 1 al local
        for i in range(7):
            if self.lista_paises[0][i].local:
                self.acomodando_cabezas_serie(self.lista_paises[0][i],1,0) 
        print(self.gruposfinal)
        # acomodando cabezas de serie en los 8 grupos
        print('******* Acomodating head of groups **********')
        for i in range(7):
            value=randint(0,len(self.lista_paises[0])-1)
            self.acomodando_cabezas_serie(self.lista_paises[0][value],i+2,value)
            print(self.gruposfinal)
        for i in range(2,5):
            self.acomodando_bombo(i)
        print('The raffle was carried out succesfully')
        return self.gruposfinal
