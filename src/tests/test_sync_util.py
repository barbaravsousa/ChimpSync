import json
import unittest
from datetime import datetime
import os
import sys

print(sys.path)
from sync_util import get_last_sync_time, update_last_sync_time


class TestLastSyncTime(unittest.TestCase):
    def setUp(self):
        with open('last_sync_time.json', 'w') as file:
            file.write('{"last_sync": "2024-04-01T12:00:00"}')

    def test_get_last_sync_time_existing_file(self):
        last_sync = get_last_sync_time()
        self.assertEqual(last_sync, datetime(2024, 4, 1, 12, 0, 0))

    def test_get_last_sync_time_file_not_exist(self):
        if os.path.exists('last_sync_time.json'):
            os.remove('last_sync_time.json')

        result = get_last_sync_time()

        self.assertIsNone(result)

    def test_update_last_sync_time(self):
        # Get the current datetime
        current_time = datetime.now().isoformat()

        # Call the function to update the last sync time
        update_last_sync_time()

        # Read the content of the last_sync_time.json file
        with open('last_sync_time.json', 'r') as file:
            data = json.load(file)

        # Check if the updated time is after the previous time
        updated_time = datetime.fromisoformat(data['last_sync'])
        self.assertGreaterEqual(updated_time, datetime.fromisoformat(current_time))
