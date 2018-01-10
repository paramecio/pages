#!/usr/bin/env python3

from paramecio.wsgiapp import app
from paramecio.citoplasma.mtemplates import PTemplate, env_theme
from modules.pages.models.pages import Page
from paramecio.cromosoma.webmodel import WebModel
from settings import config
from bottle import abort

env=env_theme(__file__)

t=PTemplate(env)

pages_modules_to_search=[]

if hasattr(config, 'pages_modules_to_search'):
    pages_modules_to_search=config.pages_modules_to_search
    
for mod in pages_modules_to_search:

    t.env.directories.insert(0, mod.replace('.', '/')+'/templates')

@app.get('/pages/<page_id:int>')
@app.get('/pages/<slug>')
def index(page_id=0, slug=''):
    
    conn=WebModel.connection()
    
    page=Page(conn)
    
    page.show_formatted=True
    
    if page_id:
    
        page.set_conditions('WHERE id=%s', [page_id])
        
    if slug:

        page.set_conditions('WHERE slugify=%s', [slug])

    arr_page=page.select_a_row_where()

    if arr_page:

        return t.load_template('page.phtml', title_page=arr_page['title'], content_page=arr_page['text'])
        
    else:
        
        abort(404, "No page found")
