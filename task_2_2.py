from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # class' realisation

class Phone(Field):
    # class' realisation

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # class' realisation

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # class' realisation