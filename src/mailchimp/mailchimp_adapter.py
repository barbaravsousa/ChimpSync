from IImporter import IImporter
from mailchimp.mailchimp_mapper import parse_contact_list
from mailchimp.mailchimp_service import MailchimpService
from settings import BATCH_SIZE


class MailchimpAdapter(IImporter):

    def __init__(self):
        self.mailchimp_service = MailchimpService()

    def get_contact_lists(self, last_sync_time: str):
        # Gets all the lists for a certain client
        all_lists = self.mailchimp_service.get_all_list()
        for contact_list in all_lists:
            list_id = contact_list["id"]
            # Obtains the total of contacts present in each contact list
            total_contacts = contact_list["stats"]["member_count"]
            # Number of contact lists that were fetched and mapped
            processed = 0
            while processed < total_contacts:
                # Gets the contacts list, considering the last sync time,
                # the current number os processed and the batch size
                mailchimp_list_of_contacts = self.mailchimp_service.get_contacts_list(list_id, last_sync_time,
                                                                                      processed, BATCH_SIZE)
                if mailchimp_list_of_contacts:
                    yield parse_contact_list(mailchimp_list_of_contacts)
                processed += BATCH_SIZE
