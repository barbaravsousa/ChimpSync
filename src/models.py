from typing import List
from pydantic import BaseModel

class Contact(BaseModel):
    id: str
    firstname: str
    lastname: str
    email: str
    status: str

class ListOfContacts(BaseModel):
    id: str
    contacts: List[Contact]

class ClientAccount(BaseModel):
    id: str
    contact_lists: List[ListOfContacts]