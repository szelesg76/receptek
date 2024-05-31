"""A receptek alkalmazás fő modulja

"""
import os
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
# from adatbazis.adatok import UZLETEK, ELELMISZEREK, kovetkezo_uzlet_id
# from adatmodell.uzletek_adat_modell import Uzlet, UzletRequest
from starlette.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from starlette import status

from sqlalchemy.orm import Session

from adatbazis.adatbazis import engine, SessionLocal
import adatmodell.uzletek_modell as uzletek_modell
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

uzletek_modell.Base.metadata.create_all(bind=engine)


app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")
# app.mount('/static', StaticFiles(directory=os.path.join(current_dir, 'static')), name='static')
app.mount("/static", StaticFiles(directory=Path(BASE_DIR, 'static')), name="static")

templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/favicon.ico')
async def favicon():
    file_name = "favicon.ico"
    file_path = os.path.join(app.root_path, "static", file_name)
    return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})


# @app.get("/test")
# async def test(request: Request):
#     return templates.TemplateResponse("home.html", {"request": request})

# @app.get("/test", response_class=HTMLResponse)
# async def test(request: Request):
#     id = 'Aldi'
#     return templates.TemplateResponse(name="home.html",  request=request, context={"id": id})

@app.get("/uzletek", response_class=HTMLResponse)
async def uzletek(request: Request, db: Session = Depends(get_db)):
    # return templates.TemplateResponse(name="uzletek.html",  request=request, context={"uzletek": UZLETEK})
    uzletek_adat = db.query(uzletek_modell.Uzletek).all()
    # for row in uzletek_adat:
    #     print(row.uzlet_id, row.uzlet_nev)
    
    return templates.TemplateResponse(name="uzletek.html",  request=request, context={"uzletek": uzletek_adat})
    # return templates.TemplateResponse("uzletek.html", {"request": request, "uzletek": uzletek_adat})

@app.get("/uzlet_uj", response_class=HTMLResponse)
async def uzlet_letrehozas(request: Request):
    return templates.TemplateResponse(name="uzlet_uj.html", request=request)


#, uzlet_request: UzletRequest,
@app.post("/uzlet_uj", response_class=HTMLResponse)
async def uzlet_letrehozas_mentes(request: Request, uzlet_nev: str = Form(...), db: Session = Depends(get_db)):
    """Új üzlet rögzítése

    Args:
        uzlet_request (UzletRequest): UzletRequest osztály segítségével validálásra kerül a 
        requestben érkező adat.

    Returns:
        list: Visszatér az új üzlet adatával
    """
    # print(type(uzlet_request))
    # uj_uzlet = Uzlet(**request.model_dump())
    # form = await PydanticForm.validate_request(request, UzletRequest)  
    
    # uzlet_id = kovetkezo_uzlet_id()
    # uj_uzlet = Uzlet(uzlet_id,uzlet_nev)
    # uj_uzlet.uzlet_id = uzlet_id
    # print(uj_uzlet.uzlet_id)
    # print(uj_uzlet.uzlet_nev)
    # UZLETEK.append(uj_uzlet)

    uzlet_adat = uzletek_modell.Uzletek()
    uzlet_adat.uzlet_nev = uzlet_nev
    
    db.add(uzlet_adat)
    db.commit()
    
    return RedirectResponse(url="/uzletek", status_code=status.HTTP_302_FOUND)



@app.get("/uzlet_modosit/{uzlet_id}", response_class=HTMLResponse)
async def uzlet_modosit(request: Request, uzlet_id: int, db: Session = Depends(get_db)):
    
    # uzlet = UZLETEK[uzlet_id-1]
    uzlet_adat = db.query(uzletek_modell.Uzletek).filter(uzletek_modell.Uzletek.uzlet_id == uzlet_id).first()
    # print(uzlet_adat)
    return templates.TemplateResponse("uzlet_modosit.html", {"request": request, "uzlet": uzlet_adat})



@app.post("/uzlet_modosit/{uzlet_id}", response_class=HTMLResponse)
async def uzlet_modosit_mentes(request: Request, uzlet_id: int, uzlet_nev: str = Form(...), db: Session = Depends(get_db)):
    """Új üzlet rögzítése

    Args:
        uzlet_request (UzletRequest): UzletRequest osztály segítségével validálásra kerül a 
        requestben érkező adat.

    Returns:
        list: 
    """
    # uj_uzlet = Uzlet(uzlet_id,uzlet_nev)

    # print(uj_uzlet.uzlet_id)
    # print(uj_uzlet.uzlet_nev)
    # UZLETEK[uzlet_id-1] = uj_uzlet
    
    uzlet_adat = db.query(uzletek_modell.Uzletek).filter(uzletek_modell.Uzletek.uzlet_id == uzlet_id).first()
    uzlet_adat.uzlet_nev = uzlet_nev  
    db.add(uzlet_adat)
    db.commit()
    return RedirectResponse(url="/uzletek", status_code=status.HTTP_302_FOUND)


@app.get("/uzlet_torol/{uzlet_id}", response_class=HTMLResponse)
async def uzlet_torol(request: Request, uzlet_id: int, db: Session = Depends(get_db)):
    
    # UZLETEK.pop(uzlet_id-1)
    # print(UZLETEK)
    uzlet_adat = db.query(uzletek_modell.Uzletek).filter(uzletek_modell.Uzletek.uzlet_id == uzlet_id).first()
    db.delete(uzlet_adat)
    db.commit()
    
    return RedirectResponse(url="/uzletek", status_code=status.HTTP_302_FOUND)


# support endpoint
@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}




# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse(request=request, name="item.html",  context={"id": id})


# @app.get("/test", response_class=HTMLResponse)
# async def test(request: Request):
#     return templates.TemplateResponse("home.html",  {"request": request}, context={"iddfg": 345})






# @app.get("/uzletek_lekerdez")
# async def uzletek_lekerdez():
#     """Üzletlista lekérdezése

#     Returns:
#         list: Visszatér az üzletlistával
#     """
#     print(type(UZLETEK))
#     return UZLETEK





# @app.get("/elelmiszerek_lekerdez")
# async def elelmiszerek_lekerdez():
#     """Élelmiszerek lekérdezése

#     Returns:
#         list: Visszatér az élelmiszerlistával
#     """
#     return ELELMISZEREK

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
