from collections import UserDict

class AdressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.name] = record

class Record:
    def __init__(self, name, *field) -> None:
        self.name = name
        self.field = list(field) or []

class Field:
    pass

class Name:
    def __init__(self, name) -> None:
        self.name = name

class Phone:
    def __init__(self, phone=None) -> None:
        self.value = phone

if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AdressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].field, list)
    assert isinstance(ab['Bill'].field[0], Phone)
    assert ab['Bill'].field[0].value == '1234567890'
    print('All Ok)')