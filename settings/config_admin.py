from paramecio.citoplasma.i18n import I18n, load_lang
from settings.config_admin import modules_admin

#from modules.pokermind.i18n import runchained

modules_other=[I18n.lang('pages', 'pages', 'Pages'), 'modules.pages.admin.pages', 'pages']

modules_admin.append(modules_other)
