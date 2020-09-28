from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def __str__(self):
        pass

class Note(Item):
    def __init__(self, title, content):
        super().__init__("Note")
        self.title = title
        self.content = content

    def __str__(self):
        info = self.type + '\n\n'
        info += self.title + '\n'*2
        info += self.content
        return info

class Business_card(Item):
    def __init__(self, name, surname, phone_number):
        super().__init__("Business card")
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        info = self.type + '\n'
        info += self.name + '\n' * 2
        info += self.surname + '\n' * 2
        info += self.phone_number
        return info

class Discount_coupon(Item):
    def __init__(self,company, expiry_date):
        super().__init__("Discount Coupon")
        self.company = company
        self.expiry_date = expiry_date

    def __str__(self):
        info = self.type + '\n'
        info += self.company + '\n' *2
        info += self.expiry_date
        return info
