from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from luo_peli import luo_peli

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a") or vastaus.endswith("b") or vastaus.endswith("c"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            tyyppi=vastaus
            peli=luo_peli(tyyppi)
            peli.pelaa()
        # elif vastaus.endswith("b"):
        #     print(
        #         "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        #     )

        #     tyyppi=vastaus
        #     peli=luo_peli(tyyppi)
        #     peli.pelaa()
        # elif vastaus.endswith("c"):
        #     print(
        #         "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        #     )

        #     haastava_yksinpeli = KPSParempiTekoaly()
        #     haastava_yksinpeli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
