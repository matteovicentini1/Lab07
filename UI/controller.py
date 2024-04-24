import flet as ft

from UI.view import View
from model.model import Model

class Umidita:
    def __init__(self,citta):
        self.citta=citta
        self.temper=[]

    def umiditmedia(self):
        som=0
        for i in self.temper:
            som+=i
        return som/len(self.temper)


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e):
        city = set()
        for i in self._model.situazioni:
            city.add(i.localita)
        umi=[]
        for i in city:
            umi.append(Umidita(i))
        if self._mese!=0:
            for i in self._model.situazioni:
                for k in umi:
                    if i.localita==k.citta and self._mese==int(i.data.month):
                        k.temper.append(i.umidita)
            self._view.lst_result.clean()
            for i in umi:
                self._view.lst_result.controls.append(ft.Text(f'Località: {i.citta} temperatura media: {i.umiditmedia()}'))
            self._view.update_page()
        else:
            self._view.lst_result.clean()
            self._view.lst_result.controls.append(ft.Text(f'Selezionare mese',color='red',size=20))
            self._view.update_page()


    def handle_sequenza(self, e):
        if self._mese != 0:
            self._view.lst_result.clean()
            seq,c=self._model.sequenza(self._mese)
            self._view.lst_result.controls.append(ft.Text(f'Sequenza ottima per il mese {self._mese} con costo {c}:'))
            m=1
            for i in seq:
                self._view.lst_result.controls.append(ft.Text(f'{m}) città: {i}'))
                m+=1
            self._view.update_page()
        else:
            self._view.lst_result.clean()
            self._view.lst_result.controls.append(ft.Text(f'Selezionare mese',color='red',size=20))
            self._view.update_page()


    def read_mese(self, e):
        self._mese = int(e.control.value)

