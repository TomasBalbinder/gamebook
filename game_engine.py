import random

from carodej_z_ohnove_hory import hra


def vytvor_postavu(hrdina):
    """Nastavi hodnoty v deniku hrace a vypise hodnoty."""
    pass

def souboj(hrdina):
    """Vyhodnoti souboj hrdiny a netvora.
    V pocatecni implementaci zada hrac utocne cislo a staminu netvora na zacatku funkce.
    Vrati True pokud hrdina prezije, False pokud umre.

    (V budoucnu
      - netvor asi dalsi parametr funkce
      - moznost utect z boje (nektere to umoznuji, nektere ne)
      - souboj s vice nestvurami soucasne
     pro vyse zminene bude potreba vylepsit podkladova data
    """
    pass

def zkusit_stesti(hrdina):
    """Vyhodnoti zkouseni stesti.
    Vrati True pri uspechu a False pri neuspechu"""
    pass

def odpocivat(hrdina):
    """Vyhodnoti odpocinek"""

def hraj(hra, hrdina):
    """Hlavni smycka hry.
          Zobrazi text prislusne stranky
          Zajisti vyreseni boje (v budoucnu odpocinku/zkouseni stesti, bude potreba vylepsit podkladova data)
          Nacte od hrace cislo dalsi strany
       (V budoucnu vyresi preruseni hry a ulozeni na priste, vypisovani aktualniho stavu postavy)
    """
    while True:
        # zobraz text stranky
        # nabidnout vypiti lektvaru
        # vyres souboj a pripadnou smrt
        # nacti dalsi cislo strany
        pass

def main():
    """
    (V budoucnu pridat nacteni ulozeneho stavu z minula)
    """
    hrdina = {
            "utocne_cislo": 0, "uc_max": 0,
            "stamina": 0, "sm_max": 0,
            "stesti": 0, "st_max": 0,
            "lektvar": None,
            "proviant": 10,
            "zlataky": 0,
            "drahokamy": 0,
            "batoh": []
            }
    vytvor_postavu(hrdina)

    hraj(hra, hrdina)

if __name__ == "__main__":
    main()
