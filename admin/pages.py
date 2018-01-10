from paramecio.citoplasma.generate_admin_class import GenerateAdminClass
from paramecio.citoplasma.adminutils import make_admin_url
#from paramecio.citoplasma.urls import make_url
from paramecio.citoplasma.i18n import I18n
from settings import config
from modules.pages.models import pages
from paramecio.citoplasma.httputils import GetPostFiles
from paramecio.cromosoma.coreforms import BaseForm

def admin(**args):
   
    forms=GetPostFiles()
    
    forms.obtain_query()
    
    t=args['t']

    conn=args['connection']
    
    page=pages.Page(conn)
    
    page.enctype=True

    page.fields['slugify'].name_form=BaseForm

    page.fields['text'].extra_parameters[0].t=t
    
    url=make_admin_url('pages')
    
    admin=GenerateAdminClass(page, url, t)
    
    admin.list.fields_showed=['id', 'title', 'slugify']
    
    return admin.show()
