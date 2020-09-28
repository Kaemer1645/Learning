from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.boxlayout import BoxLayout

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
            
            
        MDRaisedButton:
            text: "Add discount coupon"
            md_bg_color: 0.4, 1, 0.2, 1
            size_hint: 0.25, 0.08
            pos_hint: {'center_x':0.3,'center_y':0.6}
            
            
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
        
        
        MDRaisedButton:
            text: "Display discount coupons"
            md_bg_color: 0.4, 1, 0.2, 1
            size_hint: 0.25, 0.08
            pos_hint: {'center_x':0.3,'center_y':0.3}
            
            
        MDRaisedButton:
            text: "Create database"
            md_bg_color: 0.4, 1, 0.2, 1
            size_hint: 0.25, 0.08
            pos_hint: {'center_x':0.6,'center_y':0.4}
        
        
        MDRaisedButton:
            text: "Display database"
            md_bg_color: 0.4, 1, 0.2, 1
            size_hint: 0.25, 0.08
            pos_hint: {'center_x':0.6,'center_y':0.3}
        
        
    

            
            
<Content>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"

    MDTextField:
        hint_text: "City"

    MDTextField:
        hint_text: "Street"
               
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
                title="Address:",
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



if __name__ == '__main__':
    OrganizerApp().run()