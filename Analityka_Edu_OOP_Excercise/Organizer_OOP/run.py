from organizer import Organizer
from create_db import Data_base
organizer_instance = Organizer('Szymon Sleczka')
db = Data_base()
while True:
    print('What do you want to do? \n'
          '1. Add Note \n'
          '2. Add Business Card \n'
          '3. Add Discount Coupon \n'
          '4. Display notes \n'
          '5. Display Business Cards \n'
          '6. Display Discount Coupon \n' 
          '7. Create db \n' 
          '8. Display db \n' 
          '9. Delte item R\n'
          '10. Exit')

    inpt = int(input())

    if inpt == 1: organizer_instance.add_note()
    if inpt == 2: organizer_instance.add_business_card()
    if inpt == 3: organizer_instance.add_discount_coupon()
    if inpt == 4: organizer_instance.display_notes()
    if inpt == 5: organizer_instance.display_bsns_card()
    if inpt == 6: organizer_instance.display_discount_coupon()
    if inpt == 7: db.create_db(organizer_instance.get_db())
    if inpt == 8: db.disp_db()
    if inpt == 9: organizer_instance.delete_display()
    if inpt == 10: break
