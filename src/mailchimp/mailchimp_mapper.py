from typing import Dict

from models import Contact, ListOfContacts


# Maps the Mailchimp contact to Contact type
def parse_contact(mailchimp_contact: Dict[str, any]) -> Contact:
    firstname = mailchimp_contact.get('merge_fields', {}).get('FNAME', '')
    lastname = mailchimp_contact.get('merge_fields', {}).get('LNAME', '')

    return Contact(
        id=mailchimp_contact["contact_id"],
        firstname=firstname,
        lastname=lastname,
        email=mailchimp_contact["email_address"],
        status=mailchimp_contact["status"]
    )


# Maps the Mailchimp contact list to ListOfContacts type
def parse_contact_list(mailchimp_contact_list: Dict[str, any]) -> ListOfContacts:
    return ListOfContacts(
        id=mailchimp_contact_list["list_id"],
        contacts=[parse_contact(contact) for contact in mailchimp_contact_list["members"]]
    )
