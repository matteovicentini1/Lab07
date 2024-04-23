
from database import meteo_dao as md

class Model:
    def __init__(self):
        self.situazioni =md.MeteoDao().get_all_situazioni()

        self.globale=999999999999999999999999999999999999999999999999999999999999999999999



    def sequenza(self,mese):
        sit_nel_mese=[]
        for i in self.situazioni:
            if int(mese) ==i.data.month and int(i.data.day)<=15:
                sit_nel_mese.append(i)

        return self.ricorsione(sit_nel_mese,[],0,1),self.globale

    def ricorsione(self,lista,lista_da_riempire,costo,d):
        if d==16:
            return lista_da_riempire
        else:
            for i in range(len(lista)):
                if int(lista[i].data.day) == int(d):
                    if d!=15:
                        n = lista_da_riempire+[lista[i]]
                        costo += lista[i].umidita
                        return self.ricorsione(lista,n,costo,d+1)
                    else:
                        n = lista_da_riempire + [lista[i]]
                        costo += lista[i].umidita
                        if self.consecuzio(lista_da_riempire)==True and self.conteggio(lista_da_riempire)==True:
                            return self.ricorsione(lista, n, costo, d + 1)

    def consecuzio(self,lista):
        pass



    def conteggio(self,lista):
        nomi=[]
        for i in lista:
            nomi.append(i.localita)
        for i in lista:
            if nomi.count(i.localita) >6:
                return False









