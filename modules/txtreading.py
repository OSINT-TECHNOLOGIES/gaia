from colorama import Fore
import mercury as mr

def ds_info_read():
    try:
        with open("data/ee_ds.txt", "r") as periods:
            mr.Markdown(text="**AVAILABLE TIME-PERIODS AND BANDS FOR GEE DATASETS**")
            line = periods.readline()
            while line:
                line = periods.readline()
                mr.Markdown(text=line)
    except FileNotFoundError as error:
        print(Fore.RED + '[File/directory missing error] -{}'.format(str(error)[9:]))

def ee_guide_read():
    try:
        with open("data/ee_guide.txt", "r") as guide:
            mr.Markdown(text = "**HOW TO START WORKING WITH GOOGLE EARTH ENGINE**")
            line = guide.readline()
            while line:
                line = guide.readline()
                mr.Markdown(text=line)
    except FileNotFoundError as error:
        print(Fore.RED + '[File/directory missing error] -{}'.format(str(error)[9:]))
