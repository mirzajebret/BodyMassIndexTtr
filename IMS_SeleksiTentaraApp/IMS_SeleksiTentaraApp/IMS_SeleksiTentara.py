from re import M, T
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import CardTransition, FadeTransition, FallOutTransition, RiseInTransition, ScreenManager, Screen, SwapTransition
from kivy.uix. boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from kivymd.uix.label import MDLabel

Window.size = (1000, 600)
Builder.load_string("""
<WelcomeScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'assets/welcome.jpg'
    MDTextButton:
        text: 'MULAI'
        #font_name: "assets/Montserrat-Bold.ttf"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.164}
        on_press: root.login_button()
    MDTextButton:
        #font_name: "assets/Montserrat-Medium.ttf"
        text: 'K E L U A R'
        font_style: "Caption"
        on_press: root.tutup()
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.06}

    
<LoginScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'assets/login.jpg'
    #MDLabel:
    #    text: 'IMS/BMI'
    #    pos_hint : {'center_y' : 0.9}
    #    font_style: 'H2'
    #    halign: "center"
    #    #font_name: "KIVYMD/wisata app/Montserrat-Bold.ttf"
    #MDLabel:
    #    text: 'Halaman Login'
    #    pos_hint : {'center_y' : 0.8}
    #    font_style: 'Caption'
    #    halign: "center"
    #    #font_name: "KIVYMD/wisata app/Montserrat-Bold.ttf"
    MDTextField:
        id: uname
        mode: "rectangle"
        hint_text: "Nama"
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.6}
        size_hint_x:None
        width:200
        max_text_length: 15
        helper_text: "masukkan nama"
        helper_text_mode: "on_focus"
    MDTextField:
        id: passw
        password: True
        mode: "rectangle"
        hint_text: "Kata sandi"
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.45}
        size_hint_x:None
        width:200
        max_text_length: 3
        helper_text: "masukkan kata sandi"
        helper_text_mode: "on_focus"
    MDTextButton:
        text: 'MASUK'
        on_press: root.login_button_action()
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        #font_name: "assets/Montserrat-Bold.ttf"
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.3}
        
    MDTextButton:
        #font_name: "assets/Montserrat-Medium.ttf"
        text: 'K E L U A R'
        font_style: "Caption"
        on_press: root.tutup()
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.06}
    MDFloatingActionButton:
        icon: "home"
        md_bg_color: app.theme_cls.primary_color
        x: root.width - self.width - dp(10)
        y: dp(10)
        on_press: root.manager.current = 'welcome'
<DaftarScreen>:
    MDTextField:
        id: daftar_uname
        hint_text: "Username"
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.6}
        size_hint_x:None
        width:200
        max_text_length: 15
        helper_text: "masukkan nama"
        helper_text_mode: "persistent"
    MDTextField:
        id: daftar_passw
        password: True
        hint_text: "Password"
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.5}
        size_hint_x:None
        width:200
        max_text_length: 15
        helper_text: "masukkan password"
        helper_text_mode: "persistent"
    MDRectangleFlatButton:
        text: 'Daftar'
        on_press: root.daftar_button_action()
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.4}

<MainMenu2>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'assets/info_1.jpg'
    
    MDTextButton:
        #font_name: "assets/Montserrat-Medium.ttf"
        text: 'Selanjutnya'
        font_style: "H5"
        on_press: root.BMI_button()
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.15}

    MDTextButton:
        #font_name: "assets/Montserrat-Medium.ttf"
        text: 'K E L U A R'
        font_style: "Caption"
        on_press: root.tutup()
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.06}

    MDFloatingActionButton:
        icon: "account-arrow-left"
        md_bg_color: app.theme_cls.primary_color
        x: root.width - self.width - dp(10)
        y: dp(10)
        on_press: root.manager.current = 'login'
        
<MainMenu>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'assets/info_2.jpg'
    
    MDTextButton:
        #font_name: "assets/Montserrat-Medium.ttf"
        text: 'MULAI IMS'
        font_style: "H5"
        on_press: root.BMI_button()
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.15}

    MDTextButton:
        #font_name: "assets/Montserrat-Medium.ttf"
        text: 'K E L U A R'
        font_style: "Caption"
        on_press: root.tutup()
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.06}

    MDFloatingActionButton:
        icon: "account-arrow-left"
        md_bg_color: app.theme_cls.primary_color
        x: root.width - self.width - dp(10)
        y: dp(10)
        on_press: root.manager.current = 'login'
        
<TaskScreen>:
    ScrollView:
        MDList:
            id: tasklist
    MDFloatingActionButton:
        icon: "plus"
        md_bg_color: app.theme_cls.primary_color
        x: root.width - self.width - dp(10)
        y: dp(10)
        on_press: root.manager.current = 'login' 

<LayarBMI>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'assets/main.jpg'
    #MDLabel:
    #    text: 'Body Mass Index'
    #    pos_hint : {'center_y' : 0.9}
    #    font_style: 'H5'
    #    halign: "center"
    #    #font_name: "KIVYMD/wisata app/Montserrat-Bold.ttf"
    MDLabel:
        text: 'silahkan masukkan tinggi dan berat badan pada kolom dibawah'
        pos_hint : {'center_y' : 0.7}
        font_style: 'Caption'
        halign: "center"
        #font_name: "assets/Montserrat-Bold.ttf"
    MDFloatingActionButton:
        icon: "arrow-left"
        md_bg_color: app.theme_cls.primary_color
        x: root.width - self.width - dp(10)
        y: dp(10)
        on_press: root.manager.current = 'mainmenu' 
    MDTextField:
        id: tinggi
        hint_text: "Tinggi (cm)*"
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.6}
        size_hint_x:None
        width:250
        max_text_length: 3
        helper_text: "isi dengan angka minimal 3 digit"
        helper_text_mode: "on_focus"
    MDTextField:
        id: berat
        hint_text: "Berat (kg)*"
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.5}
        size_hint_x:None
        width:250
        max_text_length: 3
        helper_text: "isi dengan angka minimal 2 digit"
        helper_text_mode: "on_focus"
    MDLabel:
        id: caption
        text : ''
        halign : 'center'
        pos_hint : {'center_x' : 0.45, 'center_y': 0.41}
        theme_text_color : 'Primary'
        font_style : 'Caption'
    MDLabel:
        id: result
        text : ''
        halign : 'center'
        pos_hint : {'center_x' : 0.55,'center_y': 0.41}
        theme_text_color : 'Primary'
        font_style : 'H5'
    MDLabel:
        id: capcap
        text : ''
        halign : 'center'
        pos_hint : {'center_y': 0.28}
        theme_text_color : 'Primary'
        font_style : 'Caption'
    MDTextButton:
        text: 'HITUNG BMI'
        #font_name: "assets/Montserrat-Bold.ttf"
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.164}
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        on_press: root.press_hitung()
    MDTextButton:
        #font_name: "assets/Montserrat-Medium.ttf"
        text: 'K E L U A R'
        font_style: "Caption"
        on_press: root.tutup()
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.06}
""")


