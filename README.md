# Stable Diffusion

## Versión 2

## Cambios realizados

* Se mejoró el modelo y tiene una mejor prescición
* Acepta prompt tanto ESP como ENG
* Puede ingresar la imagen tanto URL como el PATH en local
* Agregado el cálculo del tiempo de ejecución tando del `entrenamiento` como el de `ejecución` del modelo
* Cambio en el método de exportación, ahora se usa `minio`

## ¿ Como se configura ?

1. En la raíz del proyecto existe un archivo `config.json`, ahí debe de poner el nombre del proyecto a ejecutar 


```json
{
	"proyect":"example"
}
```

2. Dentro de ese directorio debe existir otro archivo `config.json` que contendrá la siguiente configuración


```json
{
	"model_name":"timbrooks/instruct-pix2pix",
	"image_path":"https://raw.githubusercontent.com/timothybrooks/instruct-pix2pix/main/imgs/example.jpg",
	"prompt":"turn him into cyborg"
}
```

* model_name: Es el nombre del modelo que se va a ejecutar
* image_path: Es un string que contiene el path o url de la imagen
* promt: Es un string que contiene el prompt de la modificación que se va a realizar, tanto en inglés como en español