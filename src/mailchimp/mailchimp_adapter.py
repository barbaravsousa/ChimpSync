
from IImporter import IImporter
from mailchimp.mailchimp_mapper import parse_contact_list
from mailchimp.mailchimp_service import MailchimpService
from settings import BATCH_SIZE


class MailchimpAdapter(IImporter):

    def __init__(self):
        self.mailchimp_service = MailchimpService()

    def get_contact_lists(self, last_sync_time: str):
        all_lists = self.mailchimp_service.get_all_list()
        for contact_list in all_lists:
            list_id = contact_list["id"]
            total_contacts = contact_list["stats"]["member_count"]
            processed = 0
            while processed < total_contacts:
                mailchimp_list_of_contacts = self.mailchimp_service.get_contacts_list(list_id, last_sync_time,
                                                                                      processed, BATCH_SIZE)
                if mailchimp_list_of_contacts:
                    yield parse_contact_list(mailchimp_list_of_contacts)
                processed += BATCH_SIZE