class WelcomeScreen(Screen):
    def login_button(self):
        self.manager.current = 'login'

    def tutup_apk(self, instance):
        BMIApp().stop()

    def tutup(self):
        self.dialog_tutup = MDDialog(
                title="Keluar Aplikasi?",
                buttons=[
                    MDFlatButton(
                        text="OKE",
                        on_release=self.tutup_apk
                        ),
                    MDFlatButton(
                        text="BATAL",
                        on_release=self.close_tutup
                        )
                ],
            )
        self.dialog_tutup.open()
            
    def close_tutup(self, instance):
        self.dialog_tutup.dismiss()

class MainMenu2(Screen):
    def BMI_button(self):
        self.manager.current = 'mainmenu'

    dialog_tutup = None

    def tutup_apk(self, instance):
        BMIApp().stop()

    def tutup(self):
        self.dialog_tutup = MDDialog(
                title="Keluar Aplikasi?",
                buttons=[
                    MDFlatButton(
                        text="OKE",
                        on_release=self.tutup_apk
                        ),
                    MDFlatButton(
                        text="BATAL",
                        on_release=self.close_tutup
                        )
                ],
            )
        self.dialog_tutup.open()
            
    def close_tutup(self, instance):
        self.dialog_tutup.dismiss()

class MainMenu(Screen):
    def BMI_button(self):
        self.manager.current = 'layarbmi'

    dialog_tutup = None

    def tutup_apk(self, instance):
        BMIApp().stop()

    def tutup(self):
        self.dialog_tutup = MDDialog(
                title="Keluar Aplikasi?",
                buttons=[
                    MDFlatButton(
                        text="OKE",
                        on_release=self.tutup_apk
                        ),
                    MDFlatButton(
                        text="BATAL",
                        on_release=self.close_tutup
                        )
                ],
            )
        self.dialog_tutup.open()
            
    def close_tutup(self, instance):
        self.dialog_tutup.dismiss()


