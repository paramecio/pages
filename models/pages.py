from paramecio.cromosoma.extrafields.i18nfield import I18nHTMLField, I18nField
from paramecio.cromosoma.extrafields.slugifyfield import SlugifyField
from paramecio.cromosoma.webmodel import WebModel
from paramecio.cromosoma.extraforms.texthtmlform import TextHTMLForm
from paramecio.cromosoma import corefields
from paramecio.citoplasma.i18n import I18n
import json

class Page(WebModel):

    def create_fields(self):
        
        self.register(I18nField('title'), True)
        self.register(I18nHTMLField('text', TextHTMLForm('text', '')), True)
        self.register(SlugifyField('slugify'), True)

    """
    def insert(self, dict_values, external_agent=True):
        
        slugify=json.loads(dict_values.get('title', '{}'))
        
        lang=I18n.get_default_lang()
        
        dict_values['slugify']=slugify.get(lang, '')
        
        return super().insert(dict_values, external_agent)

    def update(self, dict_values, external_agent=True):
        
        slugify=json.loads(dict_values.get('title', '{}'))
        
        lang=I18n.get_default_lang()
        
        dict_values['slugify']=slugify.get(lang, '')
        
        return super().update(dict_values, external_agent)
    """
    
