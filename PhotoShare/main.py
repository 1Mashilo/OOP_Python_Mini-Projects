from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import time
import webbrowser
from filesharer import FileSharer

# Load KV file
Builder.load_file('frontend.kv')

class CameraScreen(Screen):
    def start(self):
        """Starts the camera and updates button text."""
        if not self.ids.camera.play:
            self.ids.camera.opacity = 1
            self.ids.camera.play = True
            self.ids.camera_button.text = "Stop Camera"

    def stop(self):
        """Stops the camera and updates button text."""
        if self.ids.camera.play:
            self.ids.camera.opacity = 0
            self.ids.camera.play = False
            self.ids.camera_button.text = "Start Camera"

    def capture(self):
        """Captures a photo and navigates to the ImageScreen."""
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = f"files/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    link_message = "Create a Link First"

    def create_link(self):
        """Uploads the photo to a sharing service."""
        try:
            file_path = App.get_running_app().root.ids.camera_screen.filepath
            filesharer = FileSharer(filepath=file_path)
            self.url = filesharer.share()
            self.ids.link.text = self.url
        except AttributeError:
            self.ids.link.text = self.link_message

    def copy_link(self):
        """Copies the generated link to the clipboard."""
        if hasattr(self, 'url'):
            Clipboard.copy(self.url)
        else:
            self.ids.link.text = self.link_message

    def open_link(self):
        """Opens the generated link in a web browser."""
        if hasattr(self, 'url'):
            webbrowser.open(self.url)
        else:
            self.ids.link.text = self.link_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
