"""A receptek alkalmazás fő modulja

"""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from adatok.adatok import UZLETEK, ELELMISZEREK, kovetkezo_uzlet_id
from adatmodell.uzletek_adat_modell import Uzlet, UzletRequest
from starlette.staticfiles import StaticFiles





app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/test")
async def test(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/test2")
async def test2(request: Request):
    return templates.TemplateResponse("uj_uzlet.html", {"request": request})


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

# MARK: Innen folytasd a munkát
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
