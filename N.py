import nfc
import nfc.clf

def on_connect(tag):
    if tag.ndef:
        text = nfc.ndef.TextRecord("Reusable NFC Card")
        ndef_message = nfc.ndef.Message(text)
        tag.ndef.message = ndef_message
        print("Message written to tag.")
    else:
        print("Tag is not NDEF formatted.")
    return True

with nfc.ContactlessFrontend('usb') as clf:
    clf.connect(rdwr={'on-connect': on_connect})
