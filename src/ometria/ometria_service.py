import os

import requests as requests

from models import ListOfContacts

URL = os.getenv("OMETRIA_URL")

API_KEY = os.getenv("API_KEY_OMETRIA")


def export_to_ometria(contacts_batch: ListOfContacts):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': API_KEY}

    response = requests.post(URL, json=contacts_batch, headers=headers)

    if response.status_code == 200:
        print('POST request successful!')
    else:
        print(f'POST request failed with status code {response.status_code}')  # Mandar exeção
