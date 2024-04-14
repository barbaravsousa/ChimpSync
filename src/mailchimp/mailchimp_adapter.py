from typing import List

from IImporter import IImporter
from mailchimp.mailchimp_mapper import parse_contact_list
from mailchimp.mailchimp_service import MailchimpService
from models import ListOfContacts


class MailchimpAdapter(IImporter):
    def __init__(self):
        self.mailchimp_service = MailchimpService()

    def get_contact_lists(self) -> List[ListOfContacts]:
        lists_of_contacts = []
        all_lists = self.mailchimp_service.get_all_list()
        for contact_list in all_lists:
            list_id = contact_list["id"]
            mailchimp_list_of_contacts = self.mailchimp_service.get_contacts_list(list_id)
            list_of_contacts = parse_contact_list(mailchimp_list_of_contacts)
            lists_of_contacts.append(list_of_contacts)

        return lists_of_contacts
