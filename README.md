# py-lambda-utils
> 

Este repositorio es la primer prueba para la construccion de una libreria en python 3.8 para funcionalidades frecuentes que uso en las lambdas de AWS.

## Construcción del ambiente
```sh
$  sudo apt-get update && sudo apt-get upgrade     
$  sudo apt-get install virtualenv
$  virtualenv --python=python3.8 env
$  source env/bin/activate
```

## Pre requisitos
```sh
$  pip install -r requirements.txt
```

## Guardar nuevos pre requisitos
```sh
$  pip freeze > requirements.txt
```