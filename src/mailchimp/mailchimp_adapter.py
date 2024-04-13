import IImporter
import mailchimp_service as MailchimpService

class MailchimpAdapter(IImporter):
    def __init__(self):
        self.client = MailchimpService()
        

    def get_contact_lists(self):
        return self.client.get_contacts_list()