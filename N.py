import nfc
import nfc.clf

def on_connect(tag):
    if tag.ndef:
        text = nfc.ndef.TextRecord("Hello, NFC!")
        ndef_message = nfc.ndef.Message(text)
        tag.ndef.message = ndef_message
        print("Message written to tag.")
        return True
    else:
        print("Tag is not NDEF formatted.")
        return False

with nfc.ContactlessFrontend('usb') as clf:
    clf.connect(rdwr={'on-connect': on_connect})
