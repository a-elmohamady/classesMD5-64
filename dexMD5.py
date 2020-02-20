from pyaxmlparser import APK
import sys
import base64
import zipfile
import hashlib


apkFile = "WhatsApp.apk"
apk = APK(apkFile)

zipFile = zipfile.ZipFile(apkFile,'r')
classesDexFile = zipFile.read('classes.dex')
hash = hashlib.md5()
hash.update(classesDexFile)

print("Version: " + apk.version_name)
print("ClassesDex: " + base64.b64encode(hash.digest()).decode("utf-8"));
