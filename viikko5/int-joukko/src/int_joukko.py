class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("Väärä kapasiteetti")
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise ValueError("Väärä kasvatuskoko")

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def _luo_lista(self, koko):
        return [0] * koko

    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                self._kasvata_taulukkoa()

            return True

        return False

    def _kasvata_taulukkoa(self):
        uusi_taulukko = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self._kopioi_lista(self.ljono, uusi_taulukko)
        self.ljono = uusi_taulukko

    def poista(self, n):
        if n in self.ljono[:self.alkioiden_lkm]:
            indeksi = self.ljono.index(n)
            self.ljono.pop(indeksi)
            self.alkioiden_lkm -= 1
            return True

        return False

    def _kopioi_lista(self, lahde, kohde):
        for i in range(len(lahde)):
            kohde[i] = lahde[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def _yhdiste_tai_leikkaus(a, b, yhdiste=True):
        tulos = IntJoukko()

        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in a_taulu:
            tulos.lisaa(luku)

        for luku in b_taulu:
            if (yhdiste and not tulos.kuuluu(luku)) or (not yhdiste and a.kuuluu(luku) and b.kuuluu(luku)):
                tulos.lisaa(luku)

        return tulos

    @staticmethod
    def yhdiste(a, b):
        return IntJoukko._yhdiste_tai_leikkaus(a, b, yhdiste=True)


    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            return "{" + ", ".join(map(str, self.ljono[:self.alkioiden_lkm])) + "}"
    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()

        for luku in a.to_int_list():
            if b.kuuluu(luku):
                tulos.lisaa(luku)

        return tulos

    @staticmethod
    def erotus(a, b):
        erotus_taulu = b.to_int_list()
        tulos = IntJoukko()

        for luku in a.to_int_list():
            if luku not in erotus_taulu:
                tulos.lisaa(luku)

        return tulos