class LayarBMI(Screen):
#function mengubah input ke index massa tubuh:
    def press_hitung (self):
        try:
            if self.ids.berat.text is not '' and self.ids.tinggi.text is not '':

                tinggi = (float((self.ids.tinggi.text)[0:2]))
                berat = float(self.ids.berat.text)
                
                hitung_kali = tinggi * tinggi
                hitung_bagi = (berat/hitung_kali)
                tostr = str(hitung_bagi)

                self.ids.caption.text = "BMI kamu adalah"
                self.ids.result.text  = tostr[2:4] + ',' + tostr[4:5]

                if hitung_bagi >= 0.185 and hitung_bagi <= 0.25:
                    self.ids.capcap.text = 'Berat Ideal \n \n BMI kamu Ideal, kamu dapat melanjutkan ke tahap selanjutnya\n diet yang baik dapat mempertahankan kesehatan imun'
                
                elif hitung_bagi <= 0.185 and hitung_bagi >= 0.01:
                    self.ids.capcap.text = 'Kurus \n \n BMI kamu tidak ideal,anda belum bisa melanjutkan\n pendaftaran untuk menjadi tentara indonesia\npastikan kebutuhan kalori harian terpenuhi\n dan jangan lupa untuk mengonsumsi makanan sehat'
                
                elif hitung_bagi >= 0.25 and hitung_bagi <= 0.27:
                    self.ids.capcap.text = 'Gemuk \n \nBMI kamu melebihi ideal, anda belum bisa melanjutkan\n pendaftaran untuk menjadi tentara indonesia\npastikan asupan kalori sesuai dengan kebutuhan \nkalori harian dan jangan lupa untuk mengonsumsi makanan sehat'
                
                elif hitung_bagi >= 0.27:
                    self.ids.capcap.text = 'Obesitas \n \nBMI kamu jauh melebihi ideal, anda belum bisa melanjutkan\n pendaftaran untuk menjadi tentara indonesia\nuntuk berkonsultasi dengan dokter dapat menghubungi:\n\n081288880256'

            elif self.ids.berat.text == '' and self.ids.tinggi.text == '':
                self.ids.caption.text = "Kamu belum memasukkan tinggi dan berat badan"
                self.ids.result.text = ''

            elif self.ids.berat.text == '':
                self.ids.caption.text = "Kamu belum memasukkan berat badan"
                self.ids.result.text = ''

            elif self.ids.tinggi.text == '':
                self.ids.caption.text = "Kamu belum memasukkan tinggi badan"
                self.ids.result.text = ''
        except:
            self.ids.caption.text = "Tidak bisa menghitung text!"
            self.ids.result.text = ''

    dialog_tutup = None
    def tutup_apk(self, instance):
        BMIApp().stop()
    def tutup(self):
        self.dialog_tutup = MDDialog(
                title="Keluar Aplikasi?",
                buttons=[
                    MDFlatButton(
                        text="OKE",
                        on_release=self.tutup_apk
                        ),
                    MDFlatButton(
                        text="BATAL",
                        on_release=self.close_tutup
                        )
                ],
            )
        self.dialog_tutup.open()

    def close_tutup(self, instance):
        self.dialog_tutup.dismiss()
        

class TaskScreen (Screen) :
    def on_enter (self):
        for i in range(10):
            self.ids.tasklist.add_widget(
                OneLineListItem (text=f"Filler task {i}")
            )


class LoginScreen(Screen):
#tutup button function:
    def tutup_apk(self, instance):
        BMIApp().stop()

#tutup confirm:
    def tutup(self):
        self.dialog_tutup = MDDialog(
                title="Keluar Aplikasi?",
                buttons=[
                    MDFlatButton(
                        text="OKE",
                        on_release=self.tutup_apk
                        ),
                    MDFlatButton(
                        text="BATAL",
                        on_release=self.close_tutup
                        )
                ],
            )
        self.dialog_tutup.open()

