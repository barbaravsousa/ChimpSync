from abc import ABC, abstractmethod
from datetime import datetime


class IImporter(ABC):
    @abstractmethod
    def get_contact_lists(self, last_sync_time: str):
        pass
