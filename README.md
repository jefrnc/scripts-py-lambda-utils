# py-lambda-utils
> 

Este repositorio es la primer prueba para la construccion de una libreria en python 3.8 para funcionalidades frecuentes que uso en las lambdas de AWS.

## Construcción del ambiente
```sh
$  sudo apt-get update && sudo apt-get upgrade     
$  sudo apt-get install virtualenv
$  virtualenv --python=python3.8 env
$  source env/bin/activate
$  #deactivate
```

## Pre requisitos
```sh
$  pip install -r requirements.txt
```

## Guardar nuevos pre requisitos
Si agregamos nuevos requisitos es importante plasmarlo en el archivo requirements.txt
```sh
$  pip freeze > requirements.txt
```

## Corremos los test
Con este comando ejecutamos el test
```sh
$  python setup.py pytest
```

## Build library

Ejecutamos el setup y estos nos genera un archivo whl en la carpeta /dist

```sh
$  python3.8 setup.py bdist_wheel
$  ls dist
mypythonlib-0.1.0-py3-none-any.whl
```
