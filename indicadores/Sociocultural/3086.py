from . import *

with open(SOCIOCUL_FILE, "r") as json_file:
    data_list = json.load(json_file)

process = processor.from_json(data_list['3086'])

# Carrega, processa e salva o resultado
process.process_dataframe()