class Televize:

    aktualniKanal = 0
    zapnuto = False

    def zapni(self):
        self.zapnuto = True
        pass
    def vypni(self):
        self.zapnuto = False
        pass
    def prepniKanal(self,cislo):
        self.aktualniKanal = cislo
        pass

sony = Televize()
sony.zapni()
