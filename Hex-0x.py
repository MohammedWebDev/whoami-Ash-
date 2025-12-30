input_tezt = input("Enter text to encrypt: ")

class Cipher:
    def __init__(self, text):
        self._text = text  # حماية بسيطة للخاصية

    def encrypt(self):
        # تشفير بسيط: عكس النص
        return self._text[::-1]


class HexCipher(Cipher):
    def __init__(self, text):
        super().__init__(text)  # استدعاء الأب
        self._prefix = "0x"     # بادئة Hex

    def encrypt(self):
        reversed_text = super().encrypt()
        hex_text = ''.join(format(ord(c), '02x') for c in reversed_text)
        return self._prefix + hex_text


hex_cipher = HexCipher(input_tezt)

print(hex_cipher.encrypt())
