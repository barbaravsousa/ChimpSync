from abc import ABC, abstractmethod

class IImporter(ABC):
    @abstractmethod
    def get_contact_lists(self):
        pass
    
    
    


