import os

from dotenv import load_dotenv

from mailchimp.mailchimp_adapter import MailchimpAdapter
from ometria.ometria_service import export_to_ometria
from sync_util import get_last_sync_time, update_last_sync_time

load_dotenv()


def main():
    last_sync_time = get_last_sync_time()
    importer = MailchimpAdapter()
    failed_batches = []

    for contacts_batch in importer.get_contact_lists(last_sync_time):
        try:
            export_to_ometria(contacts_batch)
            update_last_sync_time()
        except Exception as e:
            print(f"Failed to send batch: {e}")
            failed_batches.append(contacts_batch)

    if failed_batches:
        pass


if __name__ == "__main__":
    main()
