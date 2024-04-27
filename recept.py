"""A receptek alkalmazás fő modulja

"""
from fastapi import FastAPI
from adatok.adatok import UZLETEK, ELELMISZEREK, kovetkezo_uzlet_id
from adatmodell.uzletek_adat_modell import Uzlet, UzletRequest


app = FastAPI()


@app.get("/uzletek_lekerdez")
async def uzletek_lekerdez():
    """Üzletlista lekérdezése

    Returns:
        list: Visszatér az üzletlistával
    """
    print(type(UZLETEK))
    return UZLETEK


@app.post("/uzlet_letrehozas")
async def uzlet_letrehozas(uzlet_request: UzletRequest):
    """Új üzlet rögzítése

    Args:
        uzlet_request (UzletRequest): UzletRequest osztály segítségével validálásra kerül a 
        requestben érkező adat.

    Returns:
        list: Visszatér az új üzlet adatával
    """
    print(type(uzlet_request))
    uj_uzlet = Uzlet(**uzlet_request.model_dump())
    print(uj_uzlet)
    uj_uzlet.uzlet_id = kovetkezo_uzlet_id()
    UZLETEK.append(uj_uzlet)
    return uj_uzlet


@app.get("/elelmiszerek_lekerdez")
async def elelmiszerek_lekerdez():
    """Élelmiszerek lekérdezése

    Returns:
        list: Visszatér az élelmiszerlistával
    """
    return ELELMISZEREK

# @app.put("/elelmiszerek")
# async def rogzit_elelmiszerek():
#     return ELELMISZEREK


# @app.get("/eleskamra")
# async def lekerdez_eleskamra():
#     return ELESKAMRA

# @app.put("/eleskamra")
# async def rogzit_eleskamra():
#     return ELESKAMRA

#uvicorn recept:app --reload
