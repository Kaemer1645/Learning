from items import Note, Business_card, Discount_coupon

class Organizer:

    __data_base = []
    def __init__(self, owner):
        self.owner = owner

    def add_note(self):
        title = input('Title: ')
        content = input('Content: ')

        new_note = Note(title,content)
        self.__data_base.append(new_note)

    def add_business_card(self):
        name = input('Name: ')
        surname = input('Surname: ')
        phone_number = input('Phone number: ')

        new_bsns_card = Business_card(name, surname, phone_number)
        self.__data_base.append(new_bsns_card)

    def add_discount_coupon(self):
        company = input('Company: ')
        expiry_date = input('Expiry date: ')
        new_coupon = Discount_coupon(company,expiry_date)
        self.__data_base.append(new_coupon)

    def display_notes(self):
        print('Notes list')
        for x in self.__data_base:
            if x.type == 'Note':
                print(x)

    def display_bsns_card(self):
        print('Business card list')
        for x in self.__data_base:
            if x.type == 'Business card':
                print(x)

    def display_discount_coupon(self):
        print('Discount Coupon list')
        for x in self.__data_base:
            if x.type == 'Discount Coupon':
                print(x)


    def get_db(self):
        self.data_base = self.__data_base
        return self.data_base

    def delete_display(self):
        user_delete = input('Which element you want to delete?')
        for files in self.__data_base:
            if files.type == user_delete:
                self.__data_base.remove(files)