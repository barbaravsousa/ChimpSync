import json

import requests as requests
from typing import List
from models import Contact

from settings import API_KEY_OMETRIA, OMETRIA_URL


def export_to_ometria(contacts_batch: List[Contact]):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': API_KEY_OMETRIA}

    payload = [
        {
            "id": contact.id,
            "firstname": contact.firstname,
            "lastname": contact.lastname,
            "email": contact.email,
            "status": contact.status,
        } for contact in contacts_batch
    ]

    response = requests.post(OMETRIA_URL, json=payload, headers=headers)

    if response.status_code == 200:
        print('POST request successful!')
    else:
        raise Exception(f'POST request failed with status code {response.status_code}')
