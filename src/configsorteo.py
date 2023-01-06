from .equipo import seleccion

class seleciones_clasificadas():
    def __init__(self):
        self.list=[]

    def bombo1(self):
        bombo1=[]
        Qatar=seleccion('Qatar','Asia',1)
        Qatar.add_local()
        bombo1.append(Qatar)
        Inglaterra=seleccion('England','UEFA',1)
        bombo1.append(Inglaterra)
        Argentina=seleccion('Argentina','CONMEBOL',1)
        bombo1.append(Argentina)
        Francia=seleccion('France','UEFA',1)
        bombo1.append(Francia)
        España=seleccion('Spain','UEFA',1)
        bombo1.append(España)
        Belgica=seleccion('Belgium','UEFA',1)
        bombo1.append(Belgica)
        Brasil=seleccion('Brasil','CONMEBOL',1)
        bombo1.append(Brasil)
        Portugal=seleccion('Portugal','UEFA',1)
        bombo1.append(Portugal)
        self.list.append(bombo1)
        return None

    def bombo2(self):
        bombo2=[]
        Holanda=seleccion('Netherlands','UEFA',2)
        bombo2.append(Holanda)
        USA=seleccion('USA','CONCACAF',2)
        bombo2.append(USA)
        Mexico=seleccion('Mexico','CONCACAF',2)
        bombo2.append(Mexico)
        Dinamarca=seleccion('Denmark','UEFA',2)
        bombo2.append(Dinamarca)
        Alemania=seleccion('Germany','UEFA',2)
        bombo2.append(Alemania)
        Croacia=seleccion('Croatia','UEFA',2)
        bombo2.append(Croacia)
        Suiza=seleccion('Switzerland','UEFA',2)
        bombo2.append(Suiza)
        Uruguay=seleccion('Uruguay','CONMEBOL',2)
        bombo2.append(Uruguay)
        self.list.append(bombo2)
        return None

    def bombo3(self):
        bombo3=[]
        Senegal=seleccion('Senegal','AFRICA',3)
        bombo3.append(Senegal)
        Iran=seleccion('Iran','ASIA',3)
        bombo3.append(Iran)
        Polonia=seleccion('Poland','UEFA',3)
        bombo3.append(Polonia)
        Japon=seleccion('Japan','ASIA',3)
        bombo3.append(Japon)
        Marruecos=seleccion('Marrocco','AFRICA',3)
        bombo3.append(Marruecos)
        Corea=seleccion('South Corea','ASIA',3)
        bombo3.append(Corea)
        Serbia=seleccion('Serbia','UEFA',3)
        bombo3.append(Serbia)
        Tunez=seleccion('Tunisia','AFRICA',3)
        bombo3.append(Tunez)
        self.list.append(bombo3)
        return None

    def bombo4(self):
        bombo4=[]
        Ecuador=seleccion('Ecuador','CONMEBOL',4)
        bombo4.append(Ecuador)
        Canada=seleccion('Canada','CONCACAF',4)
        bombo4.append(Canada)
        Arabia=seleccion('Saudi Arabia','ASIA',4)
        bombo4.append(Arabia)
        Camerun=seleccion('Camerun','AFRICA',4)
        bombo4.append(Camerun)
        Ghana=seleccion('Ghana','AFRICA',4)
        bombo4.append(Ghana)
        Australia=seleccion('Australia','ASIA',4)
        bombo4.append(Australia)
        Costa_Rica=seleccion('Costa Rica','CONCACAF',1)
        bombo4.append(Costa_Rica)
        Gales=seleccion('Wales','UEFA',1)
        bombo4.append(Gales)
        self.list.append(bombo4)
        return None

    def __call__(self):
        self.bombo1()
        self.bombo2()
        self.bombo3()
        self.bombo4()
        return self.list
