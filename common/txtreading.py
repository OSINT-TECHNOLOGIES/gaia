from colorama import Fore
import mercury as mr
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
handler = logging.FileHandler('gee//gaia-gee-errors.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def ds_info_read():
    try:
        with open("gee/data/ee_ds.txt", "r") as periods:
            mr.Markdown(text="**AVAILABLE TIME-PERIODS AND BANDS FOR GEE DATASETS**")
            line = periods.readline()
            while line:
                line = periods.readline()
                mr.Markdown(text=line)
    except FileNotFoundError as error:
        logger.error(error)
        print(Fore.RED + '[GEE file/directory missing error] -{}'.format(str(error)))

def ee_guide_read():
    try:
        with open("common/ee_guide.txt", "r") as guide:
            mr.Markdown(text = "**HOW TO START WORKING WITH COMBINED CARTOGRAPHY AND SATELLITE IMAGERY MODULE**")
            line = guide.readline()
            while line:
                line = guide.readline()
                mr.Markdown(text=line)
    except FileNotFoundError as error:
        logger.error(error)
        print(Fore.RED + '[File/directory missing error] -{}'.format(str(error)))

def settings_read():
    try:
        with open("common//settings.json", "r") as guide:
            mr.Markdown(text = "**CURRENT SETTINGS**")
            line = guide.readline()
            while line:
                line = guide.readline()
                mr.Markdown(text=line)
    except FileNotFoundError as error:
        logger.error(error)
        print(Fore.RED + '[File/directory missing error] -{}'.format(str(error)))

def get_min_value(dataset_name):
    with open("common//settings.json", 'r') as file:
        lines = file.readlines()

    start_index = lines.index(f"*{dataset_name}*\n")
    min_line = lines[start_index + 2]
    min_value = float(min_line.split(":")[1].strip())

    return min_value

def get_max_value(dataset_name):
    with open("common//settings.json", 'r') as file:
        lines = file.readlines()

    start_index = lines.index(f"*{dataset_name}*\n")
    max_line = lines[start_index + 3]
    max_value = float(max_line.split(":")[1].strip())

    return max_value

def get_gamma_value(dataset_name):
    with open("common//settings.json", 'r') as file:
        lines = file.readlines()

    start_index = lines.index(f"*{dataset_name}*\n")
    max_line = lines[start_index + 4]
    max_value = float(max_line.split(":")[1].strip())

    return max_value
