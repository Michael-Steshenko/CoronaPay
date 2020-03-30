# requires pip install pillow

import qrcode
#from PIL import Image, ImageDraw
#from qrcode.image.pil import PilImage

# generate a paypal payment link to the user identified by "email" for "sum" amount
def CreatePayPalLink(sum, email):
    BaseUrl = "https://www.paypal.com/cgi-bin/webscr?cmd=_xclick&business=EMAIL&amount=SUM&currency_code=ILS&item_name=test"
    return BaseUrl.replace("SUM", sum).replace("EMAIL", email)

def CreateQRPayCode(sum, email):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    # The data that you want to store
    data = CreatePayPalLink(sum, email)
    # Add data
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image()

    # Save it somewhere, change the extension as needed:
    # img.save("image.png")
    # img.save("image.bmp")
    # img.save("image.jpeg")
    img.save("image.jpg")


#CreateQRPayCode("20", "oblivic90@gmail.com")

#print(CreatePayPalLink("20", "oblivic90@gmail.com"))