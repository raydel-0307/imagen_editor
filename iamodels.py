import PIL
import torch
from diffusers import StableDiffusionInstructPix2PixPipeline, EulerAncestralDiscreteScheduler
import pickle
from random import randint
from minio_db import MinioManager
from metrics import get_time
import time
import requests
import os

def make_image(image_path):

	if "https://" or image_path or "http://" in image_path:
		image = PIL.Image.open(requests.get(url, stream=True).raw)
	else:
		image = PIL.Image.open(image_path)

	image = PIL.ImageOps.exif_transpose(image)
	image = image.convert("RGB")

	return image


def TrainModel(dir_path,model_name):

	init_time = time.perf_counter()

	pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(model_name, torch_dtype=torch.float16, safety_checker=None).to("cuda")

	pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)

	model_path = f'{dir_path}/model.pkl'

	with open(model_path, 'wb') as f:
		pickle.dump(pipe, f)

	minio_manager = MinioManager()
	minio_manager.upload_model(model_name, model_path)

	os.unlink(model_path)

	print("Modelo Gurdado")

	get_time(init_time)


def MainModel(dir_path,prompt,image_path,model_name):

	init_time = time.perf_counter()
	
	minio_manager = MinioManager()
	pipe = minio_manager.download_model(model_name)

	image = make_image(image_path)
	
	images = pipe(prompt, image=image, num_inference_steps=10, image_guidance_scale=1).images
	
	img_name = f"{dir_path}/img_{randint(10000,99999)}.png"
	images[0].save(img_name)

	print(f"Imagen guardada en {img_name}")

	get_time(init_time)