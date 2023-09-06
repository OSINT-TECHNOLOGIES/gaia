import os
import re

# Finding json file in GAIA directory
for filename in os.listdir('.'):
    if filename.endswith('.json'):
        service_acc_filename = filename
        break


# Writing json filename into variable
service_acc_mail = ''

# Finding service account email
try:
    with open(json_file, 'r') as file:
        for line in file:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
            match = re.search(regex, line)
            if match:
                service_acc_mail = match.group()
                break
except NameError as error:
    print('')