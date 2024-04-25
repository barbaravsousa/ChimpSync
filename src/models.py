from pydantic import BaseModel


class Contact(BaseModel):
    id: str
    firstname: str
    lastname: str
    email: str
    status: str
