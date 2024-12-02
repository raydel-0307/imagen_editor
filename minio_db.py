import os
import requests
import pickle
from requests.exceptions import RequestException

def download_model(input_model_name, output_model_name, dir_path=None, timeout=30):
    url = 'http://192.168.1.29:8000/api/spark/download_pkl_from_minio/'
    try:
        response = requests.post(url,data={'model_name': input_model_name},timeout=timeout)
        if response.status_code == 200:
            file_name = output_model_name
            if dir_path:file_name = f"{dir_path}/{output_model_name}"
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"File downloaded and saved successfully as '{file_name}'")
        else:
            print(f"Error: {response.status_code}")
            print(response.json())
    except RequestException as e:
        print(f"Request failed: {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")

def upload_model(model_name,model_path,timeout=30):
    if not model_path:
        print("No se ingresó ninguna ruta de archivo.")
        exit()
    with open(model_path, 'rb') as file:
        file_data = file.read()
    url = 'http://192.168.1.29:8000/api/spark/upload_pkl_to_minio/'  
    try:
        files = {'file': (model_path, file_data, 'application/octet-stream')}
        response = requests.post(url,files=files,data={'object_name': model_name},timeout=timeout)
        if response.status_code == 200:
            print("Archivo subido exitosamente")
            print(response.json())
        else:
            print(f"Error: {response.status_code}")
            print(response.json())

    except RequestException as e:
        print(f"Fallo en la solicitud: {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")