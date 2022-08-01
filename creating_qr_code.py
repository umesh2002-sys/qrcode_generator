# making qr code


import pyqrcode
import png
from pyqrcode import QRCode

def QrCode():
    code_link = input("Insert website link to generate QRCode: ")
    name_qrcode = input("Name of the QRCode: ")
    url = pyqrcode.create(code_link)
    url.png(f'{name_qrcode}.png', scale= 6)


QrCode()
program_exit = input("Do you want to make another QRCode (yes/no): ").upper()
if program_exit == 'YES':
    QrCode()
else:
    print('Program Exit')



