import os
import re
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
handler = logging.FileHandler('gee//gaia-gee-errors.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

service_acc_filename = ''
service_acc_mail = ''

# Finding json file in GAIA directory
for filename in os.listdir('.'):
    if filename.endswith('.json'):
        service_acc_filename = filename
        break

# Finding service account email
try:
    with open(service_acc_filename, 'r') as file:
        for line in file:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
            match = re.search(regex, line)
            if match:
                service_acc_mail = match.group()
                break
except NameError as error:
    logger.error(error)
    print('')

