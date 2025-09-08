from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from src.repository.contacts import ContactRepository
from src.schemas.contacts import ContactModel


class ContactsService:
    def __init__(self, db: AsyncSession):
        self.contacts_repository = ContactRepository(db)

    async def create_contact(self, body: ContactModel):
        return await self.contacts_repository.create_contact(body)

    async def get_contacts(self, skip: int, limit: int, query_params: dict):
        return await self.contacts_repository.get_contacts(skip, limit, query_params)

    async def get_contact(self, contact_id: int):
        return await self.contacts_repository.get_contact_by_id(contact_id)

    # TODO: check body to be processed
    async def update_contact(self, contact_id: int, body: ContactModel):
        return await self.contacts_repository.update_contact(contact_id, body)

    async def remove_contact(self, contact_id: int):
        return await self.contacts_repository.remove_contact(contact_id)

    async def get_contacts_with_upcoming_birthdays(self):
        return await self.contacts_repository.get_contacts_with_upcoming_birthdays()
