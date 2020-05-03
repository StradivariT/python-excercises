from __future__ import annotations

import json
import uuid

class User:
    users = 0

    def __init__(self, id: str, name: str, email: str, phone: str, address: str):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

        self.__class__.users += 1

    def __del__(self):
        self.__class__.users -= 1

    def __repr__(self):
        return f'''ID: { self.id }\nName: { self.name }\nEmail: { self.email }\nPhone: { self.phone }\nAddress: { self.address }\n'''

    @classmethod
    def fromInput(cls) -> User:
        print("Enter the following values for the new user:")
        
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        address = input("Address: ")
        
        return cls(str(uuid.uuid4()), name, email, phone, address)

    @classmethod
    def fromDict(cls, inputDict) -> User:
        return cls(**inputDict)

    @classmethod
    def isEmpty(cls) -> bool:
        return cls.users == 0

    def modify(self):
        print("Enter the following values to modify the user:")

        self.name = input("Name: ")
        self.email = input("Email: ")
        self.phone = input("Phone: ")
        self.address = input("Address: ")