#function menutup pop up dari semua kondisi:
    def close_failed(self, instance):
        self.dialog_failed.dismiss()
    def close_noname(self, instance):
        self.dialog_noname.dismiss()
    def close_ok(self, instance):
        self.dialog_ok.dismiss()
    def close_tutup(self, instance):
        self.dialog_tutup.dismiss()
    def close_nopas(self, instance):
        self.dialog_nopas.dismiss()
    def close_paskos(self, instance):
        self.dialog_paskos.dismiss()
    def close_adanum(self, instance):
        self.dialog_adanum.dismiss()
    def close_else(self, instance):
        self.dialog_else.dismiss()

    def login_button_action(self):
        numbers = ['1','2','3','4','5','6','7','8','9','0']

#berhasil login:
        if self.ids.passw.text=='123' and self.ids.uname.text is not '':
            print('test123')
            self.dialog_ok = MDDialog(
                title="Login Berhasil",
                text=("selamat datang di aplikasi BMI " +  self.ids.uname.text)+ '!',
                buttons=[
                    MDFlatButton(
                        text="OKE",
                        on_release=self.close_ok
                        ),
                ],
            )

            self.dialog_ok.open()
            self.manager.current = 'mainmenu2'
            self.ids.uname.text = ''
            self.ids.passw.text = ''

#tidak ada nama:
        elif self.ids.uname.text is '' and self.ids.passw.text=='123':
            self.dialog_noname = MDDialog(
                title="LOGIN GAGAL",
                text=f"Nama tidak boleh kosong",
                buttons=[
                    MDFlatButton(
                        text="Tutup",
                        on_release=self.close_noname
                        ),
                ],
            )
            self.dialog_noname.open()

#tidak ada password
        elif self.ids.uname.text is not '' and self.ids.passw.text=='':
            self.dialog_paskos = MDDialog(
                title="LOGIN GAGAL",
                text=f"Password tidak boleh kosong",
                buttons=[
                    MDFlatButton(
                        text="Tutup",
                        on_release=self.close_paskos
                        ),
                ],
            )
            self.dialog_paskos.open()

#password salah:
        elif self.ids.uname.text is not '' and self.ids.passw.text!='123':
            self.dialog_nopas = MDDialog(
                title="LOGIN GAGAL",
                text=f"Password salah",
                buttons=[
                    MDFlatButton(
                        text="Tutup",
                        on_release=self.close_nopas
                        ),
                ],
            )
            self.dialog_nopas.open()

#nama dan sandi kosong:
        elif self.ids.uname.text == '' and self.ids.passw.text=='':
            self.dialog_failed = MDDialog(
                title="LOGIN GAGAL",
                text=f"nama dan kata sandi tidak boleh kosong",
                buttons=[
                    MDFlatButton(
                        text="Tutup",
                        on_release=self.close_failed
                        ),
                ],
            )
            self.dialog_failed.open()
###################################################################################################
        elif any(i in self.ids.uname.text for i in numbers and self.ids.passw.text=='123'):
            self.dialog_adanum = MDDialog(
                title="LOGIN GAGAL",
                text=f"nama tidak boleh berisi angka",
                buttons=[
                    MDFlatButton(
                        text="Tutup",
                        on_release=self.close_adanum
                        ),
                ],
            )
                #{self.ids.user.text}!")
            self.dialog_adanum.open()
####################################################################################################
#else condition:
        else:
            self.dialog_else = MDDialog(
                title="LOGIN GAGAL",
                buttons=[
                    MDFlatButton(
                        text="Tutup",
                        on_release=self.close_else
                        ),
                ],
            )
                #{self.ids.user.text}!")
            self.dialog_else.open()
        
    def build(self):
        pass

#draw semua widget ke layar:
class BMIApp(MDApp):
    def build(self):
        sm = ScreenManager();
        #self.theme_cls.theme_style ='Dark'
        self.theme_cls.primary_palette = 'Orange'
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainMenu2(name='mainmenu2'))
        sm.add_widget(MainMenu(name='mainmenu'))
        sm.transition=RiseInTransition()
        #sm.transition.direction='up'
        #sm.add_widget(DaftarScreen(name='daftar'))
        sm.add_widget(LayarBMI(name='layarbmi'))
        sm.add_widget(TaskScreen(name='tasklist'))
        return sm

#run app
if __name__ ==  "__main__":
    BMIApp().run()
