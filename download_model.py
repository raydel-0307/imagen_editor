import json
from minio_db import *


def fuctions_execute(config_json_path: str):
    # Leer el archivo de configuración
    with open(config_json_path, 'r', encoding='utf-8') as file:
        config = json.load(file)

    #Ruta del proyecto
    ruta = config["proyect"]
    with open(f"{ruta}/{config_json_path}", 'r', encoding='utf-8') as file:
        config = json.load(file)
        
    # Usar los valores del archivo JSON
    model_name = config["model_name"]

    # Llamar al modelo y mostrar los resultados
    download_model(model_name, "model.pkl", dir_path=ruta, timeout=3000)


def main():

    config_json_path = "config.json"

    result = fuctions_execute(config_json_path)

if __name__ == "__main__":
    main()
