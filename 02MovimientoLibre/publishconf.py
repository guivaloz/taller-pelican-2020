"""
Pelican - 02 Movimiento Libre - pelicanconf.py
"""

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Sitio web
SITEURL = 'https://movimientolibre.com'

# Generacion de feeds
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
FEED_MAX_ITEMS = 12
RSS_FEED_SUMMARY_ONLY = True

# URLs son absolutos
RELATIVE_URLS = False

# Eliminar el directorio de salida
DELETE_OUTPUT_DIRECTORY = True
