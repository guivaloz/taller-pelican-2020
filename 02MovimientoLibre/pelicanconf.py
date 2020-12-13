"""
Pelican - 02 Movimiento Libre - pelicanconf.py
"""

# Sitio web
SITENAME = 'Movimiento Libre'
SITEURL = ''
SITEDESCRIPTION = 'Sitio web de GUIVALOZ'
SITEKEYWORDS = 'Software Libre, GNU/Linux, Desarrollo, Programación'
SITELOGO = 'theme/images/movimientolibre.png'
SITETWITTER = '@guivaloz'
AUTHOR = 'guivaloz'

# Tema
THEME = 'themes/bootstrap-4'

# Directorio donde esta el contenido
PATH = 'content'

# Directorios que tienen los articulos
ARTICLE_PATHS = ['apuntes', 'articulos', 'presentaciones']

# Directorios que tienen páginas fijas, no artículos
PAGE_PATHS = ['licencias', 'portafolio']

# Directorios y archivos que son fijos
# Agregue también los directorios que tienen imágenes y descargables para artículos y páginas
STATIC_PATHS = ['favicon.ico', 'robots.txt', 'apuntes', 'articulos', 'presentaciones']

# Encabezados para las categorías
CATEGORIES_TITLES = {
    'apuntes': 'Apuntes',
    'articulos': 'Artículos',
    'presentaciones': 'Presentaciones',
}

# Usar el nombre del directorio como la categoría
USE_FOLDER_AS_CATEGORY = False

# Los artículos van en directorios por categoria/titulo/
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

# Las páginas fijas van en directorios categoria/titulo/
PAGE_URL = '{category}/{slug}/'
PAGE_SAVE_AS = '{category}/{slug}/index.html'

# Lenguaje y zona horaria
TIMEZONE = 'America/Mexico_City'
DEFAULT_LANG = 'es'

# Se desactiva la generacion de feeds
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Cargar jQuery Bootstrap desde terceros
USE_REMOTE_SERVICES = True
