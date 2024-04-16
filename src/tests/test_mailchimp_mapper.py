import unittest
from mailchimp.mailchimp_mapper import parse_contact, parse_contacts_list
from models import Contact


class TestParsingMethods(unittest.TestCase):

    def test_parse_contact(self):
        mailchimp_contact = {
            "contact_id": "123",
            "email_address": "thor@gmail.com",
            "status": "subscribed",
            "merge_fields": {
                "FNAME": "Thor",
                "LNAME": "Odinson"
            }
        }

        expected_contact = Contact(id="123", firstname="Thor", lastname="Odinson", email="thor@gmail.com",
                                   status="subscribed")

        self.assertEqual(parse_contact(mailchimp_contact), expected_contact)

    def test_parse_contact_missing_fields(self):
        mailchimp_contact = {
            "contact_id": "456",
            "email_address": "jane@gmail.com",
            "status": "unsubscribed",
        }
        expected_contact = Contact(id="456", firstname="", lastname="", email="jane@gmail.com",
                                   status="unsubscribed")
        self.assertEqual(parse_contact(mailchimp_contact), expected_contact)

    def test_parse_contact_list(self):
        mailchimp_contact_list = {
            "members": [
                {
                    "contact_id": "123",
                    "email_address": "ironman@gmail.com",
                    "status": "subscribed",
                    "merge_fields": {
                        "FNAME": "Iron",
                        "LNAME": "Man"
                    }
                },
                {
                    "contact_id": "456",
                    "email_address": "peterparker@gmail.com",
                    "status": "unsubscribed",
                }
            ]
        }
        expected_contacts = [
            Contact(id="123", firstname="Iron", lastname="Man", email="ironman@gmail.com", status="subscribed"),
            Contact(id="456", firstname="", lastname="", email="peterparker@gmail.com", status="unsubscribed")
        ]
        self.assertEqual(parse_contacts_list(mailchimp_contact_list), expected_contacts)

    def test_parse_empty_list(self):
        mailchimp_contact_list = {"members": []}
        expected_contacts = []
        self.assertEqual(parse_contacts_list(mailchimp_contact_list), expected_contacts)
