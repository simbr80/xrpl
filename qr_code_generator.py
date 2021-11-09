import qrcode
from PIL import Image

def get_qr_code(text):

    img = qrcode.make(text)
    img.show()


get_qr_code('rJnyoXNNLdXbjtKyUe8doFVLfpn3M79Npn')