from typing import Dict, List

from models import Contact


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


# Maps the Mailchimp contact list to a List<Contact>
def parse_contacts_list(mailchimp_contact_list: Dict[str, any]) -> List[Contact]:
    return [parse_contact(contact) for contact in mailchimp_contact_list["members"]]
