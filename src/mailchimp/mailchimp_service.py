import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import os

class MailchimpService:
    def __init__(self):
        self.client = MailchimpMarketing.Client()
        self.client.set_config(
            {
                "api_key": os.getenv("API_KEY_MAILCHIMP"),
                "server": os.getenv("MAILCHIMP_SERVER"),
            }
        )
        
    def get_contacts_list(self):
        try:
            response = self.client.lists.get_list_members_info("list_id")
            return response
        except ApiClientError as error:
            print("Error: {}".format(error.text))
