import time

from mailchimp.mailchimp_adapter import MailchimpAdapter
from ometria.ometria_service import export_to_ometria
from settings import SYNC_INTERVAL_HOURS, SYNC_PRECISION_SECONDS
from sync_util import get_last_sync_time, update_last_sync_time
import schedule


def sync_contacts():
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


# Schedules the sync_contacts job to run every {SYNC_INTERVAL_HOURS}
# with a precision of {SYNC_PRECISION_SECONDS}
def setup_schedule():
    schedule.every(SYNC_INTERVAL_HOURS).hours.do(sync_contacts)
    while True:
        schedule.run_pending()
        time.sleep(SYNC_PRECISION_SECONDS)


if __name__ == "__main__":
    sync_contacts()
    setup_schedule()
