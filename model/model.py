import copy

from database import meteo_dao as md
import queue as q
class Model:
    def __init__(self):
        self.situazioni =md.MeteoDao().get_all_situazioni()

        self.globale= q.PriorityQueue()

    def sequenza(self,mese):
        sit_nel_mese=[]
        for i in self.situazioni:
            if int(mese) ==i.data.month and int(i.data.day)<=15:
                sit_nel_mese.append(i)

        while not self.globale.empty():
            self.globale.get()

        self.ricorsione(sit_nel_mese,[],1)
        tup = self.globale.get()
        print('fatto')
        return tup[1],tup[0]

    def ricorsione(self,lista,lista_da_riempire,d):
        if d==16:
            self.globale.put((self.balzi(lista_da_riempire),copy.deepcopy(lista_da_riempire)))
            print('load')
            return
        else:
            for i in range(len(lista)):
                if int(lista[i].data.day) == int(d):
                    if d!=15:
                        lista_da_riempire+=[lista[i]]
                        self.ricorsione(lista,lista_da_riempire,d+1)
                        lista_da_riempire.pop()
                    else:
                        lista_da_riempire+=[lista[i]]
                        if self.consecuzio(lista_da_riempire)==True :
                            self.ricorsione(lista, lista_da_riempire, d + 1)
                        lista_da_riempire.pop()

    def balzi(self,lista):
        c=0
        for i in range(len(lista)-1):
            if lista[i].localita != lista[i + 1].localita:
                c+=1
        cc=0
        for i in lista:
            cc+=i.umidita
        return (cc+ c*100+200)

    def consecuzio(self,lista):
        if self.conteggio(lista)==True:
            c=1
            for i in range(len(lista)-1):
                if lista[i].localita == lista[i+1].localita:
                    c+=1
                else:
                    if c>=3:
                        c=1
                        continue
                    else:
                        return False
            return True
        else:
            return False



    def conteggio(self,lista):
        nomi=[]
        for i in lista:
            nomi.append(i.localita)
        for i in lista:
            if nomi.count(i.localita)>6 or nomi.count(i.localita)<3:
                return False
        return True









