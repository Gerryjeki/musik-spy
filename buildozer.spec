[app]
title = Musik Player
package.name = musikspy
package.domain = org.fake.music
source.include_exts = py,kv
version = 0.1

requirements = kivy

android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, READ_CONTACTS, INTERNET
android.arch = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 0
