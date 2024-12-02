import time

def get_time(init_time):
	timer = time.perf_counter() - init_time
	print("Tiempo de ejecución:",timer,"seg")