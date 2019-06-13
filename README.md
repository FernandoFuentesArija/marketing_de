# marketing_de

El objetivo de este proyecto es crear un motor de decisión de marketing.

La memoria de este proyecto se encuentra en:
* DOCUMENTATION/MarketingDecisionEngine.pdf

# Guia de instalación

## 1. Git

Primero instalamos `Git`.

### En Linux
Si estamos usando un `SO` Linux basado en Debian o Ubuntu, podemos hacer:
```lang=shell
apt-get install git
```

### En Windows
Si estamos usando Windows existen muchas formas posibles de instalar `Git`, una de las mejores es utilizando
[chocolatey](https://chocolatey.org/), que es un gestor de paquetes para Windows. Para instalarlo sigue
[las instrucciones dadas en su proyecto](https://chocolatey.org/install).

Una vez instalado chocolatey solo tendras que abrir la linea de comandos como administrador  pulsando {icon windows},
tecleando `cmd`, y pulsando {key Ctrl shift Enter} para lanzar la instruccion:
```lang=shell
choco install git
```

Si ya tienes `Git` instalado y solo quieres actualizarlo, sera suficiente con lanzar el comando:
```lang=shell
choco upgrade git
```

(NOTE) En la documentacion de la pagina web de `chocolatey` existe
[mas informacion sobre como usar esta herramienta desde la linea de comandos](https://chocolatey.org/docs/commands-reference)

## 2. Python y pip

Instalamos una version `3.6` de `Python` y, si fuera necesario, instalamos o actualizamos su correspondiente `pip`.

### En Linux
Podemos comprobar si `Python` esta instalado lanzando:
```lang=shell
python3 --version
```
o
```lang=shell
python3.6 --version
```

Si estamos usando un `SO` Linux basado en Debian o Ubuntu, para instalar `python` podremos ejecutar los siguientes
comandos:
```lang=shell
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6
python3.6 --version
```
y despues instalamos la herramienta `pip` que permite instalar los modulos de `python`:
```lang=shell
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install -U pip
```

### En Windows
Para instalar `Python` y `pip` en Windows vamos a volver a usar `chocolatey`. Asi, para comprobar la version actual de
`Python` lanzaremos:
```lang=shell
python --version
```

Si no se tratase de la version deseada (`3.6`) podemos comprobar que versiones de `Python 3.6` hay disponibles usando el
comando:
```lang=shell
choco list python3 --all-versions
```

o comprobar si existe una version en concreto lanzando:
```lang=shell
choco list python3 --version=3.6.X
```
donde `X` sera el numero especifico de la version

Una vez nos hemos asegurado de que queremos instalar la version `3.6.X` y de que dicha version esta disponible, podremos
instalarla ejecutando:
```lang=shell
choco install python3 --version=3.6.X
```
esto deberia instalar `pip` automaticamente ya que todas las versiones de `Python 3` lo incluyen, podemos comprobarlo
lanzando:
```lang=shell
pip --version
```

y actulizarlo si fuera necesario con el comando:
```lang=shell
python -m pip install -U pip
```

Tenemos que instalar las siguientes librerías
```lang=shell
pip3 install pymongo
pip3 install matplotlib
pip3 install pandas
```


## 3. IDE: PyCharm y clonado del proyecto

### El IDE: PyCharm
Para el desarrollo de este proyecto, estamos utilizando `PyCharm` como IDE.
Nos iremos a la pagina de [JetBrains](https://www.jetbrains.com/) y desde alli nos descargaremos el software de gestion
de herramientas que tienen:
- [TOOLBOX](https://www.jetbrains.com/toolbox/app/)

Utilizando `Toolbox`, instalaremos la version de `PyCharm` deseada.

(NOTE) `Toolbox` tambien nos servira para ir actualizando el IDE en el futuro.

### Clonado del proyecto
Una vez tenemos `PyCharm` instalado, debemos clonar el proyecto.

Para ello abrimos el IDE y en la pantalla de nuevo proyecto que se nos presenta vamos a la ruta:

{nav VCS >
Checkout from Version Control >
Git}

(NOTE) La ruta del repositorio es: https://github.com/FernandoFuentesArija/marketing_de.git

Una vez introducida la ruta, hacemos click sobre el boton **{key Clone}**.


## 4. Persistencia

Para la persistencia de los datos en este prototipo utilizamos actualmente una base de datos `MongoDB 3.4.6`
configurada tal y como viene por defecto:

    host: localhost
    port: 27017

Arrancamos la BBDD y el siguiente paso va a consistir en cargar una serie de ficheros json que hay en la ruta:
* bbdd_manager/mongoImports

Estos ficheros contienen configuración y ejemplos que vamos a necesitar.

Las sentencias a lanzar en sistemas Linux están en la ruta:
```lang=shell
bbdd_manager/mongoImports/importAll_unix
```


Las sentencias a lanzar en sistemas Windows están en la ruta:
```lang=shell
bbdd_manager/mongoImports/importAll_win.bat
```

(IMPORTANT) Primero se deberan configurar de manera correcta las rutas donde esta instalado `MongoDB` y donde se hayan
dejado los ficheros `.json` que se van a cargar.


