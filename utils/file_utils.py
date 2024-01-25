import os
import random
import math

def list_and_sort_files(data_path):
    # Verifica si la carpeta existe
    if not os.path.exists(data_path):
        print(f"La carpeta {data_path} no existe.")
        return None  # Retorna None si la carpeta no existe
    
    files = [file for file in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, file))]
    
    if len(files) == 0:
        print(f"La carpeta {data_path} no contiene archivos.")
        return None  # Retorna None si la carpeta está vacía

    # Ordena los archivos alfabéticamente manteniendo el orden numérico
    sorted_files = sorted(files, key=lambda x: int(''.join(filter(str.isdigit, x))))
    return sorted_files

    