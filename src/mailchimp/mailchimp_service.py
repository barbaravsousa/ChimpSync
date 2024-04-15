from typing import Optional

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

from settings import API_KEY_MAILCHIMP, MAILCHIMP_SERVER, BATCH_SIZE


class MailchimpService:
    def __init__(self):
        self.client = MailchimpMarketing.Client()
        self.client.set_config(
            {
                "api_key": API_KEY_MAILCHIMP,
                "server": MAILCHIMP_SERVER,
            }
        )

    def get_all_list(self):
        try:
            response = self.client.lists.get_all_lists()
            return response["lists"]
        except ApiClientError as error:
            print("Error: {}".format(error.text))

    def get_contacts_list(self, list_id: str, last_sync_time: Optional[str], processed=0, batch_size=BATCH_SIZE):
        params = {'offset': processed, 'count': batch_size, 'since_last_changed': last_sync_time}
        try:
            response = self.client.lists.get_list_members_info(list_id, **params)
            return response
        except ApiClientError as error:
            print("Error: {}".format(error.text))
