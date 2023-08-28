import os
import re

# Finding json file in GAIA directory
for filename in os.listdir('.'):
    if filename.endswith('.json'):
        json_file = filename
        break

# Writing json filename into variable
service_acc_filename = json_file

service_acc_mail = ''

# Finding service account email
with open(json_file, 'r') as file:
    for line in file:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
        match = re.search(regex, line)
        if match:
            service_acc_mail = match.group()
            break

# Creating credentials file
with open('ee_creds.txt', 'w') as file:
    file.write(str(service_acc_filename + '\n'))
    file.write(str(service_acc_mail))
    print('EE credential file was successfully created')


