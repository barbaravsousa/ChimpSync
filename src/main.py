import logging
import time
from datetime import datetime

import schedule

from mailchimp.mailchimp_adapter import MailchimpAdapter
from ometria.ometria_service import export_to_ometria
from settings import SYNC_INTERVAL_HOURS, SYNC_PRECISION_SECONDS, FAILED_BATCHES
from sync_util import get_last_sync_time, update_last_sync_time

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def sync_contacts():
    last_sync_time = get_last_sync_time()
    importer = MailchimpAdapter()
    failed_batches = []
    batch_counter = 0

    for contacts_batch in importer.get_contact_lists(last_sync_time):
        try:
            export_to_ometria(contacts_batch)
            update_last_sync_time()
            batch_counter += 1
            logging.info(f'Batch processed: {batch_counter}')
        except Exception as e:
            print(f"Failed to send batch: {e}")
            failed_batches.append(contacts_batch)

    logging.info(f'Contact lists exported to Ometria with {len(failed_batches)} failed batches')

    if failed_batches:
        with open(FAILED_BATCHES, 'a') as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            for batch in failed_batches:
                for contact in batch:
                    file.write(f"{timestamp}: {contact.id}\n")


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
