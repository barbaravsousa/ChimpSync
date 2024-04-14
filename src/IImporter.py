from abc import ABC, abstractmethod
from typing import List

from models import ListOfContacts


class IImporter(ABC):
    @abstractmethod
    def get_contact_lists(self) -> List[ListOfContacts]:
        pass
