"""A fejlesztés során használt memória adatok kerültek ide

"""
from adatmodell.uzletek_adat_modell import Uzlet

UZLETEK = [
    Uzlet(1,'Lidl')
]

ELELMISZEREK = []

ELESKAMRA = []


def kovetkezo_uzlet_id()-> int:
    if len(UZLETEK) > 0:
        return len(UZLETEK)+1
    return 1