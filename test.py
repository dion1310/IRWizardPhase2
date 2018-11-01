from __future__ import print_function,division

import kivy

kivy.require('1.10.1')


from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from os import listdir
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

kv_path = './kv/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path + kv)



class ScreenManage(ScreenManager):
    pass

class MainMenu(Screen):
    pass
class CaptureMenu(Screen):
    def modePopup(self):
        SelectModePopup().open()

class SelectModePopup(Popup):
    pass
class TempSettings(Screen):
    def checkActive(self,*args):
        pass

    def checkActive2(self,*args):
        pass

    def ActiveCI1(self,*args):
        pass
    def ActiveCI2(self,*args):
        pass

    def ActiveCI3(self,*args):
        pass
class FanSettings1(Screen):
    pass
class FanSettings2(Screen):
    def checkActive(self,*args):
        pass

    def checkActive2(self,*args):
        pass

    def ActiveCI1(self,*args):
        pass
    def ActiveCI2(self,*args):
        pass

    def ActiveCI3(self,*args):
        pass
class SwingSettings1(Screen):
    pass
class LouverSettings1(Screen):
    pass
class CaptureSession(Screen):
    pass
class FeatureTest(Screen):
    pass
class ScrollButton(Button):
    pass
class ProfileSelect(Screen):
    pass
class ProfileMenu(Screen):
    pass
class CapturePower(Screen):
    pass
class ScanDevices(Screen):
    pass



Screen = ScreenManage()
Screen.add_widget(MainMenu(name="menu"))
Screen.add_widget(CaptureMenu(name="capturemenu"))
Screen.add_widget(TempSettings(name="tempsettings"))
Screen.add_widget(FanSettings1(name="fansettings1"))
Screen.add_widget(FanSettings2(name="fansettings2"))
Screen.add_widget(SwingSettings1(name="swingsettings1"))
Screen.add_widget(LouverSettings1(name="louversettings1"))
Screen.add_widget(CaptureSession(name="capturesession"))
Screen.add_widget(FeatureTest(name="featuretest"))
Screen.add_widget(ProfileSelect(name="profileselect"))
Screen.add_widget(ProfileMenu(name="profilemenu"))
Screen.add_widget(CapturePower(name="capturepower"))
Screen.add_widget(ScanDevices(name="scandevices"))

class TestApp(App):
    def build(self):

        return ScanDevices()
test = TestApp()
test.run()