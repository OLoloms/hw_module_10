from collections import UserDict

class AdressBook(UserDict):
    def add_record(self, record):
        self[record.name] = record.list_phone
    def show_data(self):
        return self.data

class Record:
    def set_name(self, name):
        self.name = name.name
    def set_phone(self, *phones):
        self.list_phone = []
        for phone in phones:
            self.list_phone.append(phone.phone)
        
    def change_phone(self, previous_phone, new_phone):
        index = self.list_phone.index(previous_phone.phone)
        self.list_phone[index] = new_phone.phone
    def add_phone(self, phone):
        self.list_phone.append(phone.phone)
    def delete_phone(self, phone):
        self.list_phone.remove(phone.phone)

class Field:
    pass
class Name:
    def __init__(self, name) -> None:
        self.name = name
class Phone:
    def __init__(self, phone) -> None:
        self.phone = phone