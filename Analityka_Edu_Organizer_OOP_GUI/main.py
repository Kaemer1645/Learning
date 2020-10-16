from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from organizer import Organizer
from create_db import Data_base
organizer_instance = Organizer('Szymon Sleczka')
db = Data_base()
KV = '''
Screen:
    MDLabel:
        text: "This is organizer app"
        pos_hint: {'center_x':0.5,'center_y':0.9}
        halign:"center"
        
        
    FloatLayout:
    
        MDRaisedButton:
            text: "Add Note"
            md_bg_color: 0.4, 1, 0.2, 1
            size_hint: 0.25, 0.08
            pos_hint: {'center_x':0.3,'center_y':0.8}
            on_release: app.show_confirmation_dialog()
        
        
        MDRaisedButton:
            text: "Add business card"
            md_bg_color: 0.4, 1, 0.2, 1
            size_hint: 0.25, 0.08
            pos_hint: {'center_x':0.3,'center_y':0.7}
            on_release: app.business_card()

            
        MDRaisedButton:
            text: "Add discount coupon"
            md_bg_color: 0.4, 1, 0.2, 1
            size_hint: 0.25, 0.08
            pos_hint: {'center_x':0.3,'center_y':0.6}
            on_release: app.discount_coupon()
            
        MDRaisedButton:
            text: "Display notes"
            md_bg_color: 0.4, 1, 0.2, 1
            size_hint: 0.25, 0.08
            pos_hint: {'center_x':0.3,'center_y':0.5}
        
        
        MDRaisedButton:
            text: "Display business cards"
            md_bg_color: 0.4, 1, 0.2, 1
            size_hint: 0.25, 0.08
            pos_hint: {'center_x':0.3,'center_y':0.4}
            on_release: app.disp_business_card()

        MDRaisedButton:
            text: "Display discount coupons"
            md_bg_color: 0.4, 1, 0.2, 1
            size_hint: 0.25, 0.08
            pos_hint: {'center_x':0.3,'center_y':0.3}
            on_release: app.disp_discount_coupon()

            
        MDRaisedButton:
            text: "Create database"
            md_bg_color: 0.4, 1, 0.2, 1
            size_hint: 0.25, 0.08
            pos_hint: {'center_x':0.6,'center_y':0.4}
            on_release: app.data_base()
        
        MDRaisedButton:
            text: "Display database"
            md_bg_color: 0.4, 1, 0.2, 1
            size_hint: 0.25, 0.08
            pos_hint: {'center_x':0.6,'center_y':0.3}
            on_release: app.disp_data_base()

        
    

            
            
<Content>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"

    MDTextField:
        id: title
        hint_text: "Title"

    MDTextField:
        hint_text: "Content"
               
'''

class Content(BoxLayout):
    pass


class OrganizerApp(MDApp):
    dialog = None
    def build(self):
        return Builder.load_string(KV)

    def close_app(self, *largs):
        super(OrganizerApp, self).stop(*largs)

    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Add Note:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color
                    ),
                ],
            )
        self.dialog.open()

    def business_card(self):
        return organizer_instance.add_business_card()
    def discount_coupon(self):
        return organizer_instance.add_discount_coupon()
    def disp_business_card(self):
        return organizer_instance.display_bsns_card()
    def data_base(self):
        return db.create_db(organizer_instance.get_db())
    def disp_data_base(self):
        return db.disp_db()
if __name__ == '__main__':
    OrganizerApp().run()