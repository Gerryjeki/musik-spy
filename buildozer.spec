[app]
title = Musik Spy
package.name = musikspy
package.domain = org.fake.music
source.dir = .
source.include_exts = py,kv
version = 0.1

requirements = kivy
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, READ_CONTACTS, INTERNET
android.archs = armeabi-v7a
android.sdk = 30
android.build_tools = 30.0.3

[buildozer]
log_level = 2
warn_on_root = 0
clean = 1
