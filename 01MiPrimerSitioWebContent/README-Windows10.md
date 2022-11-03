# 01 Mi primer sitio web (Pelican en Windows 10)

Ejecutar pelican-quickstart para crear 01MiPrimerSitioWeb

    pelican-quickstart.exe

Alimentar asistente

    > Where do you want to create your new web site? [.] 01MiPrimerSitioWeb
    > What will be the title of this web site? Mi primer sitio web
    > Who will be the author of this web site? Nombre Apellido
    > What will be the default language of this web site? [es]
    > Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) n
    > Do you want to enable article pagination? (Y/n) n
    > What is your time zone? [Europe/Paris] America/Mexico_City
    > Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) Y
    > Do you want to upload your website using FTP? (y/N) n
    > Do you want to upload your website using SSH? (y/N) n
    > Do you want to upload your website using Dropbox? (y/N) n
    > Do you want to upload your website using S3? (y/N) n
    > Do you want to upload your website using Rackspace Cloud Files? (y/N) n
    > Do you want to upload your website using GitHub Pages? (y/N) n
    Done. Your new project is available at...

Cambiar al directorio del sitio

    cd 01MiPrimerSitioWeb

Cambiar al directorio para el contenido

    cd content

En esa ubicación cree un archivo primer-pagina.md

    Title: Mi primer artículo
    Date: 2019-03-31 19:10
    Category: Vida cotidiana

    Esta es la primer página que escribo en el constructor de sitios web Pelican.

### Construir el Sitio

    pelican -s pelicanconf.py

### Levantar el servidor

    cd output
    python -m http.server puerto
    
### Ingrese en su navegador en

    http://127.0.0.1:8000

### Termine el proceso del servidor 
    
    CTRL+C
