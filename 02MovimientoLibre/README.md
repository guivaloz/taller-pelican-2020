# 02 Movimiento Libre

Cámbiese a este directorio

    cd 02MovimientoLibre

## Comando Pelican

Consulte la ayuda

    pelican --help

Configure editando

    nano -w pelicanconf.py

Configure para publicar editando

    nano -w publishconf.py

Construya el sitio web para probarlo localmente

    pelican --delete-output-directory content

Levante el servidor web

    pelican --listen

## Instale temas creados por terceros

Cree el directorio themes y copie temas de Pelican.

    mkdir themes

Para crear el sitio con el tema configurado ejecute

    pelican --settings pelicanconf.py --delete-output-directory content

Para probar un tema puede agregar este parámetro

    pelican --settings pelicanconf.py --theme-path themes/monospace --delete-output-directory content
